#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:29:34 2020

@author: adunster
"""
'''
My First attempt building a UI, using pyqt.

This is designed to use functionality in the third part of my final project
for Complete Python Bootcamp, but provide a GUI to it instead of running it in 
command line/IPython console.
'''


# from PyQt5.QtCore import 
# from PyQt5.QtGui import 
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLineEdit, QPushButton, 
                             QVBoxLayout, QLabel, QMainWindow, QGridLayout, 
                             QRadioButton, QApplication, QFrame, QSizePolicy,
                             QDialog)

# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

# import sys

import cpb_final_3

class Points(QFrame):
    
    def __init__(self, pos, *args, **kwargs):
        super(Points, self).__init__(*args, **kwargs)
        
        
        
        layout_input = QHBoxLayout()

        layout_input.setContentsMargins(0,0,0,0)
        layout_input.setSpacing(0)
        
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText('Enter Location {}'.format(pos))
        self.push = QPushButton('OK')
        
        self.input_box.returnPressed.connect(self.ok_pressed)
        self.push.clicked.connect(self.ok_pressed)
        
        layout_input.addWidget(self.input_box)
        layout_input.addWidget(self.push)
        
        self.widget_input = QWidget()
        self.widget_input.setStyleSheet("QPushButton { margin: 1ex; }")
        self.widget_input.setLayout(layout_input)
        
        
        layout_shell = QVBoxLayout()
        layout_shell.setContentsMargins(4,4,4,4)
        layout_shell.setSpacing(4)
        
        self.label = QLabel('Point {}'.format(pos))
        label_font = self.label.font()
        label_font.setBold(True)
        label_font.setPointSize(16)
        self.label.setFont(label_font)
        self.data = QLabel('No data {}'.format(pos))
        self.data.setMinimumHeight(48)
        # self.data.setMinimumWidth(300)

        layout_shell.addWidget(self.label)
        layout_shell.addWidget(self.data)
        layout_shell.addWidget(self.widget_input)

        self.setLayout(layout_shell)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        
        
    def ok_pressed(self):
        location_input = self.input_box.text()
        location = cpb_final_3.locate_city(location_input)
        if cpb_final_3.verify_city(location):
            self.data.setText(str(location))
            self.data.setWordWrap(True)
            self.valid_location = True
        else:
            self.data.setText('Invalid Input {}'.format(location_input))
            self.valid_location = False

        

        

class AtoBWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(AtoBWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle('Point A to Point B')
        self.setStyleSheet("QPushButton { margin: 3px; }")
        self.setMinimumWidth(500)


        # Points

        layout_points = QHBoxLayout()
        layout_points.setContentsMargins(0,0,0,0)
        layout_points.setSpacing(0)
        pointa = Points('A')
        pointb = Points('B')
        layout_points.addWidget(pointa, 1)
        layout_points.addWidget(pointb, 1)
        
        widget_points = QWidget()
        widget_points.setLayout(layout_points)
        widget_points.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


        # UOM
        
        uom_label = QLabel('Select unit of measurement:')
        
        layout_uom = QGridLayout()
        
        self.uom = ''
        
        mi_button = QRadioButton('Miles')
        mi_button.setChecked(True)
        mi_button.toggled.connect(lambda:self.uom_state(mi_button))
        km_button = QRadioButton('Kilometers')
        km_button.toggled.connect(lambda:self.uom_state(km_button))
        ft_button = QRadioButton('Feet')
        ft_button.toggled.connect(lambda:self.uom_state(ft_button))
        m_button = QRadioButton('Meters')
        m_button.toggled.connect(lambda:self.uom_state(m_button))
        lg_button = QRadioButton('Leagues')
        lg_button.toggled.connect(lambda:self.uom_state(lg_button))
        nm_button = QRadioButton('Nautical Miles')
        nm_button.toggled.connect(lambda:self.uom_state(nm_button))
        
        layout_uom.addWidget(mi_button, 0, 0)
        layout_uom.addWidget(km_button, 0, 1)
        layout_uom.addWidget(ft_button, 0, 2)
        layout_uom.addWidget(m_button, 1, 0)
        layout_uom.addWidget(lg_button, 1, 1)
        layout_uom.addWidget(nm_button, 1, 2)
        
        
        # Calculate
        
        layout_calc = QVBoxLayout()
        
        label_calc = QLabel('')
        push_calc = QPushButton('Calculate!')
        # push_calc.setEnabled(False)
        
        layout_calc.addWidget(label_calc)
        layout_calc.addWidget(push_calc)
        
        
        widget_uom = QWidget()
        widget_uom.setLayout(layout_uom)
        
        widget_calc = QWidget()
        widget_calc.setLayout(layout_calc)
        
        
        # Main
        
        layout = QVBoxLayout()
        layout.addWidget(widget_points)
        layout.addWidget(uom_label)
        layout.addWidget(widget_uom)
        layout.addWidget(widget_calc)
        
        main_widget = QWidget()
        main_widget.setLayout(layout)
        
        self.setCentralWidget(main_widget)
        
    def uom_state(self,b):
        
        if b.text() == 'Miles':
            if b.isChecked() == True:
                self.uom = 'miles'
            else:
                self.uom = ''
        elif b.text() == 'Kilometers':
            if b.isChecked() == True:
                self.uom = 'kilometers'
            else:
                self.uom = ''
        elif b.text() == 'Feet':
            if b.isChecked() == True:
                self.uom = 'feet'
            else:
                self.uom = ''
        elif b.text() == 'Meters':
            if b.isChecked() == True:
                self.uom = 'meters'
            else:
                self.uom = ''
        elif b.text() == 'Leagues':
            if b.isChecked() == True:
                self.uom = 'leagues'
            else:
                self.uom = ''
        elif b.text() == 'Nautical Miles':
            if b.isChecked() == True:
                self.uom = 'nau_miles'
            else:
                self.uom = ''
        
        # print(self.uom)
        
        
    def calc_pressed(self):
        pass
        

        

app = QApplication([])

window = AtoBWindow()

window.show()

app.exec()

    


'''

Next Step:

Add borders to elements and play with spacing and style sheets.
Start attaching functionality to buttons.


'''




