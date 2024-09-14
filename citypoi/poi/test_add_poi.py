from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (e.g., Chrome)
class TestDevopstest():
  def setup_method(self):
    #self.driver = webdriver.Remote('http://selenium__standalone-chrome:4444/wd/hub', options=webdriver.ChromeOptions())
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_devopstest(self):
    self.driver.get("http://localhost/")

    # Wait for the form to be visible
    WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "form"))
    )

    # Fill out the form fields
    self.driver.find_element(By.NAME, "name").send_keys("Test POI")
    self.driver.find_element(By.NAME, "description").send_keys("This is a test POI.")
    self.driver.find_element(By.NAME, "latitude").send_keys("51.5074")
    self.driver.find_element(By.NAME, "longitude").send_keys("-0.1278")
    self.driver.find_element(By.NAME, "poi_type").send_keys("Test Type")

    # Submit the form
    self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for the redirect to the POI map page
    WebDriverWait(self.driver, 10).until(
        EC.url_to_be("http://localhost/poi/")
    )