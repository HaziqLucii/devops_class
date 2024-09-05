from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Navigate to the add POI page
    driver.get("http://localhost:8000/poi/add/")

    # Wait for the form to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "form"))
    )

    # Fill out the form fields
    driver.find_element(By.NAME, "name").send_keys("Test POI")
    driver.find_element(By.NAME, "description").send_keys("This is a test POI.")
    driver.find_element(By.NAME, "latitude").send_keys("51.5074")
    driver.find_element(By.NAME, "longitude").send_keys("-0.1278")
    driver.find_element(By.NAME, "poi_type").send_keys("Test Type")

    # Submit the form
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for the redirect to the POI map page
    WebDriverWait(driver, 10).until(
        EC.url_to_be("http://localhost:8000/poi/")
    )


finally:
    # Close the WebDriver
    driver.quit()