import base64
import os
import csv
import requests
import json
import time
from web3 import Web3
from pyevmasm import instruction_tables, disassemble_hex, disassemble_all, assemble_hex
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_bytecode(address):
    flag = 0
    while flag == 0:
        try:
            driver = webdriver.Chrome()
            BASE_URL = "https://etherscan.io/bytecode-decompiler?a="
            url = BASE_URL + address
            page = requests.get(url)
            driver.get(url)
            verify = driver.find_element_by_id("ContentPlaceHolder1_txtByteCode").text
            print(verify)
            driver.close()
            flag = 1
        except Exception as e:
            print(e)
    return verify

if __name__=='__main__':
    csv_address = '24.csv'
    with open(csv_address, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if '0x' in row[0]:
                print(row[0])
                bytecode = get_bytecode(row[0])
                with open('files/' + row[0], 'a') as newfile:
                    newfile.write(bytecode)