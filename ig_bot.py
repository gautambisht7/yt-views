import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver



# initialize driver

driver = webdriver.Edge(executable_path="msedgedriver.exe")
driver.get('https://www.instagram.com/')
driver.implicitly_wait(30)

    # accepting the cookies
try:
    cookies_accept= driver.find_element_by_xpath('//button[text()="Accept"]')
    cookies_accept.click()
    time.sleep(1)
except:
    pass

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

username.click()
username.send_keys('_gautambisht_11')
time.sleep(1)

password.click()
password.send_keys('e8c2cadf2148')
time.sleep(1)

log_in=driver.find_element_by_xpath('//div[text()="Log In"]')
log_in.click()
time.sleep(4)

    # credential storage
try:
    driver.implicitly_wait(30)
    credentials= driver.find_element_by_xpath('//button[text()="Not Now"]')
    credentials.click()
    time.sleep(1)
except:
    pass

    #  notifications
try:
    driver.implicitly_wait(30)
    notifications = driver.find_element_by_xpath('//button[text()="Not Now"]')
    notifications.click()
    time.sleep(1)
except:
    pass


        
search_1 = driver.find_element_by_xpath('//span[text()="Search"]')
driver.implicitly_wait(30)
search_1.click()
time.sleep(1)
search_2 = driver.find_element_by_xpath('//input[@placeholder="Search"]')
search_2.send_keys('virat.kohli')
driver.implicitly_wait(30)
search_2.send_keys(Keys.ENTER)   
time.sleep(1)
count = 0
while count <3:
 search_2.send_keys(Keys.ENTER)
 count +=1 # count = count +1
 driver.implicitly_wait(30)
      
time.sleep(1)
driver.implicitly_wait(30)
follow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
follow.click()
time.sleep(15)
unfollow1 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button')
driver.implicitly_wait(30)
unfollow1.click()
unfollow2 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]')
driver.implicitly_wait(30)
unfollow2.click()
        

