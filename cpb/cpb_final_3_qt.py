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
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMainWindow, QGridLayout, QRadioButton, QApplication

# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

# import sys


class Points(QWidget):
    
    def __init__(self, pos, *args, **kwargs):
        super(Points, self).__init__(*args, **kwargs)
        
        
        
        layout_input = QHBoxLayout()

        layout_input.setContentsMargins(0,0,0,0)
        layout_input.setSpacing(0)
        
        self.input_box = QLineEdit()
        self.push = QPushButton('OK')
        
        layout_input.addWidget(self.input_box)
        layout_input.addWidget(self.push)
        
        self.widget_input = QWidget()
        self.widget_input.setStyleSheet("QPushButton { margin: 1px; }")
        self.widget_input.setLayout(layout_input)
        
        
        layout_shell = QVBoxLayout()
        
        self.label = QLabel('Point {}'.format(pos))
        self.data = QLabel('No data {}'.format(pos))
        # self.data.setText('Still no data {}'.format(pos))

        layout_shell.addWidget(self.label)
        layout_shell.addWidget(self.data)
        layout_shell.addWidget(self.widget_input)

        # widget = QWidget()
        self.setLayout(layout_shell)
        
        

class AtoBWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(AtoBWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle('Point A to Point B')
        self.setStyleSheet("QPushButton { margin: 3px; }")


        # Points

        layout_points = QHBoxLayout()
        pointa = Points('A')
        pointb = Points('B')
        layout_points.addWidget(pointa)
        layout_points.addWidget(pointb)
        
        widget_points = QWidget()
        widget_points.setLayout(layout_points)


        # UOM
        
        layout_uom = QGridLayout()
        
        mi_button = QRadioButton('Miles')
        km_button = QRadioButton('Kilometers')
        ft_button = QRadioButton('Feet')
        m_button = QRadioButton('Meters')
        lg_button = QRadioButton('Leagues')
        nm_button = QRadioButton('Nautical Miles')
        
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
        push_calc.setEnabled(False)
        
        layout_calc.addWidget(label_calc)
        layout_calc.addWidget(push_calc)
        
        
        widget_uom = QWidget()
        widget_uom.setLayout(layout_uom)
        
        widget_calc = QWidget()
        widget_calc.setLayout(layout_calc)
        
        
        # Main
        
        layout = QVBoxLayout()
        layout.addWidget(widget_points)
        layout.addWidget(widget_uom)
        layout.addWidget(widget_calc)
        
        main_widget = QWidget()
        main_widget.setLayout(layout)
        
        self.setCentralWidget(main_widget)
        

app = QApplication([])

window = AtoBWindow()

window.show()

app.exec()

    


'''

Next Step:

Add borders to elements and play with spacing and style sheets.
Start attaching functionality to buttons.


'''




