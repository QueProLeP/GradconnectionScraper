# GradconnectionScraper

Command-line based web scraping app built with python and the Selenium library. 

Uses chromedriver to get the page and load gradconnection's internship page. Waits for the job containers to load and find the job cards by their class name. Prepares a list and iterate over the job cards and append the details found within the job cards (based on class name) to the list. Exports to CSV and quit the driver. 


# Internship Scraper 

This is a simple Python command-line tool that scrapes internship listings from [GradConnection Australia](https://au.gradconnection.com/internships/) and exports the data to a CSV file.

## Features

- Collects internship job titles, descriptions, and links.
- Exports the data to `internships.csv`.
- Uses Selenium for robust browser automation.

## Requirements

- Python 3.7+
- Google Chrome installed
- ChromeDriver (should be on your PATH)

## Setup Instructions

1. Clone this repository or download the script.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

  Make sure you have the correct version of ChromeDriver installed and accessible in your system's PATH.
3. Run the scraper:
  ```bash
  python scraper.py
  ```
  Output
  internships.csv will contain the internship listings in the format

