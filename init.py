#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import io
import argparse
import re
from datetime import datetime

now = datetime.now()
dt = now.strftime("%d%m%Y-%H%M%S")

#Initialize arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--composer', type=str)
parser.add_argument('-t', '--title', type=str) 
parser.add_argument('-a', '--author', type=str)
parser.add_argument('-l', '--list', action='store_true', default=False)
parser.add_argument('-p', '--proxy', type=str, default="")
parser.add_argument('-whl', '--without_headless', action='store_true', default=False)
parser.add_argument('-s', '--save', action='store_true', default=False)
args = parser.parse_args()


#Initialize config.json
with open('config/config.json') as f:
  config = json.load(f)
URL_Array = config["URL"]
Elements_Array = config["Elements"]


#Initialize variables from config
CDP = config["chromedriver_path"]

URL1 = URL_Array[0]["URL1"]
URL2 = URL_Array[0]["URL2"]

E1_1 = Elements_Array[0]["E1_1"]
E1_2 = Elements_Array[0]["E1_2"]
E1_3 = Elements_Array[0]["E1_3"]

E2 = Elements_Array[1]["E2"]
E3 = Elements_Array[2]["E3"]

E4_1 = Elements_Array[3]["E4_1"]
E4_2 = Elements_Array[3]["E4_2"]
E4_3 = Elements_Array[3]["E4_3"]

E5 = Elements_Array[4]["E5"]

#Initialize variables from argument(s) given
if args.composer:
    mode = E1_3
    name = args.composer
elif args.title:
    mode = E1_1
    name = args.title
elif args.author:
    mode = E1_2
    name = args.author
else:
    exit()

if args.proxy:
    proxy = args.proxy
else:
    proxy = ""

if args.save:
    f = open("saves/"+dt+".txt", "w")


def setup_chromedriver():
    """Starts chromedriver with the correct settings.
    """
    global chrome_options
    global driver
    chrome_options = Options()
    if args.without_headless == False:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-gpu')
    if len(proxy) > 0:
        chrome_options.add_argument('--proxy-server=%s' % proxy)
    prefs={"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096 }
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(CDP,
                            options=chrome_options)

    driver.delete_all_cookies()

def setup_page():
    """inserts name and submits it to create a cookie/sessionID
    """
    driver.get(URL1)
    driver.find_element_by_id(mode).send_keys(name)
    driver.find_element_by_id(E2).click()

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
