from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
from random import seed
from random import randint

chrome_options = webdriver.ChromeOptions()

chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

while True:
     driver.get('''https://www.youtube.com/watch?v=LVYMwW79j6Q''')
     time.sleep(5)
     driver.execute_script('''window.open("https://www.youtube.com/watch?v=LVYMwW79j6Q", "_blank");''')
     time.sleep(5)
     driver.execute_script('''window.open("https://www.youtube.com/watch?v=LVYMwW79j6Q", "_blank");''')
     time.sleep(5)
     driver.execute_script('''window.open("https://www.youtube.com/watch?v=LVYMwW79j6Q", "_blank");''')
     time.sleep(5)

     driver.execute_script('''window.open("https://www.youtube.com/watch?v=LVYMwW79j6Q", "_blank");''')
     time.sleep(5)
     
     driver.execute_script('''window.open("https://www.youtube.com/watch?v=LVYMwW79j6Q", "_blank");''')
     time.sleep(66)
     print('Done')
     driver.quit()
     time.sleep(5)

