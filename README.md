# GradconnectionScraper

Command-line based web scraping app built with python and the Selenium library. 

Uses chromedriver to get the page and load gradconnection's internship page. Waits for the job containers to load and find the job cards by their class name. Prepares a list and iterate over the job cards and append the details found within the job cards (based on class name) to the list. Exports to CSV and quit the driver. 

