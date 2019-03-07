from selenium import webdriver
import time
import random

browser = webdriver.Chrome("/Users/a/Downloads/chromedriver")
browser.get("http://www.protonmail.com")
time.sleep(1.5)

browser.find_element_by_css_selector('.btn.btn-ghost.btn-short').click()


time.sleep(2.5)
user = browser.find_element_by_id('username')
user.send_keys('ryanbourque@protonmail.com')
time.sleep(.5)
browser.find_element_by_id('password').send_keys('Ryan2222')
time.sleep(.5)
browser.find_element_by_id('login_btn').click()

time.sleep(5.5)

browser.find_element_by_xpath('//div/div/section/button').click()

time.sleep(3)

browser.find_element_by_name('autocomplete').send_keys('dwong19@lasalle-academy.org')
time.sleep(1.5)

x = 'Hey Dan' + str(random.randint(0, 1000))

browser.find_element_by_css_selector('input.subject').send_keys(x)

time.sleep(2.5)

#browser.find_element_by_xpath('//#docuhtml/body/div').click()
#time.sleep(2)

#elements = browser.find_element_by_class_name('angular-squire-iframe')
#browser.find_element_by_xpath('//div[@class="protonmail_signature_block-user protonmail_signature_block-empty"]')

#browser.execute_script("arguments[0].innerHTML='Hey Ryan... It works 😉'", browser.find_element_by_xpath('//div[@class="protonmail_signature_block-user protonmail_signature_block-empty"]'))

#browser.find_element_by_xpath('//html/body/div').send_keys('Hey Ryan... It works 😉')

#time.sleep(2)

browser.find_element_by_css_selector('button.composer-btn-send').click()


while True:
    time.sleep(10)

    browser.find_element_by_xpath('//div/div/section/button').click()

    time.sleep(3)

    browser.find_element_by_name('autocomplete').send_keys('dwong19@lasalle-academy.org')
    time.sleep(1.5)

    x = 'Hey Dan' + str(random.randint(0, 1000))
    
    browser.find_element_by_css_selector('input.subject').send_keys(x)

    time.sleep(1.5)

    #browser.find_element_by_class_name('protonmail_signature_block-proton').send_keys('Hey Ryan... It works 😉')

    #time.sleep(2)

    browser.find_element_by_css_selector('button.composer-btn-send').click()