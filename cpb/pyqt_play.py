#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:31:34 2020

@author: adunster
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


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
