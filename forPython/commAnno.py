import re
import json
import pprint
import requests
from bs4 import BeautifulSoup


def createStructure(soup):
    # mylist = []
    # count = 0

    # for tag in soup.find_all():

    #     mylist.append(
    #         (tag.name, tag.attrs, [parent.name for parent in tag.parents if parent.name != '[document]']))

    #     if count > 10:
    #         break
    #     count += 1

    mylist = [({'tag_name': tag.name}, {"tag_attrs": tag.attrs}, {"tag_parents": [parent.name for parent in tag.parents if parent.name !=
                                                                                  '[document]']}) for tag in soup.find_all()]

    open_file = open("savedlist.json", 'w')
    open_file.write(json.dumps(mylist))
    open_file.close()

    pprint.pprint(mylist)


def main():

    page_link = "https://randyzwitch.com/"

    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    # createStructure(soup)

    json_file = open("savedlist.json", "r")
    data = json.load(json_file)
    json_file.close()

    # print(data[27])
    # print('class' in data[27][1].get("tag_attrs").keys())

    for i in range(len(data)):
        if('class' in data[i][1].get("tag_attrs").keys()):
            print(data[i])


if __name__ == "__main__":
    main()
