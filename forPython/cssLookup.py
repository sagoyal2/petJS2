import os
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def localhost(driver):
    driver.get("http://localhost:5000")
    driver.execute_script(
        'return document.getElementById("nothere").setAttribute("style", "background-color: rgb(190, 11, 80);position: absolute;top:700px;left: 85px;")')


def anyCss(driver, link):

    # "https://www.dominos.com/en/"
    # "https://www.gosarpinos.com/pizza-delivery/naperville-sarpinos#!/Review/4"

    driver.get(link)
    length = driver.execute_script('return document.styleSheets.length')

    all_links = []

    print("Saving Following CSS files")

    for i in range(length):
        link = driver.execute_script(
            'return document.styleSheets['+str(i)+'].href')
        if(link):
            print(link)
            all_links.append(link)

    return all_links


def saveAllCss(links):

    for link in links:
        # change name
        full_name = str(link)
        saved_name = re.findall(r"(?<=css\/).*$", full_name)[0]

        # get code
        retrieved = requests.get(link)

        # save css
        open_file = open(os.path.join('savedCss', saved_name), 'w')
        open_file.write(retrieved.text)
        open_file.close()

    print("Saved")


def main():
    driver = webdriver.Chrome()

    # save all css_files for
    all_links = anyCss(driver, "https://randyzwitch.com/")
    saveAllCss(all_links)

    input("Press Enter to end...")


if __name__ == "__main__":
    main()
