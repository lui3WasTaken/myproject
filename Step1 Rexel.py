from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

class Step1:
    def __init__(self,clicks):
        self.driver = webdriver.Chrome()
        self.url = "https://orteil.dashnet.org/cookieclicker/"
        self.clicks = clicks
    def click_cookie(self):
        self.driver.get(self.url)
        time.sleep(5)
        elems= self.driver.find_elements_by_id("bigCookie")
        self.highest = 0
        self.lowest = 0
        while True:
            prices = self.driver.find_elements_by_class_name("price")
            for price in prices:
                print(price.text)
                if price.text > self.highest:
                    self.highest = price.text
                
            for elem in elems:
                elem.click()

    def quit_driver(self):
        time.sleep(5)
        self.driver.close()
i = Step1(clicks=500)
i.click_cookie()
i.quit_driver()