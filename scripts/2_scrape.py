import requests
from bs4 import BeautifulSoup
import re
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import pandas as pd

# Load suburb URLs from CSV
suburbs = pd.read_csv("../project-2-group-real-estate-industry-project-25/data/landing/url-site.csv")
suburbs_with_zip_codes = list(suburbs["url"])

home_url = "https://www.domain.com.au/"

def fetch_page(url, retries=3, delay=5):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive'
    }
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1}/{retries} failed for URL: {url}. Error: {e}")
            time.sleep(delay)
    return None

def scrape_property_details(url):
    print(f"Scraping details for: {url}")
    response = fetch_page(url)
    if not response:
        return None
    
    bsobj = BeautifulSoup(response.text, "lxml")
    pattern1 = re.compile(r'>(.+)<.')
    pattern2 = re.compile(r'destination=(.+)" rel=.')
    
    try:
        property_name = bsobj.find("h1", {"class": "css-164r41r"}).text.strip() if bsobj.find("h1", {"class": "css-164r41r"}) else None

        property_price = bsobj.find("div", {"data-testid": "listing-details__summary-title"})
        property_price = pattern1.findall(str(property_price))[0] if property_price else None

        all_basic_features = bsobj.find("div", {"data-testid": "property-features-wrapper"})
        all_basic_features = all_basic_features.findAll("span", {"data-testid": "property-features-text-container"}) if all_basic_features else []
        
        property_features = []
        for feature in all_basic_features:
            property_features.append(feature.contents[0].strip())
        
        # Handle missing features (Bedrooms, Bathrooms, Parking)
        bedrooms = property_features[0] if len(property_features) > 0 else "-"
        bathrooms = property_features[1] if len(property_features) > 1 else "-"
        parking = property_features[2] if len(property_features) > 2 else "-"

        type_div = bsobj.find("div", {"data-testid": "listing-summary-property-type"})
        property_type = type_div.find("span").text.strip() if type_div and type_div.find("span") else "N/A"


        lat_long = bsobj.find("a", {"target": "_blank", 'rel': "noopener noreferrer"})
        latitude, longitude = None, None
        
        if lat_long:
            lat_long_match = pattern2.findall(str(lat_long))
            if lat_long_match:
                latitude, longitude = lat_long_match[0].split(',')


        extras = []
        extra_features = bsobj.find("ul", {"class": "css-4ewd2m"})
        extra_features = extra_features.findAll("li", {"data-testid": "listing-details__additional-features-listing", "class": "css-vajaaq"}) if extra_features else []
        for extra in extra_features:
            extras.append(extra.contents[0].strip())

        property_header = bsobj.find("h3", {"data-testid": "listing-details__description-headline"})
        property_headline = property_header.get_text(strip=True) if property_header else "N/A"
   
        property_description = ""
        if property_header:
            for p in property_header.find_next_siblings('p'):
                property_description += p.get_text(strip=True) + " "
    
        listing_summary = bsobj.find("ul", {"data-testid": "listing-summary-strip", "class": "css-1h9anz9"})
        availability = date_available = bond = internal_area = land_area = "-"
        if listing_summary:
            list_items = listing_summary.find_all("li")
            for li in list_items:
                if "Date Available" in li.text:
                    date_available = li.find("strong").text.strip()
                elif "Available from" in li.text:
                    availability = li.find("strong").text.strip()
                elif "Bond" in li.text:
                    bond = li.find("strong").text.strip()
                elif "Internal area" in li.text:
                    internal_area = li.find("strong").text.strip()
                elif "Land area" in li.text:
                    land_area = li.find("strong").text.strip()

        return {
            "URL": url,
            "Rent_Price": property_price,
            "Address": property_name,
            "Bedrooms": bedrooms,
            "Bathrooms": bathrooms,
            "Parking": parking,
            "Property_Type": property_type,
            "Latitude": latitude,
            "Longitude": longitude,
            "Property_Headline": property_headline,
            "Property_Description": property_description.strip(),
            "Extra_Features": ', '.join(extras),
            "Date_Available": date_available,
            "Availability" : availability,
            "Bond": bond,
            "Internal_Area": internal_area,
            "Land_Area": land_area
        }
    except Exception as e:
        print(f"Error extracting details from {url}: {e}")
        return None

def scrape_page(suburb, page_number):
    print(f"Scraping page {page_number} for suburb {suburb}...")
    response = fetch_page(f"{home_url}/rent/{suburb}/?page={page_number}")
    if response:
        bsobj = BeautifulSoup(response.text, "lxml")
        result_list = bsobj.find("ul", {"data-testid": "results"})
        if result_list:
            all_links = result_list.findAll("a", href=re.compile(r"https://www.domain.com.au/*"))
            return list(set(link.attrs['href'] for link in all_links if 'href' in link.attrs))
    return None

def main():
    list_of_links = []
    properties_details = []

    with ThreadPoolExecutor(max_workers=20) as executor: 
        for suburb in suburbs_with_zip_codes:
            suburb_has_links = False
            page_number = 1
            while True:
                future = executor.submit(scrape_page, suburb, page_number)
                links = future.result()

                if links:
                    suburb_has_links = True
                    list_of_links.extend(links)
                    page_number += 1
                else:
                    if not suburb_has_links:
                        print(f"No links found for {suburb}. Moving to next suburb.")
                    else:
                        print(f"No more links found for {suburb} at page {page_number}.")
                    break


    list_of_links = list(set(list_of_links))
    with ThreadPoolExecutor(max_workers=20) as executor: 
        future_to_link = {executor.submit(scrape_property_details, link): link for link in list_of_links}
        for future in as_completed(future_to_link):
            property_details = future.result()
            if property_details:
                properties_details.append(property_details)


    cwd = os.getcwd()
    csv_file = os.path.join(cwd, "data/landing/alt_properties2.csv")
    csv_columns = [
        "URL", "Rent_Price", "Address", "Bedrooms", "Bathrooms", "Parking", "Property_Type",
        "Latitude", "Longitude", "Property_Headline", "Property_Description", "Extra_Features",
        "Date_Available", "Availability", "Bond", "Internal_Area", "Land_Area"
    ]

    os.makedirs(os.path.dirname(csv_file), exist_ok=True)
    try:
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=csv_columns)
            writer.writeheader()
            for data in properties_details:
                writer.writerow(data)
        print(f"\nData has been saved to {csv_file}")
    except IOError as e:
        print(f"Error saving to CSV: {e}")

if __name__ == "__main__":
    main()
