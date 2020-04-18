#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:43:45 2020

@author: adunster
"""

'''
    
    - Can I fetch gold/silver prices and set up an alert when certain conditions are met?
    
     but if you’re using a local debugging server, just make sure to use 
     localhost as your SMTP server and use port 1025 rather than port 465 or
     587. Besides this, you won’t need to use login() or encrypt the 
     communication using SSL/TLS.

london fix price (what my chart uses) is set pm at 15:00 GMT. However,
site I use to update doesn't list this number until next day. 

gold: 0.975 < > 1.225
'''


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




