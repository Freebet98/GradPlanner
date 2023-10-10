import requests
from bs4 import BeautifulSoup

#url of list of classes
url = "https://www.myu.umn.edu/psp/psprd/EMPLOYEE/CAMP/c/SA_LEARNER_SERVICES.CLASS_SEARCH.GBL"

try:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(text)

        print("Text extracted and saved to 'output.txt'")
    else:
        print("Failed to retrieve web page. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error: ", e)