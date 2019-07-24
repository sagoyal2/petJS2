import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def localhost(driver):
    driver.get("http://localhost:5000")
    driver.execute_script(
        'return document.getElementById("nothere").setAttribute("style", "background-color: rgb(190, 11, 80);position: absolute;top:700px;left: 85px;")')


def pizzapage(driver, place):

    if(place is "dominos"):
        driver.get("https://www.dominos.com/en/")

    if(place is "sarpinos"):
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


def main():
    driver = webdriver.Chrome()

    pizzapage(driver, "dominos")
    # pizzapage(drive, "sarpinos")

    input("Press Enter to end...")


if __name__ == "__main__":
    main()
