from bs4 import BeautifulSoup
import urllib3
import csv
import time

http = urllib3.PoolManager()

pageURL = "https://rivoters.com/by_ZIP_Code/02813.html"

def getSoup():
    page = http.request('GET', pageURL)
    soup = BeautifulSoup(page.data, "html.parser")
    return soup

def getNames(soup):
    people = soup.findAll("a")
    people.pop(0)
    people.pop(0)
    with open ("/Users/a/Documents/names.csv", 'a+') as f:
        write = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(people)):
            peopleList = str(people[i].text).split(',')
            last = peopleList[0].lower()
            first = peopleList[1].split()[0].lower()
            name = [first, last]
            write.writerow(name)


getNames(getSoup())