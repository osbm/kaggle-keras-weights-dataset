from bs4 import BeautifulSoup
import requests

from pprint import pprint    
import re
import os
import sys


url = "https://github.com/fchollet/deep-learning-models/releases"


def get_filenames(url=url):
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')


    # find all realeases
    releases = soup.find_all('div', class_='d-flex flex-column flex-md-row my-5 flex-justify-center')

    files = []
    # find all filenames in each release
    for release in releases:
        release_name = release.find('span', class_='ml-1 wb-break-all')
        release_name = release_name.text.strip()
        
        filename = release.find_all('li', class_="Box-row d-flex flex-column flex-md-row")
        for i in filename:
            i = i.find('a')
            i = i.text.strip()
            if "Source" in i:
                continue
            files.append(release_name + "/" + i)
    return files

files = get_filenames(url)
pprint(files)