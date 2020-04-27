#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:36:30 2020

@author: adunster
"""

'''
Configurable email setup for alerts. By default sends an alert via localhost,
which would need to be loaded and monitored in a terminal window, using command:
sudo python -m smtpd -c DebuggingServer -n localhost:1025
or something similar depending on your exact system and setup.

Running this script by itself (rather than calling it from another script) will
run the config setup 

'''



# Imports

import smtplib, ssl
import re
import importlib
from os import path
from email.message import EmailMessage


# Functions

def run_config(user_input=False):
    '''
    Sets up config file. Input: Boolean.
    'True' will run user input for writing config file; 'False' will generate 
    localhost default.
    '''
    
    global cfg
    
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
        select_input = ''
        # Input:
        while select_input == '':
            
            # Get base values from current config:
            importlib.reload(send_email_config)
            cfg = send_email_config.config_dict
            lh_input = cfg['localhost']
            serv_input = cfg['smtp_server']
            port_input = cfg['smtp_port']
            sender_input = cfg['sender_email']
            rec_input = cfg['receiver_email']
            username_input = cfg['username']
            password_input = cfg['password']
            
            print('Current configuration is: {}'.format(cfg))
            select_input = input('Enter a selection to modify, default to return to default localhost, or end to quit: ')
            
            # Localhost Input
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
            
            # SMTP Server Input
            elif select_input.lower() == 'smtp_server' or 'server' in select_input.lower():
                serv_input = input('Enter a new SMTP server: ')
                select_input = ''
            
            #SMTP Port Input
            elif select_input.lower() == 'smtp_port' or 'port' in select_input.lower():
                port_input = ''
                while not port_input.isdigit():
                    port_input = input('Enter a new SMTP port: ')
                    if not port_input.isdigit():
                        print('Invalid input.')
                        port_input = ''
                select_input = ''
            
            #Sender Email Address Input
            elif select_input.lower() == 'sender_email' or 'sender' in select_input.lower():
                sender_input = ''
                while sender_input == '':
                    sender_input = input('Enter sender email address: ')
                    if bool(re.search('\S+@\S+\.\S+', sender_input)) == False:
                        print('Invalid email address.')
                        sender_input = ''
                select_input = ''
            
            #Receiver Email Address Input
            elif select_input.lower() == 'receiver_email' or 'rec' in select_input.lower():
                rec_input = ''
                while rec_input == '':
                    rec_input = input('Enter receiver email address: ')
                    if bool(re.search('\S+@\S+\.\S+', rec_input)) == False:
                        print('Invalid email address.')
                        sender_input = ''
                select_input = ''
            
            #Sender Email Account Login Username Input
            elif select_input.lower() == 'username' or 'user' in select_input.lower():
                username_input = input('Enter username: ')
                select_input = ''
            
            #Sender Email Account Login Password Input
            elif select_input.lower() == 'password' or 'pass' in select_input.lower():
                password_input = input('Enter your password: ')
                select_input = ''
            
            #Revert to Default Settings
            elif select_input.lower() == 'default':
                print('\nRestoring default settings.\n')
                select_input = ''
                write_config()
                continue
            
            #Exit Config
            elif select_input.lower() in ('end','quit','exit','done'):
                print('\nEnd config.')
                break
            
            else:
                print('\n\'{}\': invalid selection.'.format(select_input))
                select_input = ''
            
            if not serv_input == 'localhost':
                lh_input == False
            
            print()
            write_config(lh_input,serv_input,port_input,sender_input,rec_input,username_input,password_input)




def send_alert(alerts):
    '''
    Takes alerts from goldsilver.py and sends email as specified in config.
    Input: tuple of (int quantity of alerts, string of gold message, string of silver message)
    '''
    msg = EmailMessage()
    
    msg['Subject'] = '{} Gold/Silver Alerts'.format(alerts[0])
    msg['From'] = cfg['sender_email']
    msg['To'] = cfg['receiver_email']
    
    msg.set_content('You have {a} alerts from goldsilver.py.\n{g}\n{s}'.format(a=alerts[0], g=alerts[1], s=alerts[2]))
    
    if cfg['localhost'] == True:
        server = smtplib.SMTP(cfg['smtp_server'],cfg['smtp_port'])
        server.send_message(msg)
        
    elif cfg['localhost'] == False:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(cfg['smtp_server'],cfg['smtp_port'], context=context) as server:
            server.login(cfg['username'], cfg['password'])
#            server.sendmail(cfg['sender_email'], cfg['receiver_email'], message)
            server.send_message(msg)


    
# Config 

if not path.exists('send_email_config.py'):
    run_config()
    
import send_email_config

cfg = send_email_config.config_dict




if __name__ == '__main__':
    run_config(user_input=True)
