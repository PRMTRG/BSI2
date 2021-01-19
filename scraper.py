"""
Author:
Igor Motowidło (gottomy2)
"""

import requests
from bs4 import BeautifulSoup
import threading

URL = "https://techreport.com/"
document = requests.get(URL)
soup = BeautifulSoup(document.content, 'html.parser')
threads = []


def scraper(req):
    """
    Scrapper function for single thread
    Arguments:
    req -- requested html fragment to search
    """
    link = req.find('a')['href']
    value = req.find('a').get_text()
    print("Title: " + value + " | Link: " + link)


def main():
    """
    Count over all found elements until elements == 10
    appends && starts new thread for each element calls scrapper function
    """
    h4 = soup.find_all('h4', {'post-title'})
    count = 0
    for result in h4:
        if count == 10:
            break
        count += 1
        t = threading.Thread(target=scraper, args=(result,))
        threads.append(t)
        t.start()


if __name__ == "__main__":
    main()