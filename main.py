from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

class Scraper():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.URL = "https://www.myprotein.com/"
        self.product_URL = []
        self.driver.get(self.URL)
        self.delay = 10

    # Creating a wrapper for all functions
    def start_scraper(self):
       self.accept_cookies()
    
    # This function is accept cookies
    def accept_cookies(self):
        try:
            accept_cookies_button = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//button[@class='cookie_modal_button']")))
            
            accept_cookies_button.click()
            time.sleep(1)
            self.close_signup_modal()
        except TimeoutException:
            print("Loading took too much time!")
    
    def close_signup_modal(self):
        try:
            # Wait for the modal to appear
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//*[@class='emailReengagement show']")))
            
            # exit the modal
            exit_modal = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, "//button[@class='emailReengagement_close_button']")))
            
            exit_modal.click()
            time.sleep(1)
        except TimeoutException:
            print("Loading took too much time!")


scraper = Scraper()
scraper.start_scraper()