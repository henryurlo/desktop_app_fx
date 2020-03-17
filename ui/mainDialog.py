# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(271, 306)
        self.comboBoxReferenceCurrency = QtWidgets.QComboBox(Dialog)
        self.comboBoxReferenceCurrency.setGeometry(QtCore.QRect(70, 90, 61, 22))
        self.comboBoxReferenceCurrency.setObjectName("comboBoxReferenceCurrency")
        self.comboBoxReferenceCurrency.addItem("")
        self.comboBoxReferenceCurrency.addItem("")
        self.comboBoxReferenceCurrency.addItem("")
        self.labelTitle = QtWidgets.QLabel(Dialog)
        self.labelTitle.setGeometry(QtCore.QRect(60, 20, 181, 31))
        self.labelTitle.setObjectName("labelTitle")
        self.labelUSD = QtWidgets.QLabel(Dialog)
        self.labelUSD.setGeometry(QtCore.QRect(20, 150, 47, 14))
        self.labelUSD.setObjectName("labelUSD")
        self.labelPHP = QtWidgets.QLabel(Dialog)
        self.labelPHP.setGeometry(QtCore.QRect(20, 180, 47, 14))
        self.labelPHP.setObjectName("labelPHP")
        self.labelIDR = QtWidgets.QLabel(Dialog)
        self.labelIDR.setGeometry(QtCore.QRect(20, 210, 47, 14))
        self.labelIDR.setObjectName("labelIDR")
        self.lineEditUSD = QtWidgets.QLineEdit(Dialog)
        self.lineEditUSD.setGeometry(QtCore.QRect(80, 150, 113, 20))
        self.lineEditUSD.setObjectName("lineEditUSD")
        self.lineEditPHP = QtWidgets.QLineEdit(Dialog)
        self.lineEditPHP.setGeometry(QtCore.QRect(80, 180, 113, 20))
        self.lineEditPHP.setObjectName("lineEditPHP")
        self.lineEditIDR = QtWidgets.QLineEdit(Dialog)
        self.lineEditIDR.setGeometry(QtCore.QRect(80, 210, 113, 20))
        self.lineEditIDR.setObjectName("lineEditIDR")
        self.pushButtonConfigure = QtWidgets.QPushButton(Dialog)
        self.pushButtonConfigure.setGeometry(QtCore.QRect(50, 260, 75, 23))
        self.pushButtonConfigure.setObjectName("pushButtonConfigure")
        self.pushButtonLoadRates = QtWidgets.QPushButton(Dialog)
        self.pushButtonLoadRates.setGeometry(QtCore.QRect(170, 260, 75, 23))
        self.pushButtonLoadRates.setObjectName("pushButtonLoadRates")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBoxReferenceCurrency.setItemText(0, _translate("Dialog", "USD"))
        self.comboBoxReferenceCurrency.setItemText(1, _translate("Dialog", "PHP"))
        self.comboBoxReferenceCurrency.setItemText(2, _translate("Dialog", "IDR"))
        self.labelTitle.setText(_translate("Dialog", "Curency Converter"))
        self.labelUSD.setText(_translate("Dialog", "USD"))
        self.labelPHP.setText(_translate("Dialog", "PHP"))
        self.labelIDR.setText(_translate("Dialog", "IDR"))
        self.pushButtonConfigure.setText(_translate("Dialog", "Configure"))
        self.pushButtonLoadRates.setText(_translate("Dialog", "Load Rates"))
