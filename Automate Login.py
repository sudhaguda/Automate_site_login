from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from getpass import getpass

def printUse():
    print("Usage: python automateLogin.py -[fb/gmail]")
    print("Eg: python automateLogin.py -fb")
    print("Eg: python automateLogin.py -gmail")
    print(len(sys.argv))


email = input("Enter Email: ")
psd = getpass("Enter Password: ")
login_website =  'gmail'
if login_website=='gmail':
    try:
        driver_path = "Chrom_driver_path"
        driver = webdriver.Chrome(driver_path)
        driver.get("https://mail.google.com")
        driver.find_element_by_id('identifierId').send_keys(email)
        driver.find_element_by_id('identifierNext').click()
        sleep(5)
        driver.find_element_by_name('password').send_keys(psd)
        driver.find_element_by_id('passwordNext').click()
    except:
        print("Cannot login to your gmail account")
elif login_website == 'facebook':
    try:
        driver_path = "Chrom_driver_path"
        driver = webdriver.Chrome(driver_path)
        driver.get("https://facebook.com")
        driver.find_element_by_id('email').send_keys(email)
        driver.find_element_by_id('pass').send_keys(psd)
        driver.find_element_by_id('loginbutton').click()
    except:
        print("Cannot login to facebook account")