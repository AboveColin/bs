#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import init as config

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('/usr/bin/chromedriver',
                          options=chrome_options)

driver.delete_all_cookies()
driver.get(config.URL1)

search_box = driver.find_element_by_name(config.E1)
search_box.send_keys(config.args.a)
python_button = driver.find_element_by_name(config.E2)
python_button.click()

Cookie = driver.get_cookie(config.Cn2)['value']

driver.get(config.URL2)

T_count = int(driver.find_element_by_id(config.E3).text.replace(config.T2, '').replace(config.T3, ''))

total_pages = T_count // 10
total_pages_rest = T_count % 10


def next_page(n, max):
    if max <= 8:
        print(config.T1)
        exit()
    if max > 8:
        print(get_T_info(n))
        if n == 2:
            P_button = driver.find_element_by_id(config.E5_1)
            C_page = driver.find_element_by_id(config.E6_1).text
        elif n == 3:
            P_button = driver.find_element_by_id(config.E5_2)
            C_page = driver.find_element_by_id(config.E6_2).text
        elif n == 4:
            P_button = driver.find_element_by_id(config.E5_3)
            C_page = driver.find_element_by_id(config.E6_3).text
        elif n == 5:
            P_button = driver.find_element_by_id(config.E5_4)
            C_page = driver.find_element_by_id(config.E6_4).text
        elif n >= 6 and n <= max - 2:
            P_button = driver.find_element_by_id(config.E5_5)
            C_page = driver.find_element_by_id(config.E6_5).text
        elif n == max - 1:
            P_button = driver.find_element_by_id(config.E5_6)
            C_page = driver.find_element_by_id(config.E6_6).text
        elif n == max:
            P_button = driver.find_element_by_id(config.E5_7)
            C_page = driver.find_element_by_id(config.E6_7).text
        elif n == max + 1:
            P_button = driver.find_element_by_id(config.E5_8)
            C_page = driver.find_element_by_id(config.E6_8).text
        if n != max + 2:
            P_button.click()
        else:
            C_page = driver.find_element_by_id(config.E6_1).text

        return C_page
    else:
        return ''


def get_T_info(x):
    if x == total_pages + 1:
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


for x in range(2, total_pages + 2):
    print('=====================')
    print('==========' + str(next_page(x, total_pages)) + '==========')
    print()
