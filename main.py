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
        self.brands_URL = []
        self.brands_list = ["protein", "bars", "clothing", "vitamins", "vegan", "creatine"]
        self.driver.get(self.URL)
        self.delay = 10

    # Creating a wrapper for all functions
    def start_scraper(self):
       self.accept_cookies()
       self.get_brands_url()
    
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

    # Creating a function of user input, and let the user to choose brand
    def get_brands_url(self):
        while True:
            try: 
                # GET USER CHOICE
                if len(self.brands_URL) == 0:
                    user_product_type = input(f'''
                    ####### PLEASE SELECT WHICH PRODUCT YOU WANT TO GET DATA FROM #########
                    #######################################################################
                    ---> {self.brands_list} <---
                    ''')
                    print()
                else:
                    if len(self.brands_URL) == 6:
                        break
                    else:
                        user_product_type = input(f'''
                        ####### ADD MORE PRODUCTS OR PRESS "n" TO FINISH! #########
                        #######################################################################
                        ---> {self.brands_list} <---
                        ''')
                        print()

                        if user_product_type.lower() == "n":
                            break
                
                # Call function to get specific brand link and name
                self.choose_brand(user_product_type.lower())
     
            except:
                print("Invalid Selection!")
    
    # Get a link of a specific brand
    def choose_brand(self, user_input):
        index = 0
        # Find the links index from a DOM of a chosen brand
        if user_input == "protein":
            index = 1
        elif user_input == "bars":
            index = 2
        elif user_input == "clothing":
            index = 3
        elif user_input == "vitamins":
            index = 4
        elif user_input == "vegan":
            index = 5
        elif user_input == "creatine":
            index = 6
        
        if user_input in self.brands_list:
            link = self.driver.find_element(By.XPATH, f"//div[@class='brandLogos trackwidget componentWidget']/a[{index}]").get_attribute("href")

            brand_object = {"brand": user_input, "link": link}
            # Store brand details
            self.brands_URL.append(brand_object)
            i = self.brands_list.index(user_input)
            # Delete the specific brand to make sure wont be chosen next time
            del self.brands_list[i]
        else:
            # Reject input if brand chosen already or not valid!
            print("This Product Is Already Selected or Not Valid")



scraper = Scraper()
scraper.start_scraper()