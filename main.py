# -*- coding: utf-8 -*-
# @Time    : 2023/5/24
# @Author  : Chen Ruida
# @Email   : chenruida@outlook.com
# @File    : MainWindow.py
# @desc    : 主窗口

import os
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from UI import Ui_MainWindow
from fusionPoint import FusionPoint


class MainWindow(QMainWindow):
    __pointPath = ""
    __positionPath = ""
    __method = 1

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.radioButton1.setChecked(True)
        self.thread = None
        self.__method = 1

        self.ui.actionExit.triggered.connect(self.close)

        self.ui.radioButton1.toggled.connect(
            lambda: self.btnState(self.ui.radioButton1))
        self.ui.radioButton2.toggled.connect(
            lambda: self.btnState(self.ui.radioButton2))

    def get_msg(self, msg):
        """
        信号-获取信息
        :param msg: 信息
        :return:
        """
        self.ui.textEdit.append(str(msg))

    def btnState(self, btn):
        # 输出按钮1与按钮2的状态，选中还是没选中
        if btn.text() == u"\u7b97\u6cd5\u4e00\uff08\u5c0f\u8303\u56f4\u79fb\u52a8\uff09":
            if btn.isChecked() == True:
                self.ui.textEdit.append(btn.text()+" 已被选择")
                self.__method = 1

        if btn.text() == u"\u7b97\u6cd5\u4e8c\uff08\u5927\u8303\u56f4\u79fb\u52a8\uff09":
            if btn.isChecked() == True:
                self.ui.textEdit.append(btn.text() + " 已被选择")
                self.__method = 2

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        打开文件夹 函数
        :return:  文件夹地址
        """
        self.__pointPath = os.path.normpath(
            QFileDialog.getExistingDirectory(self, "选取文件夹", './'))
        self.ui.lineEdit.setText(self.__pointPath)
        print(self.ui.lineEdit.text())

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        打开文件夹 函数
        :return:  文件夹地址
        """
        self.__positionPath = os.path.normpath(
            QFileDialog.getExistingDirectory(self, "选取文件夹", './'))
        self.ui.lineEdit_2.setText(self.__positionPath)
        print(self.ui.lineEdit_2.text())

    @pyqtSlot()
    def on_pushButtonRun_clicked(self):
        """
        This function is a PyQt slot that is called when the "pushButtonRun" button is clicked. It initializes a FusionPoint thread with the provided point, position, and method parameters. It then connects the thread's signal to the "get_msg" function and starts the thread.
        """
        if self.__pointPath == "" or self.__positionPath == "":
            self.ui.textEdit.append("请先选取文件夹")
            return
        self.thread = FusionPoint(
            self.__pointPath, self.__positionPath, self.__method)
        self.thread.signal.connect(self.get_msg)
        self.thread.start()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    sys.exit(myapp.exec_())
