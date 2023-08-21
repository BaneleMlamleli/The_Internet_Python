from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import *
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.kineticskunk.co.za/")
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='A/B Testing']").click()
time.sleep(3)

print('test run done')