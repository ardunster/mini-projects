#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:36:30 2020

@author: adunster
"""

'''
Email test code:

but if you’re using a local debugging server, just make sure to use 
localhost as your SMTP server and use port 1025 rather than port 465 or
587. Besides this, you won’t need to use login() or encrypt the 
communication using SSL/TLS.




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



# Imports

import smtplib
from os import path



# Functions

#def get_config():
#    '''
#    Retrieves and assigns globals from config file
#    '''
#    
#    global server
#    global sender_email
#    global receiver_email
#    global username
#    global password
#    
#    with open(config, 'r') as config_file:
#        config_list = [i.strip() for i in config_file if not i[0] == '#' and not i == '\n']
#    
#    config_dict = {}
#    
#    for i in config_list:
#        key,val = i.split(' = ')
#        config_dict.update({key:val})
#
#            
#    server = smtplib.SMTP(smtp_server,port)
#    
#    return config_dict

    

def run_config(user_input=False):
    '''
    Sets up config file. Input: Boolean.
    'True' will run user input for writing config file; 'False' will generate 
    localhost default.
    '''
    if user_input == False:
        with open('send_email_config.py', 'w') as config_file:
            config_file.write('# Email Config\n\n')
            config_file.write('config_dict = { \'localhost\' : True, \n')
            config_file.write('               \'smtp_server\' : \'localhost\',\n')
            config_file.write('               \'smtp_port\' : 1025,\n')
            config_file.write('               \'sender_email\' : \'bogus@bogus.com\',\n')
            config_file.write('               \'receiver_email\' : \'your@bogus.com\',\n')
            config_file.write('               \'username\' : \'\',\n')
            config_file.write('               \'password\' : \'\'\n')
            config_file.write('               }')

def send_alert(alerts):
    '''
    Takes alerts from goldsilver.py and sends email as specified in config.
    '''
    
    server.sendmail(sender_email, receiver_email, message)


# Globals

#config = 'send_email_config.py'

#smtp_server = 'localhost'
#port = 1025
#
#sender_email = 'bogus@bogus.com'
#receiver_email = 'your@gmail.com'
#
#server = smtplib.SMTP(smtp_server,port)
    
# Config 

if not path.exists('send_email_config.py'):
    run_config()
    
import send_email_config as cfg


#
#
#smtp_server = ''
#port = 0
#
#sender_email = ''
#receiver_email = ''
#
#server = smtplib.SMTP(smtp_server,port)
#    
#
#        
        

if __name__ == '__main__':
    run_config(user_input=True)
    
    