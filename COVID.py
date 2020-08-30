import requests
from bs4 import BeautifulSoup

def covid_stats(url: str = "https://www.worldometers.info/coronavirus") -> dict:
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    keys = soup.findAll("h1")
    values = soup.findAll("div", { "class" : "maincounter-number" })
    keys += soup.findAll("span", {"class" : "panel-title"})
    values += soup.findAll("div", {"class" : "number-table-min"})
    return {key.text.strip(): value.text.strip() for key, value in zip(keys,values)}

if __name__ == '__main__':
    print("\033[1m" + "Covid Stats Of Word" + "\033[0m\n")
    for key , value in covid_stats().items():
        print(f"{key}\n{value}\n")
    
    