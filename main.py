#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import init as config

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(config.CDP,
                          options=chrome_options)

driver.delete_all_cookies()
driver.get(config.URL1)

search_box = driver.find_element_by_name(config.E1)
search_box.send_keys(config.args.a)
python_button = driver.find_element_by_name(config.E2)
python_button.click()

driver.get(config.URL2)

T_count = int(driver.find_element_by_id(config.E3).text.replace(config.T2, '').replace(config.T3, ''))

total_pages = T_count // 10
total_pages_rest = T_count % 10

def next_page(n, max):
    print(get_T_info(n))
    P_button = driver.find_element_by_id(config.E5)
    P_button.click()
    return n-1


def get_T_info(x):
    if x == total_pages + 2:
        for x in range(1, total_pages_rest + 1):
            x = str(x).zfill(2)
            A_Name = driver.find_element_by_id(config.E4_1 + x + config.E4_2).text
            T_name = driver.find_element_by_id(config.E4_1 + x + config.E4_3).text

            print(A_Name + ' - ' + T_name)
    else:

        for x in range(1, 11):
            if x < 10:
                x = str(x).zfill(2)
            A_Name = driver.find_element_by_id(config.E4_1 + str(x) + config.E4_2).text
            T_name = driver.find_element_by_id(config.E4_1 + str(x) + config.E4_3).text

            print(A_Name + ' - ' + T_name)


for x in range(2, total_pages + 3):
    print('=====================')
    print('==========' + str(next_page(x, total_pages)) + '==========')
    print()

driver.quit()