#匯入模組套件
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from calculator_4 import Ui_Dialog

#定義click_button函數，按下按鈕時讀取按鈕的文字並打印出來
def click_button():
    readText = ui.pushButton_plus.text()
    ui.answer.clicked.connect(readText)
    print(readText)


def result_exe():
    if ui.Blank.text().isnumeric() and ui.Blank_2.text().isnumeric() :
        readNum = int(ui.Blank.text()) + int(ui.Blank_2.text())
        print('result is '+ str(readNum))
        ui.answer.setText('result is '+ str(readNum))
        ui.change.setText('+')
    else:
        print('please input interger')

def result_exe_2():
    if ui.Blank.text().isnumeric() and ui.Blank_2.text().isnumeric() :
        readNum = int(ui.Blank.text()) - int(ui.Blank_2.text())
        print('result is '+ str(readNum))
        ui.answer.setText('result is '+ str(readNum))
        ui.change.setText('-')
    else:
        print('please input interger')

def result_exe_3():
    if ui.Blank.text().isnumeric() and ui.Blank_2.text().isnumeric() :
        readNum = int(ui.Blank.text()) * int(ui.Blank_2.text())
        print('result is '+ str(readNum))
        ui.answer.setText('result is '+ str(readNum))
        ui.change.setText('*')        
    else:
        print('please input interger')

def result_exe_4():
    if ui.Blank.text().isnumeric() and ui.Blank_2.text().isnumeric() :
        if ui.checkBox.isChecked(): #如果checkbox被勾起
            readNum = int(ui.Blank_2.text()) / int(ui.Blank.text())
        else:
            readNum = int(ui.Blank.text()) / int(ui.Blank_2.text())
        print('result is '+ str(readNum))
        ui.answer.setText('result is '+ str(readNum))
        ui.change.setText('/')
    else:
        print('please input interger')
   
#在單選按鈕被點擊時被調用，並打印出一條訊息
def click_radio():
    print("click_radio")

#設定UI
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

#創建按鈕組並連接函數
buttonGroup = QButtonGroup(widget)
buttonGroup.addButton(ui.radioButton)
buttonGroup.addButton(ui.radioButton_2)
buttonGroup.addButton(ui.radioButton_3)
buttonGroup.addButton(ui.radioButton_4)
ui.radioButton.clicked.connect(result_exe)
ui.radioButton_2.clicked.connect(result_exe_2)
ui.radioButton_3.clicked.connect(result_exe_3)
ui.radioButton_4.clicked.connect(result_exe_4)


#顯示
widget.show()
app.exec_()