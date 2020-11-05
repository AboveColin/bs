#!/usr/bin/python
# -*- coding: utf-8 -*-
import configparser as ConfigParser
import io
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--a', required=True)
args = parser.parse_args()

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read('config/config.ini')

CDP = config.get('ChromeDriver', 'path')

URL1 = config.get('URL', 'URL1')
URL2 = config.get('URL', 'URL2')

E1 = config.get('Elements', 'E1')
E2 = config.get('Elements', 'E2')
E3 = config.get('Elements', 'E3')

E4_1 = config.get('Elements', 'E4_1')
E4_2 = config.get('Elements', 'E4_2')
E4_3 = config.get('Elements', 'E4_3')

E5 = config.get('Elements', 'E5')

T1 = config.get('Text', 'T1')
T2 = config.get('Text', 'T2')
T3 = config.get('Text', 'T3')
