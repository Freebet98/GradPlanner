import requests
from bs4 import BeautifulSoup

#url of list of classes
url = "https://umtc.catalog.prod.coursedog.com/courses?page=1&cq="

try:
    response = requests.get(url)

    if response.status_code == 200:
        file = open('output.txt', 'w')
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all('div')
        for div in divs:
            text = div.text
            file.write(text)
            file.write("\n")

        file.close()

        print("Text extracted and saved to 'output.txt'")
    else:
        print("Failed to retrieve web page. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error: ", e)
