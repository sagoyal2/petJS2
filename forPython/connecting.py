import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def localhost(driver):
    driver.get("http://localhost:5000")
    driver.execute_script(
        'return document.getElementById("nothere").setAttribute("style", "background-color: rgb(190, 11, 80);position: absolute;top:700px;left: 85px;")')


def anycss(driver, link):

    # "https://www.dominos.com/en/"
    # "https://www.gosarpinos.com/pizza-delivery/naperville-sarpinos#!/Review/4"

    driver.get(link)
    length = driver.execute_script('return document.styleSheets.length')

    all_links = []

    for i in range(length):
        link = driver.execute_script(
            'return document.styleSheets['+str(i)+'].href')
        if(link):
            print(link)
            all_links.append(link)

    return all_links


def savecss(whichlink):
    returned = requests.get(whichlink)

    # print(returned.text)

    file1 = open("alltext.css", 'w')
    file1.write(returned.text)
    file1.close()


def main():
    driver = webdriver.Chrome()

    # localhost(driver)
    all_links = anycss(driver, "https://randyzwitch.com/")
    savecss(all_links[2])

    # css_selector = ".navbar-default"
    # css_property = "background-color"
    # attribute_name = "style"

    css_selector = "iframe"
    attribute_name = "style"

    # elem = driver.find_element_by_css_selector(css_selector)
    # print(elem.value_of_css_property(css_property))

    # RANDOM AI STUFF GOES HERE
    generated_result = "position: absolute; top:700px; left: 85px"

    # script = "document.querySelector(\"" + css_selector + "\").setAttribute(\"" + \
    #     attribute_name + "\", \"" + css_property + ":" + generated_result + "\")"

    script = "document.querySelector(\"" + css_selector + "\").setAttribute(\"" + \
        attribute_name + "\", \"" + generated_result + "\")"

    driver.execute_script(script)

    input("Press Enter to end...")


if __name__ == "__main__":
    main()
