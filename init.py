#!/usr/bin/python
# -*- coding: utf-8 -*-
import configparser as ConfigParser
import io
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--a')
args = parser.parse_args()

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read('config/config.ini')

URL1 = config.get('URL', 'URL1')
URL2 = config.get('URL', 'URL2')

E1 = config.get('Elements', 'E1')
E2 = config.get('Elements', 'E2')
E3 = config.get('Elements', 'E3')

E4_1 = config.get('Elements', 'E4_1')
E4_2 = config.get('Elements', 'E4_2')
E4_3 = config.get('Elements', 'E4_3')

E5_1 = config.get('Elements', 'E5_1')
E5_2 = config.get('Elements', 'E5_2')
E5_3 = config.get('Elements', 'E5_3')
E5_4 = config.get('Elements', 'E5_4')
E5_5 = config.get('Elements', 'E5_5')
E5_6 = config.get('Elements', 'E5_6')
E5_7 = config.get('Elements', 'E5_7')
E5_8 = config.get('Elements', 'E5_8')

E6_1 = config.get('Elements', 'E6_1')
E6_2 = config.get('Elements', 'E6_2')
E6_3 = config.get('Elements', 'E6_3')
E6_4 = config.get('Elements', 'E6_4')
E6_5 = config.get('Elements', 'E6_5')
E6_6 = config.get('Elements', 'E6_6')
E6_7 = config.get('Elements', 'E6_7')
E6_8 = config.get('Elements', 'E6_8')
E6_9 = config.get('Elements', 'E6_9')

Cn1 = config.get('Cookies', 'Cn1')
Cn2 = config.get('Cookies', 'Cn2')

T1 = config.get('Text', 'T1')
T2 = config.get('Text', 'T2')
T3 = config.get('Text', 'T3')
