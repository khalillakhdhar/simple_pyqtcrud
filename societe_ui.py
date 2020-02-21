# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'societe.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(533, 729)
        self.ajsc = QtWidgets.QPushButton(Dialog)
        self.ajsc.setGeometry(QtCore.QRect(150, 420, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ajsc.setFont(font)
        self.ajsc.setObjectName("ajsc")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 71, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 121, 31))
        self.label_5.setObjectName("label_5")
        self.titre = QtWidgets.QLineEdit(Dialog)
        self.titre.setGeometry(QtCore.QRect(160, 40, 171, 31))
        self.titre.setObjectName("titre")
        self.adr = QtWidgets.QPlainTextEdit(Dialog)
        self.adr.setGeometry(QtCore.QRect(150, 160, 201, 71))
        self.adr.setObjectName("adr")
        self.des = QtWidgets.QPlainTextEdit(Dialog)
        self.des.setGeometry(QtCore.QRect(160, 270, 201, 71))
        self.des.setObjectName("des")
        self.form = QtWidgets.QComboBox(Dialog)
        self.form.setGeometry(QtCore.QRect(150, 112, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.form.setFont(font)
        self.form.setObjectName("form")
        self.form.addItem("")
        self.form.addItem("")
        self.form.addItem("")
        self.form.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ajsc.setText(_translate("Dialog", "Ajouter"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">titre</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Forme:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Adresse:</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Description:</span></p></body></html>"))
        self.form.setItemText(0, _translate("Dialog", "SARL"))
        self.form.setItemText(1, _translate("Dialog", "SUARL"))
        self.form.setItemText(2, _translate("Dialog", "SARI"))
        self.form.setItemText(3, _translate("Dialog", "Autre"))
