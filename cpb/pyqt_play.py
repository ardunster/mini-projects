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





# class Color(QWidget):
    
#     def __init__(self, color, *args, **kwargs):
#         super(Color, self).__init__(*args, **kwargs)
#         self.setAutoFillBackground(True)
        
#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)
        
        
# class MainWindow(QMainWindow):
    
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
        
#         self.setWindowTitle('Colorful')
        
#         # layout = QHBoxLayout()

#         # layout.addWidget(Color('red'))
#         # layout.addWidget(Color('green'))
#         # layout.addWidget(Color('blue'))
#         # layout.addWidget(Color('orange'))
        
        
#         # layout1 = QHBoxLayout()
#         # layout1.setContentsMargins(3,5,3,5)
#         # layout1.setSpacing(3)
#         # layout2 = QVBoxLayout()
#         # layout3 = QVBoxLayout()

#         # layout2.addWidget(Color('red'))
#         # layout2.addWidget(Color('yellow'))
#         # layout2.addWidget(Color('purple'))

#         # layout1.addLayout( layout2 )

#         # layout1.addWidget(Color('green'))

#         # layout3.addWidget(Color('red'))
#         # layout3.addWidget(Color('purple'))
        
#         # layout1.addLayout( layout3 )
        
#         layout = QGridLayout()

#         layout.addWidget(Color('red'), 0, 0)
#         layout.addWidget(Color('green'), 1, 0)
#         layout.addWidget(Color('blue'), 1, 1)
#         layout.addWidget(Color('purple'), 2, 1)
        
#         widget = QWidget()
#         widget.setLayout(layout)
        
#         self.setCentralWidget(widget)
        


# class MainWindow(QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
        
#         self.setWindowTitle("My Awesome App")
        
#         widget = QComboBox()
#         widget.addItems(["One", "Two", "Three"])

#         # The default signal from currentIndexChanged sends the index
#         widget.currentIndexChanged.connect( self.index_changed )
        
#         # The same signal can send a text string
#         widget.currentIndexChanged[str].connect( self.text_changed )

#         self.setCentralWidget(widget)


#     def index_changed(self, i): # i is an int
#         print(i)
        
#     def text_changed(self, s): # s is a str
#         print(s)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")
        
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        #widget.setReadOnly(True) # uncomment this to make readonly
        
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)
        
        
    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())
        
    def text_changed(self, s):
        print("Text changed...")
        print(s)
            
    def text_edited(self, s):
        print("Text edited...")
        print(s)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication([])

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()