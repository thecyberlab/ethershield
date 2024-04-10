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

def produce_ngram(org_str, n):
    converted_str = ''
    i = 0
    while i + n <= len(org_str):
        converted_str = converted_str + str(base64.b64encode(org_str[i:(i + n)].encode('utf-8'))) + ' '
        i = i + 1
    z = 0
    while z <= n - 1:
        j = 0
        temp_str = org_str[i + z + 1:len(org_str)]
        while j <= i + z + n - len(org_str):
            temp_str = temp_str + ' '
            j = j + 1
        converted_str = converted_str + str(base64.b64encode(temp_str.encode('utf-8'))) + ' '
        z = z + 1
    converted_str = converted_str[:-1]
    print (converted_str)
    return converted_str

def produce_ngram_all(org_str, n):
    converted_str = ''
    i = 0
    org_list = org_str.split(' ')
    while i + n <= len(org_list):
        added_str = ''
        for single_str in org_list[i:(i + n)]:
            added_str = added_str + single_str + ' '
        added_str = added_str[:-1]
        converted_str = converted_str + str(base64.b64encode(added_str.encode('utf-8'))) + ' '
        print (converted_str)
        i = i + 1
    z = 0
    while z <= n - 1:
        j = 0
        temp_list = org_list[i + z + 1:len(org_list)]
        temp_str = ''
        for single_str in temp_list:
            temp_str = temp_str + single_str + ' '
        temp_str = temp_str[:-1]
        while j <= i + z + n - len(org_list):
            temp_str = temp_str + ' '
            j = j + 1
        converted_str = converted_str + str(base64.b64encode(temp_str.encode('utf-8'))) + ' '
        z = z + 1
    converted_str = converted_str[:-1]
    return converted_str

def get_bytecode(address):
    with open('files/' + address, 'r') as tempfile:
        bytecode = tempfile.readline()
    return bytecode


if __name__=='__main__':
    n_gram = 4
    top = 50
    document_list_phishing = []
    document_list_ponzi = []
    document_list_coinstolen = []
    document_list_nonmalicious = []
    document_list_honeypot = []
    document_list_high_risk = []
    op_all_list_phishing = []
    op_all_list_ponzi = []
    op_all_list_coinstolen = []
    op_all_list_nonmalicious = []
    op_all_list_honeypot = []
    op_all_list_high_risk = []
    address_phishing = []
    address_ponzi = []
    address_coinstolen = []
    address_nonmalicious = []
    address_honeypot = []
    address_high_risk = []
    csv_address = '24.csv'
    with open(csv_address, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if '0x' in row[0]:
                print(row[0])
                bytecode = get_bytecode(row[0])
                if bytecode:
                    bytecode = bytecode[2:]
                    all_op = disassemble_hex(bytecode)
                    opcode_list = all_op.split('\n')
                    text_str = ''
                    for every_opcode in opcode_list:
                        text_str = text_str + ' ' + every_opcode
                    ngram_str = produce_ngram(bytecode, n_gram)
                    all_op_ngram = produce_ngram_all(text_str, n_gram)
                    if row[1] == '1':
                        document_list_phishing.append(ngram_str)
                        op_all_list_phishing.append(all_op_ngram)
                        address_phishing.append(row[0])
                    if row[1] == '0':
                        document_list_ponzi.append(ngram_str)
                        op_all_list_ponzi.append(all_op_ngram)
                        address_ponzi.append(row[0])
    
    with open('1.txt', 'a') as strfile:
        for word in document_list_phishing:
            strfile.write(word)
        for word in op_all_list_phishing:
            strfile.write(word)
    with open('0.txt', 'a') as strfile:
        for word in document_list_ponzi:
            strfile.write(word)
        for word in op_all_list_ponzi:
            strfile.write(word)

    # sort for phishing
    vectorizer = TfidfVectorizer()
    phishing_dict_list = []
    print(document_list_phishing)
    X_phishing = vectorizer.fit_transform(document_list_phishing)
    names = vectorizer.get_feature_names_out()
    for single_record in X_phishing.toarray():
        temp = {}
        i = 0
        for name in names:
            temp[name] = single_record[i]
            i = i + 1
        phishing_dict_list.append(temp) 
    data = {'word': vectorizer.get_feature_names_out(),
            'tfidf': X_phishing.toarray().sum(axis=0).tolist()}
    df = pd.DataFrame(data)
    df = df.sort_values(by="tfidf", ascending=False)
    ranking_phishing = np.array(df).tolist()


    # sort for ponzi
    vectorizer = TfidfVectorizer()
    X_ponzi = vectorizer.fit_transform(document_list_ponzi)
    names = vectorizer.get_feature_names_out()
    ponzi_dict_list = []
    for single_record in X_ponzi.toarray():
        temp = {}
        i = 0
        for name in names:
            temp[name] = single_record[i]
            i = i + 1
        ponzi_dict_list.append(temp) 
    data = {'word': vectorizer.get_feature_names_out(),
            'tfidf': X_ponzi.toarray().sum(axis=0).tolist()}
    df = pd.DataFrame(data)
    df = df.sort_values(by="tfidf", ascending=False)
    ranking_ponzi = np.array(df).tolist()


    topwords = []
    i = 0
    for word in ranking_phishing:
        if i == 50:
            break
        if word[0] not in topwords:
            topwords.append(word[0])
        i = i + 1
    
    i = 0
    for word in ranking_ponzi:
        if i == 50:
            break
        if word[0] not in topwords:
            topwords.append(word[0])
        i = i + 1
    
    temp_write_list = ['Address']
    column_for_new_feature = ''
    str_for_new_feature = ''
    dic_str_for_new_feature = ''
    for word in topwords:
        temp_write_list.append(word + '(bytecode)')
    with open("ngram_24.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(temp_write_list)
    for word in topwords:
        column_for_new_feature = column_for_new_feature + word + ' '
        str_for_new_feature = str_for_new_feature + '\'' + word + '\','
        dic_str_for_new_feature = dic_str_for_new_feature + '\'' + word + '\':float,'
    with open('temp_strs_24.txt', 'a') as strfile:
        strfile.write(column_for_new_feature)
        strfile.write(str_for_new_feature)
        strfile.write(dic_str_for_new_feature)

    i = 0
    for single in phishing_dict_list:
        temp_write_list =[]
        temp_write_list.append(address_phishing[i])
        for word in topwords:
            if word in single:
                temp_write_list.append(single[word])
            else:
                temp_write_list.append(0)
        with open("ngram_24.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(temp_write_list)
        i = i + 1

    i = 0
    for single in ponzi_dict_list:
        temp_write_list =[]
        temp_write_list.append(address_ponzi[i])
        for word in topwords:
            if word in single:
                temp_write_list.append(single[word])
            else:
                temp_write_list.append(0)
        with open("ngram_24.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(temp_write_list)
        i = i + 1

    # sort for phishing
    vectorizer = TfidfVectorizer()
    phishing_dict_list = []
    X_phishing = vectorizer.fit_transform(op_all_list_phishing)
    names = vectorizer.get_feature_names_out()
    for single_record in X_phishing.toarray():
        temp = {}
        i = 0
        for name in names:
            temp[name] = single_record[i]
            i = i + 1
        phishing_dict_list.append(temp) 
    data = {'word': vectorizer.get_feature_names_out(),
            'tfidf': X_phishing.toarray().sum(axis=0).tolist()}
    df = pd.DataFrame(data)
    df = df.sort_values(by="tfidf", ascending=False)
    ranking_phishing = np.array(df).tolist()


    # sort for ponzi
    vectorizer = TfidfVectorizer()
    X_ponzi = vectorizer.fit_transform(op_all_list_ponzi)
    names = vectorizer.get_feature_names_out()
    ponzi_dict_list = []
    for single_record in X_ponzi.toarray():
        temp = {}
        i = 0
        for name in names:
            temp[name] = single_record[i]
            i = i + 1
        ponzi_dict_list.append(temp) 
    data = {'word': vectorizer.get_feature_names_out(),
            'tfidf': X_ponzi.toarray().sum(axis=0).tolist()}
    df = pd.DataFrame(data)
    df = df.sort_values(by="tfidf", ascending=False)
    ranking_ponzi = np.array(df).tolist()

    topwords = []
    i = 0
    for word in ranking_phishing:
        if i == 50:
            break
        if word[0] not in topwords:
            topwords.append(word[0])
        i = i + 1
    
    i = 0
    for word in ranking_ponzi:
        if i == 50:
            break
        if word[0] not in topwords:
            topwords.append(word[0])
        i = i + 1

    temp_write_list = ['Address']
    column_for_new_feature = ''
    str_for_new_feature = ''
    dic_str_for_new_feature = ''
    for word in topwords:
        temp_write_list.append(word + '(op)')
    with open("ngram_op_24.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(temp_write_list)
    for word in topwords:
        column_for_new_feature = column_for_new_feature + word + ' '
        str_for_new_feature = str_for_new_feature + '\'' + word + '\','
        dic_str_for_new_feature = dic_str_for_new_feature + '\'' + word + '\':float,'
    with open('temp_strs.txt', 'a') as strfile:
        strfile.write(column_for_new_feature)
        strfile.write(str_for_new_feature)
        strfile.write(dic_str_for_new_feature)
    i = 0
    for single in phishing_dict_list:
        temp_write_list =[]
        temp_write_list.append(address_phishing[i])
        for word in topwords:
            if word in single:
                temp_write_list.append(single[word])
            else:
                temp_write_list.append(0)
        with open("ngram_op_24.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(temp_write_list)
        i = i + 1

    i = 0
    for single in ponzi_dict_list:
        temp_write_list =[]
        temp_write_list.append(address_ponzi[i])
        for word in topwords:
            if word in single:
                temp_write_list.append(single[word])
            else:
                temp_write_list.append(0)
        with open("ngram_op_24.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(temp_write_list)
        i = i + 1
    