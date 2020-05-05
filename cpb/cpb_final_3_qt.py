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


# from PyQt5.QtCore import Qt, QSize
# from PyQt5.QtGui import QPalette, QIcon
# from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QMainWindow, QToolBar, QAction, QStatusBar, QCheckBox

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class Points(QWidget):
    
    def __init__(self, pos, *args, **kwargs):
        super(Points, self).__init__(*args, **kwargs)
        
        layout_shell = QVBoxLayout()
        
        layout_input = QHBoxLayout()
        # layout_input.setStyleSheet("QPushButton { margin: 0ex; }")
        # layout_input.setContentsMargins(0,0,0,0)
        # layout_input.setSpacing(0)
        
        
        label = QLabel('Point {}'.format(pos))
        data = QLabel('No data {}'.format(pos))
        data.setText('Still no data {}'.format(pos))
        
        input_box = QLineEdit()
        push = QPushButton('OK')
        
        layout_shell.addWidget(label)
        layout_shell.addWidget(data)
        layout_input.addWidget(input_box)
        layout_input.addWidget(push)
        
        

class AtoBWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(AtoBWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle('Point A to Point B')
        self.setStyleSheet("QPushButton { margin: 3ex; }")
        
        # layout = QVBoxLayout()
        
        # Point A
        # layout_a = QVBoxLayout()
        
        # label_pointa = QLabel('Point A')
        # data_pointa = QLabel('No data A')
        # data_pointa.setText('Still no data A')
        # input_pointa = QLineEdit()
        # push_pointa = QPushButton('OK')
        
        # layout_a.addWidget(label_pointa)
        # layout_a.addWidget(data_pointa)
        # layout_a.addWidget(input_pointa)
        # layout_a.addWidget(push_pointa)
        
        # Point B
        # layout_b = QVBoxLayout()
        
        # label_pointb = QLabel('Point B')
        # data_pointb = QLabel('No data B')
        # data_pointb.setText('Still no data B')
        # input_pointb = QLineEdit()
        # push_pointb = QPushButton('OK')
        
        # layout_b.addWidget(label_pointb)
        # layout_b.addWidget(data_pointb)
        # layout_b.addWidget(input_pointb)
        # layout_b.addWidget(push_pointb)

        
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
        
        label_calc = QLabel('No data final calc')
        push_calc = QPushButton('Calculate!')
        
        layout_calc.addWidget(label_calc)
        layout_calc.addWidget(push_calc)
        
        
        # Layout
        # widget_a = QWidget()
        # widget_a.setLayout(layout_a)
        
        # widget_b = QWidget()
        # widget_b.setLayout(layout_b)
        
        widget_uom = QWidget()
        widget_uom.setLayout(layout_uom)
        
        widget_calc = QWidget()
        widget_calc.setLayout(layout_calc)
        
        layout_points = QHBoxLayout()
        pointa = Points('A')
        pointb = Points('B')
        layout_points.addWidget(pointa)
        layout_points.addWidget(pointb)
        
        widget_points = QWidget()
        widget_points.setLayout(layout_points)
        
        layout = QVBoxLayout()
        layout.addWidget(widget_points)
        layout.addWidget(widget_uom)
        layout.addWidget(widget_calc)
        
        main_widget = QWidget()
        main_widget.setLayout(layout)
        
        self.setCentralWidget(widget_points)
        

app = QApplication([])

window = AtoBWindow()

window.show()

app.exec()

    


'''

Next Step: Figure out why my Points class isn't working


'''




