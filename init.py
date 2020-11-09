#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser as ConfigParser
import io
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--composer')
parser.add_argument('-t', '--title') 
parser.add_argument('-a', '--author')
args = parser.parse_args()

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read('config/config.ini')

CDP = config.get('ChromeDriver', 'path')

URL1 = config.get('URL', 'URL1')
URL2 = config.get('URL', 'URL2')

E1_1 = config.get('Elements', 'E1_1')
E1_2 = config.get('Elements', 'E1_2')
E1_3 = config.get('Elements', 'E1_3')

E2 = config.get('Elements', 'E2')
E3 = config.get('Elements', 'E3')

E4_1 = config.get('Elements', 'E4_1')
E4_2 = config.get('Elements', 'E4_2')
E4_3 = config.get('Elements', 'E4_3')

E5 = config.get('Elements', 'E5')

if args.composer:
    mode = E1_3
    name = args.composer
elif args.title:
    mode = E1_1
    name = args.title
elif args.author:
    mode = E1_2
    name = args.author

def setup_chromedriver():
    global chrome_options
    global driver
    """Starts chromedriver with the correct settings.
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(CDP,
                            options=chrome_options)

    driver.delete_all_cookies()

def setup_page():
    """inserts name and submits it to create a cookie/sessionID
    """
    driver.get(URL1)
    driver.find_element_by_id(mode).send_keys(name)
    driver.find_element_by_name(E2).click()

def info_page():
    global T_count
    global total_pages
    global total_pages_rest
    global last_page
    driver.get(URL2)
    T_count = int(re.sub("[^0-9]", "", driver.find_element_by_id(E3).text))
    total_pages = T_count // 10
    total_pages_rest = T_count % 10
    
    if total_pages_rest != 0:
        last_page = total_pages+1
    else:
        last_page = total_pages

setup_chromedriver()
setup_page()
info_page()
