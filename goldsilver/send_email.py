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
import re
import importlib
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
    
#    global cfg
    
    def write_config(localhost=True, smtp_server='localhost', smtp_port=1025, sender_email='bogus@bogus.com', receiver_email='your@bogus.com', username='', password=''):
        '''Writes localhost config, default values localhost'''
        with open('send_email_config.py', 'w') as config_file:
            config_file.write('# Email Config\n\n')
            config_file.write('config_dict = { \'localhost\' : ' + str(localhost) + ', \n')
            config_file.write('               \'smtp_server\' : \'' + str(smtp_server) + '\',\n')
            config_file.write('               \'smtp_port\' : ' + str(smtp_port) + ',\n')
            config_file.write('               \'sender_email\' : \'' + str(sender_email) + '\',\n')
            config_file.write('               \'receiver_email\' : \'' + str(receiver_email) + '\',\n')
            config_file.write('               \'username\' : \'' + str(username) + '\',\n')
            config_file.write('               \'password\' : \'' + str(password) + '\'\n')
            config_file.write('               }')
            
    if user_input == False:
        write_config()
    elif user_input == True:
        # Get base values from current config:
        select_input = ''
        lh_input = cfg['localhost']
        serv_input = cfg['smtp_server']
        port_input = cfg['smtp_port']
        sender_input = cfg['sender_email']
        rec_input = cfg['receiver_email']
        username_input = cfg['username']
        password_input = cfg['password']
        # Input:
        while select_input == '':
            print('Current configuration is: {}'.format(cfg))
            select_input = input('Enter a selection to modify, default to return to default localhost, or end to quit: ')
            
            if select_input == 'localhost':
                lh_input = ''
                while not lh_input == True and not lh_input == False:
                    lh_input = input('Reset server and port to default (localhost)? True or False: ')
                    if lh_input.lower() == 'true' or lh_input[0].lower() == 'y':
                        lh_input = True
                    elif lh_input.lower() == 'false' or lh_input[0].lower() == 'n':
                        lh_input = False
                    else:
                        print('Invalid input.')
                if lh_input == True:
                    serv_input = 'localhost'
                    port_input = 1025
                select_input = ''
                
            elif select_input.lower() == 'smtp_server' or 'server' in select_input.lower():
                serv_input = input('Enter a new SMTP server: ')
                select_input = ''
                
            elif select_input.lower() == 'smtp_port' or 'port' in select_input.lower():
                port_input = ''
                while not port_input.isdigit():
                    port_input = input('Enter a new SMTP port: ')
                    if not port_input.isdigit():
                        print('Invalid input.')
                        port_input = ''
                select_input = ''
                
            elif select_input.lower() == 'sender_email' or 'sender' in select_input.lower():
                sender_input = ''
                while sender_input == '':
                    sender_input = input('Enter sender email address: ')
                    if bool(re.search('\S+@\S+\.\S+', sender_input)) == False:
                        print('Invalid email address.')
                        sender_input = ''
                select_input = ''
                
            elif select_input.lower() == 'receiver_email' or 'rec' in select_input.lower():
                rec_input = ''
                while rec_input == '':
                    rec_input = input('Enter receiver email address: ')
                    if bool(re.search('\S+@\S+\.\S+', rec_input)) == False:
                        print('Invalid email address.')
                        sender_input = ''
                select_input = ''
                
            elif select_input.lower() == 'username' or 'user' in select_input.lower():
                username_input = input('Enter username: ')
                select_input = ''
                
            elif select_input.lower() == 'password' or 'pass' in select_input.lower():
                password_input = input('Enter your password: ')
                select_input = ''
                
            elif select_input.lower() == 'default':
                print('Restoring default settings.')
                write_config()
                
            elif select_input.lower() in ('end','quit','exit','done'):
                print('Finalizing setup.')
                break
            
            else:
                print('\'{}\': invalid selection.\n'.format(select_input))
                select_input = ''
                
            print()
            write_config(lh_input,serv_input,port_input,sender_input,rec_input,username_input,password_input)
            importlib.reload(send_email_config)




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
    
from send_email_config import config_dict as cfg



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
#    pass
    run_config(user_input=True)
    
    