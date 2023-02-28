from selenium import webdriver
from selenium.webdriver.common.by import By #used for finding element using Name,ID,Class,Tag name https://selenium-python.readthedocs.io/locating-elements.html
from selenium.webdriver.common.keys import Keys#used for button trigger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#path is used for chrome or IE or firefox downloaded driver link
#PATH = "C:/programfiles/chromedriver.exe"
#driver=webdriver.Chrome(PATH)
driver=webdriver.Chrome()
driver.get("https://www.techwithtim.net/")
#driver.title for extract title from webpage
#print(driver.title)
#print(driver.page_source)#find the entire html page document
search=driver.find_element(By.NAME,"s") #search proper element in webpage using name attribute
search.send_keys("test")#send test to the s name search box
search.send_keys(Keys.RETURN)# Enter key is used as RETURN
#wait for trigger the search button and load the new page and extract information
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    #print(main.text)
    articles=main.find_elements(By.TAG_NAME,"article")
    for article in articles:
        header=main.find_element(By.CLASS_NAME,"entry-summary")
        print(header.text)
except:
    driver.quit()
#main=driver.find_element(By.ID,"main")
#print(main.text)#all text data
#time.sleep(5)# sleep for 5 seconds
driver.quit()
#driver.close() for closing one tab
#driver.quit() for closing browser