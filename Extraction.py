import requests
from bs4 import BeautifulSoup

# url of list of classes
url = "https://umtc.catalog.prod.coursedog.com/courses?page=1&cq="


def find_divs(element):
    if element.name == 'div':
        text = element.text
        file.write(text)
        file.write("\n")
    for child in element.find_all('div', recursive=True):
        find_divs(child)

try:
    response = requests.get(url)

    if response.status_code == 200:
        file = open('output.txt', 'w')
        soup = BeautifulSoup(response.text, 'html.parser')

        find_divs(soup.html)

        file.close()

        print("Text extracted and saved to 'output.txt'")
    else:
        print("Failed to retrieve web page. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error: ", e)
