from bs4 import BeautifulSoup
import urllib3
import csv

#need a PoolManager() instance to make requests
http = urllib3.PoolManager()

#url we want to scrape
pageURL = "https://rivoters.com/by_ZIP_Code/02831.html"

#returns the document as a nested data structure
def getSoup():
    page = http.request('GET', pageURL)
    soup = BeautifulSoup(page.data, "html.parser")
    return soup

#finds all of the names
def getNames(soup):
    #finds all intances of 'a' which means we can find all classes because they are written <a class ...>
    people = soup.findAll("a")

    #remove the first two instances of 'a' classes, we do not need them
    people.pop(0)
    people.pop(0)

    #writes to the .csv file namesForTests
    with open ("/Users/a/PycharmProjects/Thing/SendEm/namesForTests.csv", 'a+') as f:
        #write = a writer object of namesForTests.csv, split by commas because .csv file, minimizes what is quoted
        write = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #goes through all names in people
        for i in range(len(people)):

            #peopleList is 2 strings (the first and last names) created by separating them by commas
            peopleList = str(people[i].text).split(',')

            #the last name is set to the name in peopleList at index 0
            last = peopleList[0].lower()

            #currently the string at peopleList[1] is written as Patrick R (the middle initial)
            #we just want the first name so we split() which splits the string into a list of two strings
            #and then we are assigning first to the first string in that list, which is the first name
            first = peopleList[1].split()[0].lower()

            #the name of the person is written to the .csv as the first name, last name
            name = [first, last]
            write.writerow(name)


#getSoup() is the parameter used for getNames(soup) because we need the html nested data structure to analyze
getNames(getSoup())