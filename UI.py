# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'UI.ui'
##
# Created by: crd
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionMo = QAction(MainWindow)
        self.actionMo.setObjectName(u"actionMo")
        # self.actionFilter = QAction(MainWindow)
        # self.actionFilter.setObjectName(u"actionFilter")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.radioButton1 = QRadioButton(self.centralwidget)
        self.radioButton1.setObjectName(u"radioButton1")

        self.horizontalLayout_3.addWidget(self.radioButton1)

        self.radioButton2 = QRadioButton(self.centralwidget)
        self.radioButton2.setObjectName(u"radioButton2")

        self.horizontalLayout_3.addWidget(self.radioButton2)

        self.pushButtonRun = QPushButton(self.centralwidget)
        self.pushButtonRun.setObjectName(u"pushButtonRun")

        self.horizontalLayout_3.addWidget(self.pushButtonRun)

        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionMo)
        # self.menu.addAction(self.actionFilter)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.actionAbout)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"\u60ef\u5bfc\u3001\u91cc\u7a0b\u8ba1\u4e0e\u6fc0\u5149\u6570\u636e\u878d\u5408\u5904\u7406\u7cfb\u7edfV1.0", None))
        self.actionMo.setText(QCoreApplication.translate(
            "MainWindow", u"\u6570\u636e\u878d\u5408", None))
        # self.actionFilter.setText(QCoreApplication.translate(
        #     "MainWindow", u"\u6570\u636e\u7b5b\u9009", None))
        self.actionAbout.setText(QCoreApplication.translate(
            "MainWindow", u"\u5173\u4e8e", None))
        self.actionExit.setText(QCoreApplication.translate(
            "MainWindow", u"\u9000\u51fa", None))
        self.actionHelp.setText(QCoreApplication.translate(
            "MainWindow", u"\u5e2e\u52a9", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"\u70b9\u4e91\u6570\u636e\u6587\u4ef6\u5939\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"\u6253\u5f00", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u65b9\u4f4d\u6570\u636e\u6587\u4ef6\u5939\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u6253\u5f00", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"\u878d\u5408\u7b97\u6cd5\uff1a", None))
        self.radioButton1.setText(QCoreApplication.translate(
            "MainWindow", u"\u7b97\u6cd5\u4e00\uff08\u5c0f\u8303\u56f4\u79fb\u52a8\uff09", None))
        self.radioButton2.setText(QCoreApplication.translate(
            "MainWindow", u"\u7b97\u6cd5\u4e8c\uff08\u5927\u8303\u56f4\u79fb\u52a8\uff09", None))
        self.pushButtonRun.setText(QCoreApplication.translate(
            "MainWindow", u"\u8fd0\u884c", None))
        self.menu.setTitle(QCoreApplication.translate(
            "MainWindow", u"\u6253\u5f00", None))
        self.menu_2.setTitle(QCoreApplication.translate(
            "MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi
