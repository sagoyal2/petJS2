from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get("http://localhost:5000")
# driver.get("https://www.dominos.com/en/")
driver.get(
    "https://www.gosarpinos.com/pizza-delivery/naperville-sarpinos#!/Review/4")
# elem = driver.find_element_by_class_name("signs__apply")
# elem.click()

length = driver.execute_script('return document.styleSheets.length')

for i in range(length):
    link = driver.execute_script(
        'return document.styleSheets['+str(i)+'].href')
    if(link):
        print(link)
