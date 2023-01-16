from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

url = "https://github.com/"

driver.get("https://github.com/")
time.sleep(5)
searchInput = driver.find_element(By.NAME, "q")

searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(3)

result = driver.find_elements(By.CLASS_NAME, "v-align-middle")

for i in result:
    print(i.text)

driver.close()