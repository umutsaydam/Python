from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://github.com/john?tab=followers"

driver = webdriver.Edge()

driver.get(url)
time.sleep(2)

followers = []

while True:
    items = driver.find_elements(
        By.CLASS_NAME, "d-table.table-fixed.col-12.width-full.py-4.border-bottom.color-border-muted")

    for i in items:
        followers.append(i.find_element(By.CLASS_NAME, "Link--secondary").text)

    time.sleep(1)
    page = driver.find_element(
        By.CLASS_NAME, "pagination").find_elements(By.TAG_NAME, "a")

    if len(page) == 1 and page[0].text == "Next":
        page[0].click()
    elif len(page) == 2 and page[1].text == "Next":
        page[1].click()
    elif len(page) == 1 and page[0].text == "Previous":
        break
    else:
        continue

    time.sleep(2)

print(followers)