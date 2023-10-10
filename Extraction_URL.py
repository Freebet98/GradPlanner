import requests
from bs4 import BeautifulSoup

#url of list of classes
url = "https://cbs.umn.edu/academics/majors-and-minors"

try:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
      
        file = open("output.txt", "w")
        for link in soup.find_all("a"):
            data = link.get("href") #This does not get a str, and I don't know why not since when it extracts just text from the website it gets info
            file.write(data)
            file.write("\n")

        file.close()

        print("URLs extracted and saved to 'output.txt'")
    else:
        print("Failed to retrieve web page. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error: ", e)
