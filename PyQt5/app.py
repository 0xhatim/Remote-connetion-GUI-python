# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import socket

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 492)
        Dialog.setStyleSheet("")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 401, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setGeometry(QtCore.QRect(110, 60, 125, 201))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.status_label = QtWidgets.QLabel(self.splitter)
        self.status_label.setObjectName("status_label")
        self.ConnectButton = QtWidgets.QPushButton(self.splitter)
        self.ConnectButton.setObjectName("ConnectButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(30, 50, 321, 161))
        self.tableView.setObjectName("tableView")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(130, 20, 111, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.splitter_3 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_3.setGeometry(QtCore.QRect(60, 270, 239, 32))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.pushButton = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_2.setGeometry(QtCore.QRect(30, 240, 304, 26))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.splitter_2)
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 351, 121))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "IP CONTROLLER"))
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        self.lineEdit.setText(_translate("Dialog",local_ip))
        self.label_2.setText(_translate("Dialog", "PORT"))
        self.lineEdit_2.setText(_translate("Dialog", "9090"))
        self.status_label.setText(_translate("Dialog", "STATUS"))
        self.ConnectButton.setText(_translate("Dialog", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        self.label_3.setText(_translate("Dialog", "Connections"))
        self.pushButton.setText(_translate("Dialog", "Send Command"))
        self.pushButton_2.setText(_translate("Dialog", "Send ALL"))
        self.label_5.setText(_translate("Dialog", "ID"))
        self.label_4.setText(_translate("Dialog", "Command"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
