from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = "https://instagram.com"
        self.driver = webdriver.Edge()
        self.getDriver()

    def getDriver(self):
        self.driver.get(self.url)
        time.sleep(2)

    def signIn(self):
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        password.send_keys(Keys.ENTER)
        time.sleep(3)

    def sendMessage(self, target, message):
        self.driver.find_element(
            By.CLASS_NAME, "XTCLo.d_djL.DljaH").send_keys(target)
        time.sleep(2)
        list = self.driver.find_elements(By.CLASS_NAME, "-qQT3")
        self.driver.get(list[0].get_attribute("href"))
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "_acan._acap._acat").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, "textarea").send_keys(message)
        time.sleep(4)
        self.driver.find_element(By.TAG_NAME, "textarea").send_keys(Keys.ENTER)
       


a = Instagram("umut.saydm", "umtsydm01")
a.signIn()

a.sendMessage("turker_saydam", "sdfsdfsd")
