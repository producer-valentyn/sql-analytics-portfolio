# Online Store Analytics Automation

## Project Overview

This project automates the analysis of online store event data using Python. It processes a CSV dataset, checks data quality, generates analytical reports, and creates visualizations.

The project was originally developed as part of my Data Analytics studies, using data extracted from Google BigQuery. The current version runs locally on a CSV dataset.

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- CSV data processing
- Data quality checks
- Automated reporting and visualization

## Dataset

The dataset contains 800,996 rows and 9 columns, covering the period from November 1, 2020, to January 27, 2021.

It includes information about:
- Dates and countries
- Devices and continents
- Traffic channels
- Events and event values
- Test groups

## Automated Workflow

The `run_analysis.py` script performs the following steps:

1. Loads the input CSV dataset.
2. Checks the data structure and quality.
3. Identifies duplicate rows and invalid or missing values.
4. Generates summary reports grouped by different dimensions.
5. Creates charts showing event activity over time, by device, and by traffic channel.
6. Saves the generated CSV reports and charts to the `output/` directory.

## Project Structure

```text
Online_Store_Analytics/
├── online_store_dataset.csv
├── run_analysis.py
├── README.md
└── output/
    ├── data_overview.csv
    ├── data_quality_report.csv
    ├── daily_events.csv
    ├── events_by_country.csv
    ├── events_by_continent.csv
    ├── events_by_device.csv
    ├── events_by_channel.csv
    ├── events_by_test.csv
    ├── events_by_test_group.csv
    ├── events_summary.csv
    ├── test_groups_summary.csv
    └── charts/
```

## How to Run

### 1. Install dependencies

```bash
pip install pandas matplotlib
```

### 2. Prepare the dataset

Place `online_store_dataset.csv` in the same directory as `run_analysis.py`.

### 3. Run the script

```bash
python run_analysis.py
```

The script creates the `output/` directory and saves the reports and charts automatically.

## Key Skills Demonstrated

- Automating a repeatable data analysis workflow
- Data validation and quality checks
- Data aggregation using Pandas
- Generating CSV reports
- Creating data visualizations
- Organizing a Python analytics project

## Limitations

The current version processes a local CSV file. It does not connect directly to BigQuery or automatically retrieve updated data.

The results depend on the structure and contents of the provided dataset.
