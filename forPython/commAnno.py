import re
import requests
from bs4 import BeautifulSoup


def main():

    page_link = "https://en.wikipedia.org/wiki/Pasta"

    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    # file1 = open("allwiki.html", 'w')
    # file1.write(str(soup.prettify))
    # file1.close()

    result = soup.find_all(
        'div', {"class": re.compile(r'nav\w+')})

    print(result[0])


if __name__ == "__main__":
    main()
