from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

driver.implicitly_wait(30)
driver.get("https://instagram.com/virat.kohli/") 
driver.implicitly_wait(30)
login = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()
driver.implicitly_wait(30)
time.sleep(3)
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.click()
username.send_keys('_gautambisht_11')
time.sleep(1)
password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.click()
time.sleep(1)
password.send_keys('e8c2cadf2148')
subit = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(5)
driver.implicitly_wait(30)
noti = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(5)
driver.implicitly_wait(30)
while True: 

    driver.implicitly_wait(30)
    follow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button').click()
    time.sleep(20)
    unfollow1 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button').click()
    time.sleep(2)
    unfollow2 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
    print('unfollowing')
    time.sleep(6)
    
