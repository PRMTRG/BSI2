"""
Author:
Tymoteusz Mirski
Igor Motowidło
"""


import os
import requests as r
from bs4 import BeautifulSoup
import pdfkit
import time
import multiprocessing 
import sys
import subprocess
import argparse


def get_article_links_from_google(query, count):
    """
    Get article links from Google Search articles tab.

    Parameters
    ----------
    query : string
        Search query.
    count : int
        Number of links to get.

    Returns
    -------
    list
        URLs of the articles.

    """
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


def save_webpage_as_pdf(url, filename):
    """
    Render and save website to a pdf file.

    Parameters
    ----------
    url : string
        Address of the website.
    filename : string
        Name of the output pdf file.

    Returns
    -------
    None.

    """
    try:
        pdfkit.from_url(url, filename, {"quiet":""})
    except:
        pass


def main():
    """
    Gets links of articles by usage of get_article_links_from_google function
    then enumerates through the links array and calls save_webpage_as_pdf in single thread one for each link.
    """
    query = "nvidia"
    count = 5
    output_dir = "scrape_output"    
    ap = argparse.ArgumentParser()
    ap.add_argument("-q", "--query", required=False,
                    help="Google search query",
                    default=query, metavar="query")                
    ap.add_argument("-c", "--count", required=False, type=int,
                    help="number of articles to get", 
                    default=count)  
    ap.add_argument("-d", "--dir", required=False,
                    help="Output directory",
                    default=output_dir, metavar="directory")               
    args = vars(ap.parse_args())
    query = args["query"]
    count = args["count"]
    output_dir = args["dir"]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    links = get_article_links_from_google(query, count)
    processes = []
    for i, link in enumerate(links):
        process = multiprocessing.Process(target=save_webpage_as_pdf, args=(link, f"{output_dir}/{i+1}.pdf"))
        process.start()
        processes.append(process)
    time.sleep(10)
    # Making sure that process of wkhtmltopdf.exe has been stopped
    subprocess.Popen(["powershell.exe", "./kill.ps1"], stdout=subprocess.DEVNULL)
    for process in processes:
        process.terminate()


if __name__ == "__main__":
    main()