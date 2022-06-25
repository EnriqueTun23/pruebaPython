# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:42:09 2022

@author: quiqu
"""

import requests
import time
import hashlib
import pandas as pd
import os

from sqlalchemy import create_engine

URL= 'https://restcountries.com/v2/all'

data = requests.get(URL)


data = data.json()


df = pd.DataFrame()
    
df['Región'] = None
df['City Name'] = None
df['Language'] = None
df['Time'] = None


def conver_hash(data_hash):
    hash_data = hashlib.sha1(data_hash.encode("utf-8"))
    return hash_data.hexdigest().upper()


    
def parse_data(data):
    
    hash_conver = conver_hash(data['languages'][0]['name'])
    
    parse_data = {}
    parse_data['Región'] = data['region']
    parse_data['City Name'] = data['name']
    parse_data['Language'] = hash_conver
    
    return parse_data


def save_sql(dataFrame):
    
    if os.path.isfile('sqlite_country.db'):
        os.remove('sqlite_country.db')

    engine = create_engine('sqlite:///sqlite_country.db', echo=True)
    sqlite_connection = engine.connect()
    sqlite_table = "country"
    dataFrame.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
    
    sqlite_connection.close()

def save_json(dataFrame):
    if os.path.isfile('sqlite_country.json'):
        os.remove('sqlite_country.json')
    
    dataFrame.to_json(r'sqlite_country.json', orient='records')
    
    

if __name__ == '__main__':
    start = time.time()
    for i in data:
        
        parse = parse_data(i)
        end = time.time()
        parse['Time'] = "{} ms".format((end - start))
        df = df.append(parse, ignore_index=True)
    
    
    save_sql(df)
    save_json(df)



    
    