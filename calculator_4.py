# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_4.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(984, 606)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(730, 480, 171, 41))
        self.checkBox.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.checkBox.setObjectName("checkBox")
        self.change = QtWidgets.QLabel(Dialog)
        self.change.setGeometry(QtCore.QRect(450, 150, 121, 61))
        self.change.setStyleSheet("font: 16pt \"Times New Roman\";")
        self.change.setObjectName("change")
        self.Blank_2 = QtWidgets.QLineEdit(Dialog)
        self.Blank_2.setGeometry(QtCore.QRect(600, 140, 271, 71))
        self.Blank_2.setObjectName("Blank_2")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 420, 141, 61))
        self.radioButton_2.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(510, 420, 141, 61))
        self.radioButton_3.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.Blank = QtWidgets.QLineEdit(Dialog)
        self.Blank.setGeometry(QtCore.QRect(140, 140, 271, 71))
        self.Blank.setObjectName("Blank")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(120, 420, 121, 51))
        self.radioButton.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName("radioButton")
        self.answer = QtWidgets.QLabel(Dialog)
        self.answer.setGeometry(QtCore.QRect(430, 270, 161, 81))
        self.answer.setStyleSheet("font: 20pt \"Times New Roman\";")
        self.answer.setObjectName("answer")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(730, 430, 111, 31))
        self.radioButton_4.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.setObjectName("radioButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "Inverse division"))
        self.change.setText(_translate("Dialog", "change"))
        self.radioButton_2.setText(_translate("Dialog", "Subtraction"))
        self.radioButton_3.setText(_translate("Dialog", "Multiplication"))
        self.radioButton.setText(_translate("Dialog", "Addition"))
        self.answer.setText(_translate("Dialog", "TextLabel"))
        self.radioButton_4.setText(_translate("Dialog", "Division "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
