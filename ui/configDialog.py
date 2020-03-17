# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButtonSave = QtWidgets.QPushButton(Dialog)
        self.pushButtonSave.setGeometry(QtCore.QRect(50, 180, 75, 23))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonClose = QtWidgets.QPushButton(Dialog)
        self.pushButtonClose.setGeometry(QtCore.QRect(180, 180, 75, 23))
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 120, 141, 16))
        self.label.setObjectName("label")
        self.comboBoxDefaultFX = QtWidgets.QComboBox(Dialog)
        self.comboBoxDefaultFX.setGeometry(QtCore.QRect(220, 110, 60, 22))
        self.comboBoxDefaultFX.setObjectName("comboBoxDefaultFX")
        self.comboBoxDefaultFX.addItem("")
        self.comboBoxDefaultFX.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 81, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonSave.setText(_translate("Dialog", "save"))
        self.pushButtonClose.setText(_translate("Dialog", "close"))
        self.label.setText(_translate("Dialog", "Default reference Currency"))
        self.comboBoxDefaultFX.setItemText(0, _translate("Dialog", "USD"))
        self.comboBoxDefaultFX.setItemText(1, _translate("Dialog", "IDR"))
        self.label_2.setText(_translate("Dialog", "Config Settings"))
