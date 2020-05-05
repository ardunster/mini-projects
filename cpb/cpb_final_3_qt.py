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

# app = QApplication([])
# # app.setStyle('Macintosh')

# palette = QPalette()

# palette.setColor(QPalette.ButtonText, Qt.blue)

# app.setPalette(palette)

# app.setStyleSheet("QPushButton { margin: 3ex; }")

# def oh_no_clicked():
#     alert = QMessageBox()
#     alert.setText('Oh no you did it didn\'t you D:')
#     alert.exec_()

# def boring_click():
#     alert = QMessageBox()
#     alert.setText('Why would you think this did something?')
#     alert.exec_()

# window = QWidget()
# layout = QVBoxLayout()

# boring_button = QPushButton('Some stuff top button')
# layout.addWidget(boring_button)

# boring_button.clicked.connect(boring_click)

# button = QPushButton('Don\'t you DARE push this button!!!!')
# layout.addWidget(button)

# button.clicked.connect(oh_no_clicked)

# window.setLayout(layout)
# window.show()

# # label = QLabel('WHATS UP FREAKS!')

# # label.show()

# app.exec()

# class BoringWindow(QMainWindow):
    
#     def __init__(self,*args,**kwargs):
#         super(BoringWindow, self).__init__(*args,**kwargs)

#         # self.windowTitleChanged.connect(self.onWindowTitleChange)
        
#         # self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        
#         # self.windowTitleChanged.connect(lambda x: self.my_custom_fn(25))
        
#         # self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))
        
#         self.setWindowTitle('Boring Window of Boringness')
        
                
#         label = QLabel('This is a boring PyQT window.')
        
#         label.setAlignment(Qt.AlignCenter)
        
#         self.setCentralWidget(label)
        
#         toolbar = QToolBar("My boring toolbar")
#         toolbar.setIconSize(QSize(16,16))
#         self.addToolBar(toolbar)
        
#         button_action = QAction(QIcon('abacus.png'), "Boring button", self)
#         button_action.setStatusTip("booorriiinnnnggg")
#         button_action.triggered.connect(self.onMyToolBarButtonClick)
#         button_action.setCheckable(True)
#         toolbar.addAction(button_action)
        
#         toolbar.addSeparator()
        
#         button_action2 = QAction(QIcon('animal.png'), 'Super XXtra boring button', self)
#         button_action2.setStatusTip('XXtra Boring')
#         button_action2.triggered.connect(self.onMyToolBarButtonClick)
#         button_action2.setCheckable(True)
#         toolbar.addAction(button_action2)
        
#         toolbar.addWidget(QLabel('Ugh'))
#         toolbar.addWidget(QCheckBox())
        
        
#         self.setStatusBar(QStatusBar(self))
        
#     def onWindowTitleChange(self, s):
#         print(s)
        
#     def my_custom_fn(self, a="HELLLO!", b=5):
#         print(a, b)
        
#     def contextMenuEvent(self, event):
#         print("Context menu event!")
#         super(BoringWindow, self).contextMenuEvent(event)
        
#     def onMyToolBarButtonClick(self, s):
#         print("click", s)
        
        
        
# app = QApplication([])

# window = BoringWindow()

# window.show()

# app.exec()


# class MainWindow(QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
        
#         self.setWindowTitle("My Awesome App")
        

#         layout = QVBoxLayout()
#         widgets = [QCheckBox,
#             QComboBox,
#             QDateEdit,
#             QDateTimeEdit,
#             QDial,
#             QDoubleSpinBox,
#             QFontComboBox,
#             QLCDNumber,
#             QLabel,
#             QLineEdit,
#             QProgressBar,
#             QPushButton,
#             QRadioButton,
#             QSlider,
#             QSpinBox,
#             QTimeEdit]
        
#         for w in widgets:
#             layout.addWidget(w())
            
        
#         widget = QWidget()
#         widget.setLayout(layout)
        
#         # Set the central widget of the Window. Widget will expand
#         # to take up all the space in the window by default.
#         self.setCentralWidget(widget)


# # You need one (and only one) QApplication instance per application.
# # Pass in sys.argv to allow command line arguments for your app.
# # If you know you won't use command line arguments QApplication([]) works too.
# app = QApplication(sys.argv)

# window = MainWindow()
# window.show() # IMPORTANT!!!!! Windows are hidden by default.

# # Start the event loop.
# app.exec_()




#----------------------------------

class AtoBWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(AtoBWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle('Point A to Point B')
        
        layout = QVBoxLayout()
        
        # Point A
        label_pointa = QLabel('Point A')
        label_pointa.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        data_pointa = QLabel('No data A')
        data_pointa.setText('Still no data A')
        input_pointa = QLineEdit()
        push_pointa = QPushButton('OK')
        
        layout.addWidget(label_pointa)
        layout.addWidget(data_pointa)
        layout.addWidget(input_pointa)
        layout.addWidget(push_pointa)
        
        # Point B
        
        label_pointb = QLabel('Point B')
        data_pointb = QLabel('No data B')
        data_pointb.setText('Still no data B')
        input_pointb = QLineEdit()
        push_pointb = QPushButton('OK')
        
        layout.addWidget(label_pointb)
        layout.addWidget(data_pointb)
        layout.addWidget(input_pointb)
        layout.addWidget(push_pointb)

        
        # UOM
        
        mi_button = QRadioButton('Miles')
        km_button = QRadioButton('Kilometers')
        ft_button = QRadioButton('Feet')
        m_button = QRadioButton('Meters')
        lg_button = QRadioButton('Leagues')
        nm_button = QRadioButton('Nautical Miles')
        
        layout.addWidget(mi_button)
        layout.addWidget(km_button)
        layout.addWidget(ft_button)
        layout.addWidget(m_button)
        layout.addWidget(lg_button)
        layout.addWidget(nm_button)
        
        # Calculate
        
        label_calc = QLabel('No data final calc')
        push_calc = QPushButton('Calculate!')
        
        layout.addWidget(label_calc)
        layout.addWidget(push_calc)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        

app = QApplication([])

window = AtoBWindow()

window.show()

app.exec()

    







