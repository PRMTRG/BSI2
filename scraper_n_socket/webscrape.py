"""
Author:
Tymoteusz Mirski
"""


import os
import threading
import requests as r
from bs4 import BeautifulSoup
import pdfkit
import time
import multiprocessing 
import sys
import subprocess


def get_article_links_from_google(query, count):
    url = "http://google.com/search"
    position = 0
    max_requests = 3
    req_cnt = 0
    links = []
    while len(links) < count and req_cnt < max_requests:
        params = { "q": query, "tbm": "nws", "start": position }
        page = r.get(url, params=params).text
        soup = BeautifulSoup(page, "html.parser")
        for a in soup.find_all("a"):
            link = a.get("href")
            if not link.startswith("/url") or "google" in link:
                continue
            link = link[7:]
            link = link.split("&", 1)[0]
            if link not in links:
                links.append(link)
        req_cnt += 1
        position += 10
    return links[:count]


def save_webpage_as_pdf(link, filename):
    try:
        pdfkit.from_url(link, filename, {"quiet":""})
    except:
        pass


def main():
    query = "nvidia"
    output_dir = "scrape_output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    links = get_article_links_from_google(query, 10)
    processes = []
    for i, link in enumerate(links):
        process = multiprocessing.Process(target=save_webpage_as_pdf,
                                  args=(link, f"{output_dir}/{i+1}.pdf"))
        process.start()
        processes.append(process)
    time.sleep(5)
    p = subprocess.Popen(["powershell.exe",
        "./kill.ps1"],
        stdout=sys.stdout)
    for process in processes:
        process.terminate()


if __name__ == "__main__":
    main()
    
