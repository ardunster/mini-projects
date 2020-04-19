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
import re


class TooFewLines(Exception):
    '''
    Raised by too few lines in xlsx files
    '''
    pass

class MissingFiles(Exception):
    '''
    Raised if missing xlsx files
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
    
#    prices_gold = 'goldprices.xlsx'
    gold_wb = xl.load_workbook(prices_gold)
    gold_ws = gold_wb.worksheets[0]
    gold_mr = gold_ws.max_row
    
#    prices_silver = 'silverprices.xlsx'
    silver_wb = xl.load_workbook(prices_silver)
    silver_ws = silver_wb.worksheets[0]
    silver_mr = silver_ws.max_row
    
    if gold_mr < 202:
        raise TooFewLines('Too few lines in {} to compute 200dma, check data.'.format(prices_gold))
    elif silver_mr < 202:
        raise TooFewLines('Too few lines in {} to compute 200dma, check data.'.format(prices_silver))




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
    re_sub = re.compile('[^\d\.\-]')
    
    for i in range(0,(len(content) - 3),4):
        w_date = datetime.datetime.strptime(content[i], '%Y-%m-%d')
        w_date = w_date.date()
        content_arr.append((w_date,(re.sub(re_sub, '', content[i+1])),(re.sub(re_sub, '', content[i+2])),(re.sub(re_sub, '', content[i+3]))))

        
    return content_arr

def verify_mr(goldorsilver):
    '''
    Checks against a possible bug in openpyxl reporting too high of a max row.
    Input: string, either 'gold' or 'silver'
    Starts with reported last row and works backward to verify that the contents
    of the cell is not None
    '''
    if goldorsilver == 'gold':
        verify_mr = gold_mr
        verify_ws = gold_ws
    elif goldorsilver == 'silver':
        verify_mr = silver_mr
        verify_ws = silver_ws
    for row in range(verify_mr,0,-1):
        if not verify_ws.cell(row=row,column=1).value == None:
            last_row = row
            return last_row


def update():
    '''
    Finds indexes for last updated information in both files, adds data after 
    index, saves files
    '''
    def find_index():
        ''' Checks indexes to find next line to add'''
        w_date_gold = gold_ws.cell(row=gold_mr, column=1).value.date()
        w_date_silver = silver_ws.cell(row=silver_mr, column=1).value.date()
        ind_gold = ''
        ind_silver = ''
        while ind_gold == '' and ind_silver == '':
            for tup in range(len(current)):
                if current[tup][0] == w_date_gold:
                    ind_gold = (tup - 1)
                elif current[tup][0].timetuple().tm_mon == 1 and len(current) == 1:
                    ind_gold = tup
                if current[tup][0] == w_date_silver:
                    ind_silver = (tup - 1)
                elif current[tup][0].timetuple().tm_mon == 1 and len(current) == 1:
                    ind_silver = tup
        return ind_gold, ind_silver
            
    def add_row(goldorsilver,add_row,w_date,w_value):
        if goldorsilver == 'gold':
            add_ws = gold_ws
        elif goldorsilver == 'silver':
            add_ws = silver_ws
        add_ws.cell(row=add_row, column=1).value = w_date
        add_ws.cell(row=add_row, column=1).number_format = 'yy/mm/dd'
        add_ws.cell(row=add_row, column=2).value = float(w_value)
        add_ws.cell(row=add_row, column=2).number_format = '#,##0.00'
        add_ws.cell(row=add_row, column=3).value = '=(B{}-B{})'.format(add_row,add_row-1)
        add_ws.cell(row=add_row, column=3).number_format = '#,##0.00'
        add_ws.cell(row=add_row, column=4).value = '=AVERAGE(B{}:B{})'.format(add_row,add_row-200)
        add_ws.cell(row=add_row, column=4).number_format = '#,##0.00'
        add_ws.cell(row=add_row, column=5).value = '=(B{}/D{})'.format(add_row, add_row)
        add_ws.cell(row=add_row, column=5).number_format = '#,##0.00'

                
    gold_silver_index = (find_index())
    
    
    # Gold
    g_add_row = gold_mr + 1        
    for i in range(gold_silver_index[0],-1,-1):
        if not current[i][2] == '-':
            add_row('gold',g_add_row,current[i][0],current[i][2])
            g_add_row += 1
        elif current[i][2] == '-' and not current[i][1] == '-':
            add_row('gold',g_add_row,current[i][0],current[i][1])
            g_add_row += 1
        
    # Silver
    s_add_row = silver_mr + 1
    for i in range(gold_silver_index[1],-1,-1):
        if not current[i][3] == '-':
            add_row('silver',s_add_row,current[i][0],current[i][3])
            s_add_row += 1
            
    gold_wb.save(prices_gold)
    silver_wb.save(prices_silver)

def calc_dma():
    '''
    Retrieves and calculates the data for 200dma and relative gold and relative 
    silver values. This is also calculated in the xlsx file if loaded in a client,
    but openpyxl will not evaluate formulas so must be separately calculated in
    the script for alerts, etc.
    '''
    
    # Gold
    
    pass
    
    
#    return gold_200dma, gold_ratio, silver_200dma, silver_ratio



prices_gold = 'goldprices.xlsx'
prices_silver = 'silverprices.xlsx'

if not path.exists(prices_gold) or not path.exists(prices_silver):
    raise MissingFiles('Error, missing data. Please ensure goldprices.xlsx and silverprices.xlsx have been generated appropriately.')

if __name__ == '__main__':
    print('run code here')
#    current = get_current()
    # line with test data so I don't have to refresh website every time - remove in final
    current = [(datetime.date(2020, 4, 17), '1693.15', '1692.55', '15.16'), (datetime.date(2020, 4, 16), '1717.85', '1729.50', '15.50'), (datetime.date(2020, 4, 15), '1712.25', '1718.65', '15.57'), (datetime.date(2020, 4, 14), '1715.85', '1741.90', '15.51'), (datetime.date(2020, 4, 9), '1662.50', '1680.65', '15.18'), (datetime.date(2020, 4, 8), '1649.05', '1647.80', '15.06'), (datetime.date(2020, 4, 7), '1652.20', '1649.25', '15.08'), (datetime.date(2020, 4, 6), '1636.60', '-', '-'), (datetime.date(2020, 4, 3), '1609.75', '1613.10', '14.39'), (datetime.date(2020, 4, 2), '1588.05', '-', '-'), (datetime.date(2020, 4, 1), '1594.25', '1576.55', '14.02'), (datetime.date(2020, 3, 31), '1604.65', '1608.95', '13.93'), (datetime.date(2020, 3, 30), '1624.45', '1618.30', '14.06'), (datetime.date(2020, 3, 27), '1621.20', '1617.30', '14.32'), (datetime.date(2020, 3, 26), '1620.10', '1634.80', '14.42'), (datetime.date(2020, 3, 25), '1620.95', '1605.45', '13.96'), (datetime.date(2020, 3, 24), '1599.50', '1605.75', '13.62'), (datetime.date(2020, 3, 23), '1494.50', '1525.40', '12.51'), (datetime.date(2020, 3, 20), '1504.45', '1494.40', '12.63'), (datetime.date(2020, 3, 19), '1480.70', '1474.25', '12.00'), (datetime.date(2020, 3, 18), '1506.00', '1498.20', '12.42'), (datetime.date(2020, 3, 17), '1472.35', '1536.20', '12.44'), (datetime.date(2020, 3, 16), '1504.65', '1487.70', '12.96'), (datetime.date(2020, 3, 13), '1588.15', '1562.80', '15.77'), (datetime.date(2020, 3, 12), '1636.65', '1570.70', '16.52'), (datetime.date(2020, 3, 11), '1662.50', '1653.75', '17.02'), (datetime.date(2020, 3, 10), '1657.40', '1655.70', '17.07'), (datetime.date(2020, 3, 9), '1676.60', '1672.50', '16.88'), (datetime.date(2020, 3, 6), '1687.00', '1683.65', '17.48'), (datetime.date(2020, 3, 5), '1647.45', '1659.60', '17.20'), (datetime.date(2020, 3, 4), '1644.80', '1641.85', '17.25'), (datetime.date(2020, 3, 3), '1599.05', '1615.50', '16.81'), (datetime.date(2020, 3, 2), '1609.70', '1599.65', '16.92'), (datetime.date(2020, 2, 28), '1626.35', '1609.85', '17.18'), (datetime.date(2020, 2, 27), '1646.60', '1652.00', '18.05'), (datetime.date(2020, 2, 26), '1647.95', '1634.90', '18.08'), (datetime.date(2020, 2, 25), '1655.90', '1650.30', '18.33'), (datetime.date(2020, 2, 24), '1682.35', '1671.65', '18.78'), (datetime.date(2020, 2, 21), '1633.70', '1643.30', '18.56'), (datetime.date(2020, 2, 20), '1610.35', '1619.00', '18.38'), (datetime.date(2020, 2, 19), '1609.50', '1604.20', '18.34'), (datetime.date(2020, 2, 18), '1588.20', '1589.85', '17.88'), (datetime.date(2020, 2, 17), '1580.30', '1580.80', '17.80'), (datetime.date(2020, 2, 14), '1576.35', '1581.40', '17.70'), (datetime.date(2020, 2, 13), '1575.00', '1575.05', '17.64'), (datetime.date(2020, 2, 12), '1566.75', '1563.70', '17.56'), (datetime.date(2020, 2, 11), '-', '1570.50', '17.70'), (datetime.date(2020, 2, 7), '1568.30', '1572.65', '17.77'), (datetime.date(2020, 2, 6), '1564.75', '1563.30', '17.76'), (datetime.date(2020, 2, 5), '1552.20', '1553.30', '17.62'), (datetime.date(2020, 2, 4), '1571.20', '1558.35', '17.73'), (datetime.date(2020, 2, 3), '1578.85', '1574.75', '17.77'), (datetime.date(2020, 1, 31), '1580.85', '1584.20', '17.88'), (datetime.date(2020, 1, 30), '1580.40', '1578.25', '17.72'), (datetime.date(2020, 1, 29), '1571.20', '-', '-'), (datetime.date(2020, 1, 28), '1579.60', '1574.00', '17.98'), (datetime.date(2020, 1, 27), '1583.45', '1580.10', '18.30'), (datetime.date(2020, 1, 24), '1561.85', '1564.30', '17.83'), (datetime.date(2020, 1, 23), '1554.05', '-', '-'), (datetime.date(2020, 1, 22), '1558.10', '1556.90', '17.77'), (datetime.date(2020, 1, 21), '1556.25', '1551.30', '17.98'), (datetime.date(2020, 1, 20), '1559.25', '1560.15', '18.06'), (datetime.date(2020, 1, 17), '1556.50', '1557.60', '18.06'), (datetime.date(2020, 1, 16), '1555.20', '1554.55', '18.01'), (datetime.date(2020, 1, 15), '1551.90', '1549.00', '17.85'), (datetime.date(2020, 1, 14), '1544.95', '1545.10', '17.77'), (datetime.date(2020, 1, 13), '1550.35', '1549.90', '17.98'), (datetime.date(2020, 1, 10), '1548.80', '1553.60', '17.92'), (datetime.date(2020, 1, 9), '1547.85', '1550.75', '17.91'), (datetime.date(2020, 1, 8), '1582.85', '1571.95', '18.42'), (datetime.date(2020, 1, 7), '1566.50', '1567.85', '18.14'), (datetime.date(2020, 1, 6), '1576.85', '1573.10', '18.44'), (datetime.date(2020, 1, 3), '1547.40', '1548.75', '18.21'), (datetime.date(2020, 1, 2), '1520.55', '1527.10', '17.92')]
    load_xlsx()
    gold_mr = verify_mr('gold')
    silver_mr = verify_mr('silver')
    update()
    
    
    
    

'''
next steps
- check for relative ratios in alert zones
- produce a chart graphic, dated?
- produce an alert of some kind. email or?
- script to run daily at x time or on startup if not run
'''


