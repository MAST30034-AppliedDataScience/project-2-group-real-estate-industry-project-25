# Real Estate Rental Prices Prediction in Victoria, Australia

This guide will walk you through setting up, running, and understanding the project to analyze real estate data using location-based analysis, data scraping, and predictive modeling.

## Table of Contents
1. [Clone the Repository](#1-clone-the-repository)
2. [Install Dependencies](#2-install-dependencies)
3. [Obtain an API Key](#3-obtain-an-api-key)
4. [Data Collection](#4-data-collection)
5. [Data Scraping](#5-data-scraping)
6. [Data Preprocessing](#6-data-preprocessing)
7. [Exploratory Data Analysis (EDA)](#7-exploratory-data-analysis-eda)
8. [School Count Analysis](#8-school-count-analysis)
9. [Feature Selection](#9-feature-selection)
10. [Model Building and Evaluation](#10-model-building-and-evaluation)

## 1. Clone the Repository

First, open your terminal and run the following commands to clone the project repository and navigate into the project directory:

```bash
git clone https://github.com/MAST30034-AppliedDataScience/project-2-group-real-estate-industry-project-25.git
cd project-2-group-real-estate-industry-project-25
```

## 2. Set Up a Python Virtual Environment (Recommended)
Setting up a virtual environment ensures that your project dependencies are isolated from other Python projects on your system.

1. Create a virtual environment (you can replace venv with any name you prefer):
``` bash
conda create -n group25env python=3.11.5
```

2. Activate the virtual environment:

  ``` bash
  conda activate group25env
  ```


After activating, your terminal should show the virtual environment's name, like (group25env).


## 3. Install Dependencies

Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

## 4. Obtain an API Key

To use the OpenRouteService API for location-based analysis, follow these steps:

1. Sign up or log in to [OpenRouteService (OSM)](https://openrouteservice.org/dev/#/login) and generate an API key.
2. In the project directory, go to the `config` folder.
3. Open the `api_key.txt` file (create one if it doesn't exist) and paste your OpenRouteService API key into the file.
4. Ensure there are no spaces or extra lines, and save the file.

## 5. Data Collection

Navigate to the `notebooks` directory and run the data collection notebook to fetch external datasets:

```bash
cd notebooks
jupyter notebook DataCollecting.ipynb
```

* Run all cells to download datasets and generate a list of target suburbs for further analysis.

## 6. Data Scraping

To collect property data from Domain.com.au, run the following script located in the `scripts` folder:

```bash
cd ../scripts
python scrape.py
```
**Note:** The data scraping process may take 30-40 minutes, depending on your machine. For example, an M2 MacBook Air (8GB RAM) takes approximately 40 minutes.


## 7. Data Preprocessing

Preprocess the collected data to prepare it for analysis. Run the preprocessing notebook and make sure to insert your OpenRouteService API key when prompted:

```bash
cd ../notebooks
jupyter notebook PreProcessing.ipynb
```
* This step includes cleaning the data, handling missing values, converting categorical data, and addressing outliers.

## 8. Exploratory Data Analysis (EDA)

To gain insights into the dataset, open and run the EDA notebook:

```bash
jupyter notebook EDA.ipynb
```

* This notebook provides visualizations, feature distributions, and insights into the significance of various columns.

## 9. School Count Analysis

To analyze the impact of nearby schools on property prices, run the following notebook:

```bash
jupyter notebook SchoolCountAnalysis.ipynb
```

* This notebook aggregates nearby school counts and creates a feature that captures the number of schools within a 2km radius for each property.

## 10. Feature Selection

Feature engineering and selection are critical for model building. Use the following notebook to perform feature scaling, one-hot encoding, KNN imputation, PCA, and mutual information analysis:

```bash
jupyter notebook FeatureSelections.ipynb
```

## 11. Model Building and Evaluation

To construct predictive models, open and run the Model Building notebook:

```bash
jupyter notebook ModelBuilding.ipynb
```

* This notebook covers the creation and evaluation of various models, including simple regression models, stacked models, and deep learning approaches.
