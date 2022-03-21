from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
from random import seed
from random import randint

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

class InstaBot:
    def __init__(self, username, password):
        driver.implicitly_wait(30)
        driver.get("https://instagram.com")    
        driver.implicitly_wait(30)  
        time.sleep(getRandomTime())
        driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys('_gautambisht_11')
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys('e8c2cadf2148')
        time.sleep(getRandomTime())      
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        
        try:
           time.sleep(5)
           driver.implicitly_wait(30)
           search_2 = driver.find_element_by_xpath('//input[@placeholder="Search"]')
           search_2.send_keys("cristiano")
           time.sleep(5)
           search_2.send_keys(Keys.ENTER)   
           count = 0
           while count <2:
               search_2.send_keys(Keys.ENTER)
               count +=1 # count = count +1
               time.sleep(1)

        except: 
             while True: 

                  driver.implicitly_wait(30)
                  follow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button').click()
                  print('Following')
                  time.sleep(30)
                  unfollow1 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button').click()
                  time.sleep(2)
                  unfollow2 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
                  print('Unfollowed')
                  time.sleep(6)



def getRandomTime():
        randTime = randint(3, 5)
        return randTime      
InstaBot("your_usernmae", "your_password")   





