from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Set up driver
driver = webdriver.Chrome()

# Load the page
driver.get("https://au.gradconnection.com/internships/")

# Wait for job containers to load (use the real class from the site)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "campaign-box"))
)

# Find all job cards by their actual container class
job_cards = driver.find_elements(By.CLASS_NAME, "campaign-box")

# Prepare a list to store job data
job_data = []

for card in job_cards:
    try:
        title = card.find_element(By.CLASS_NAME, "box-header").text
        description = card.find_element(By.CLASS_NAME, "box-description").text
        link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
        job_data.append([title, description, link])
    except:
        continue  # Skip any card that causes errors

# Export to CSV
with open("internships.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Description", "Link"])
    writer.writerows(job_data)

print("Done! ✅ Exported to internships.csv")

driver.quit()
