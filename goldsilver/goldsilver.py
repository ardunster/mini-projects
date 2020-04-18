#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:43:45 2020

@author: adunster
"""

'''
    
    - Can I fetch gold/silver prices and set up an alert when certain conditions are met?
    


london fix price (what my chart uses) is set pm at 15:00 GMT. However,
site I use to update doesn't list this number until next day. 

gold: 0.975 < > 1.225
'''

'''
Email test code:

but if you’re using a local debugging server, just make sure to use 
localhost as your SMTP server and use port 1025 rather than port 465 or
587. Besides this, you won’t need to use login() or encrypt the 
communication using SSL/TLS.


import smtplib

port = 1025
smtp_server = 'localhost'

server = smtplib.SMTP(smtp_server,port)

sender_email = 'bogus@bogus.com'

#sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

# Send email here

server.sendmail(sender_email, receiver_email, message)

'''


import openpyxl as xl
from os import path
import datetime
from bs4 import BeautifulSoup as bs
import requests


class TooFewLines(Exception):
    '''
    Raised by too few lines in xlsx files
    '''
    pass

def load_xlsx():
    '''
    Loads existing data
    '''
    global prices_gold
    global gold_wb
    global gold_ws 
    global gold_mr
    
    global prices_silver
    global silver_wb
    global silver_ws
    global silver_mr
    
    prices_gold = 'goldprices.xlsx'
    gold_wb = xl.load_workbook(prices_gold)
    gold_ws = gold_wb.worksheets[0]
    gold_mr = gold_ws.max_row
    
    prices_silver = 'silverprices.xlsx'
    silver_wb = xl.load_workbook(prices_silver)
    silver_ws = silver_wb.worksheets[0]
    silver_mr = silver_ws.max_row
    
    if gold_mr < 202:
        raise TooFewLines('Too few lines in goldprices.xlsx to compute 200dma, check data.')
    elif silver_mr < 202:
        raise TooFewLines('Too few lines in silverprices.xlsx to compute 200dma, check data.')




def get_current():
    '''
    Retrieves current information from website, returns as a list of tuples:
    (Datetime, Gold AM, Gold PM, Silver noon)
    '''
    
    url = 'https://goldsilver.com/price-charts/historical-london-fix/'
    
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    content = []

    for item in soup.find_all('td'):
        item_text = item.get_text()
        if not item_text == '':
            content.append(item_text)
    
    content_arr = []
    
    for i in range(0,(len(content) - 3),4):
        w_date = datetime.datetime.strptime(content[i], '%Y-%m-%d')
        w_date = w_date.date()
        content_arr.append((w_date,content[i+1].strip('$'),content[i+2].strip('$'),content[i+3].strip('$')))
        
    return content_arr




if __name__ == '__main__':
    if not path.exists('goldprices.xlsx') or not path.exists('silverprices.xlsx'):
        print('Error, missing data. Please ensure goldprices.xlsx and silverprices.xlsx have been generated appropriately.')
    else:
        print('run code here')
        current = get_current()
        load_xlsx()

'''
Next steps:
- fetch most recent row in each
- find and index in current (data error if na? edge case beginning of year?)
- append data after that into xlsx
- check for relative ratios in alert zones
- produce an alert of some kind. email or?
'''


