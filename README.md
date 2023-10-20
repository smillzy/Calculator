# Calculator
Self made calculator by using Python, QtDesigner

我在 112/04/15~112/06/10 學習 Python UI/UX 圖形介面設計實戰班，檔案為課程的作品

# 安裝指南

1. Qt Designer
   
   請確保您已經安裝 Qt Designer。如果尚未安裝，請前往官方網站下載並安裝：
   [Qt Designer 下載頁面](https://build-system.fman.io/qt-designer-download)

2. Visual Studio Code

   接著，請確保您已經安裝Visual Studio Code。如果尚未安裝，請前往官方網站下載並安裝：
   [Visual Studio Code 下載頁面](https://code.visualstudio.com/download)

# 使用指南

打開Visual Studio Code，直接在Terminal上執行 **calculator_rec_4.py**

開啟後，即可在兩個空白格子中輸入數字，輸入完畢可以點選`Addition`, `Subtraction`, `Multiplication`, `Division`, `Inverse division` 做加減乘除的運算。

# 修改

如果想修改介面，可以參照以下方法

#### 步驟一

將 calculator_4.ui 丟到Qt Designer，修改完後，存成ui檔。

#### 步驟二

修改 calculator_4.py 中按鈕屬性內容。

例如要新增一個反除法`Inverse division`的功能:

```Python
class Ui_Dialog(object):

    #要配置的對話框
    def setupUi(self, Dialog):

        #說明CheckBox是Dialog的子元素
        self.checkBox = QtWidgets.QCheckBox(Dialog)

        #設置位置和大小 (左上角 x 座標, 左上角 y 座標, 寬度, 高度)
        self.checkBox.setGeometry(QtCore.QRect(730, 480, 171, 41))

        #設置樣式
        self.checkBox.setStyleSheet("font: 12pt \"Times New Roman\";")

        #設置物件名稱
        self.checkBox.setObjectName("checkBox")

    #重新宣告按鈕顯示的文字
    def retranslateUi(self, Dialog):

        #設置checkBox的文字為Inverse division
        self.checkBox.setText(_translate("Dialog", "Inverse division"))
```

#### 步驟三

新增功能在 calculator_rec_4.py 中

新增一個反除法`Inverse division`的功能:

```Python
def result_exe_4():
    if ui.Blank.text().isnumeric() and ui.Blank_2.text().isnumeric() :
        if ui.checkBox.isChecked(): #新增在這，如果checkbox被勾起，則為反除法
            readNum = int(ui.Blank_2.text()) / int(ui.Blank.text())
        else:
            readNum = int(ui.Blank.text()) / int(ui.Blank_2.text())
        print('result is '+ str(readNum))
        ui.answer.setText('result is '+ str(readNum))
        ui.change.setText('/')
    else:
        print('please input interger')
```
