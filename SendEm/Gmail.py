from selenium import webdriver
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv


#UNITED STATES 2797

class Gmail:

    browser = None

    nameLine = 0

    password = 'Daniel2222'

    def initalizeBrowser(Gmail):
        Gmail.browser = webdriver.Chrome("/Users/a/Downloads/chromedriver")
        Gmail.browser.get("http://www.gmail.com")
        time.sleep(1.5)

    def createEmail(Gmail):
        browser = Gmail.browser
        password = Gmail.password
        first = []
        last = []
        browser.find_elements_by_css_selector('.RveJvd.snByac')[1].click()
        with open("/Users/a/PycharmProjects/Thing/SendEm/namesForTests.csv", 'r+') as f:
            read = csv.reader(f, delimiter=',', quotechar='"')
            for row in read:
                first.append(row[0])
                last.append(row[1])
        time.sleep(.5)
        browser.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys(first[Gmail.nameLine])
        time.sleep(.5)
        browser.find_elements_by_css_selector('.whsOnd.zHQkBf')[1].send_keys(last[Gmail.nameLine])
        time.sleep(.5)
        address = first[Gmail.nameLine] + last[Gmail.nameLine] + str(random.randint(100000, 1000000))
        browser.find_elements_by_css_selector('.whsOnd.zHQkBf')[2].send_keys(address)
        browser.find_elements_by_css_selector('.whsOnd.zHQkBf')[3].send_keys(password)
        browser.find_elements_by_css_selector('.whsOnd.zHQkBf')[4].send_keys(password)
        browser.find_element_by_css_selector('.RveJvd.snByac').click()
        Gmail.nameLine+=1

    def signIn(Gmail):
        browser = Gmail.browser
        browser.find_element_by_id('identifierId').send_keys('danwong2019@gmail.com')
        time.sleep(.5)
        browser.find_element_by_xpath('//div/div/content/span').click()
        time.sleep(3)
        browser.find_element_by_xpath('//div/div/div/div/input').send_keys('Daniel2222')
        time.sleep(.5)
        browser.find_element_by_xpath('//div/div/content/span').click()
        time.sleep(4.5)

    def send(Gmail):
        browser = Gmail.browser
        browser.find_element_by_xpath('//div/div/div/div/div/div/div/div/div/div/div/div/div/div').click()
        time.sleep(2)
        browser.find_element_by_class_name('vO').send_keys('rbourque19@lasalle-academy.org')
        time.sleep(1)
        x = 'Hey Ryan ' + str(random.randint(0, 1000))
        browser.find_element_by_class_name('aoT').send_keys(x)
        time.sleep(1.5)
        ActionChains(browser).key_down(Keys.COMMAND).key_down(Keys.ENTER).key_up(Keys.COMMAND).key_up(Keys.ENTER).perform()

    def closeBrowser(Gmail):
        browser = Gmail.browser
        browser.quit()

Gmail.initalizeBrowser(Gmail)

Gmail.createEmail(Gmail)

#Gmail.signIn(Gmail)

#while True:
#    Gmail.send(Gmail)
#    time.sleep(1.5)