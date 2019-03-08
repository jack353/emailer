from selenium import webdriver
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#UNITED STATES 2797

class Gmail:

    browser = None


    def initalizeBrowser(Gmail):
        Gmail.browser = webdriver.Chrome("/Users/a/Downloads/chromedriver")
        Gmail.browser.get("http://www.gmail.com")
        time.sleep(1.5)

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
        browser.find_element_by_class_name('vO').send_keys('pcosta19@lasalle-academy.org')
        time.sleep(1)
        x = 'Hey Dan' + str(random.randint(0, 1000))
        browser.find_element_by_class_name('aoT').send_keys(x)
        time.sleep(1.5)
        ActionChains(browser).key_down(Keys.COMMAND).key_down(Keys.ENTER).key_up(Keys.COMMAND).key_up(Keys.ENTER).perform()

    def closeBrowser(Gmail):
        browser = Gmail.browser
        browser.quit()

    # browser.find_element_by_xpath('//#docuhtml/body/div').click()
    # time.sleep(2)

    # elements = browser.find_element_by_class_name('angular-squire-iframe')
    # browser.find_element_by_xpath('//div[@class="protonmail_signature_block-user protonmail_signature_block-empty"]')

    # browser.execute_script("arguments[0].innerHTML='Hey Ryan... It works 😉'", browser.find_element_by_xpath('//div[@class="protonmail_signature_block-user protonmail_signature_block-empty"]'))

    # browser.find_element_by_xpath('//html/body/div').send_keys('Hey Ryan... It works 😉')

    # time.sleep(2)


Gmail.initalizeBrowser(Gmail)

Gmail.signIn(Gmail)

while True:
    Gmail.send(Gmail)
    time.sleep(1.5)