import sys
'''import pandas as pd
from pandas import DataFrame'''
from interface import *
from formAdd_ui import *
from mongoCnt import *
from PySide6.QtWidgets import QApplication, QMessageBox,QInputDialog,QTextEdit
from PySide6.QtCore import QStringListModel,QModelIndex
from PySide6.QtGui import QIcon
import common.log
import os

class  MainWindow(QMainWindow):
#------Khoi Tao---------------------------------------------------
    def __init__(self, parent = None ):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('img/kca.ico'))
        self.setWindowTitle('Code Record Library - Developed by Kent')
        #show window 
        self.show()
        #event
        self.ui.opAll.clicked.connect(self.locDataAll)
        self.ui.lvFunc.clicked.connect(self.on_item_clicked)
        self.ui.btAdd.clicked.connect(self.open_new_form)
        self.ui.btFix.clicked.connect(self.fixData)
        self.ui.btDel.clicked.connect(self.DeleteDoc)
        self.ui.btLog.clicked.connect(self.logCheck)
        self.ui.cbGroup.currentTextChanged.connect(self.loadGroup)
        self.ui.txExp.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.ui.txSyn.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.ui.txTim.textChanged.connect(self.on_text_changed)
        
#------Ham thuc thi-------------------------------------------
    def on_text_changed(self):
        try:
            if self.ui.opGroup.isChecked() == True:
                txt = self.ui.txTim.text()
                strGroup = self.ui.cbGroup.currentText()
                listGroup = truyVanByText(txt,strGroup)
                # Thêm mỗi mục vào QListWidget
                model = list()
                modelRong = QStringListModel(list())
                for item in listGroup:
                    #listWidgetItem = item.get('name')  # Chọn trường bạn muốn hiển thị
                    model.append(item.get('name'))
                kk = QStringListModel(model)
                self.ui.lvFunc.setModel(modelRong)  
                self.ui.lvFunc.setModel(kk)  
            else:
                txt = self.ui.txTim.text()
                listGroup = truyVanByTextAll(txt)
                # Thêm mỗi mục vào QListWidget
                model = list()
                modelRong = QStringListModel(list())
                for item in listGroup:
                    #listWidgetItem = item.get('name')  # Chọn trường bạn muốn hiển thị
                    model.append(item.get('name'))
                kk = QStringListModel(model)
                self.ui.lvFunc.setModel(modelRong)  
                self.ui.lvFunc.setModel(kk)                            
        except Exception as e:
            common.log.logExport(e)    
    def logCheck(self):
        #common.log.logExport("Test Local Folder") 
        pyFile_abs_path = os.path.abspath(sys.argv[0])
        log_folder_path = os.path.dirname(pyFile_abs_path) + r'\log';
        if not os.path.exists(log_folder_path):
            os.mkdir(log_folder_path)
        os.startfile(log_folder_path)
    def clearOldData(self):
        self.ui.txName.setText("")
        self.ui.txMean.setText("")
        self.ui.txLib.setText("")
        self.ui.txSyn.setText("")
        self.ui.txExp.setText("")
    def loadGroup(self):
        try:
            self.clearOldData()
            if self.ui.opGroup.isChecked() == True:
                strGroup = self.ui.cbGroup.currentText()
                listGroup = truyVanByCodeGroup(strGroup)
                print(len(listGroup))
                if len(listGroup)==0:
                    self.ui.lbNotice.setText(f"Không Có Dữ Liệu Của {strGroup}")
                else:
                # Thêm mỗi mục vào QListWidget
                    model = list()
                    modelRong = QStringListModel(list())
                    for item in listGroup:
                        #listWidgetItem = item.get('name')  # Chọn trường bạn muốn hiển thị
                        model.append(item.get('name'))
                    kk = QStringListModel(model)
                    self.ui.lvFunc.setModel(modelRong)  
                    self.ui.lvFunc.setModel(kk)  
                    self.ui.lbNotice.setText(f"Có Dữ Liệu Của {strGroup}")               
            else:  
                QMessageBox.information(self, "Thông Báo", f"Phải chọn Group Code!!!")
                self.ui.cbGroup.setCurrentText("-")
        except Exception as e:
            common.log.logExport(e)
    def get_a_str(self):
        title = "Enter a Modify's Password"
        label = "Type your password"
        text = "my secret password"
        mode = QLineEdit.Password
        my_selected_str, ok = QInputDialog.getText(
        self, title, label, mode, text)
        return my_selected_str
    def fixData(self):
        try:
            passConfirm = self.get_a_str()
            if passConfirm == "21077421$":
                if self.ui.txName.toPlainText() != "":
                    strType = self.ui.lbNotice.text().split('-')[1]
                    updateData(self.ui.txName.toPlainText(),self.ui.txLib.toPlainText(),
                            self.ui.txMean.toPlainText(),self.ui.txSyn.toPlainText(),
                            self.ui.txExp.toPlainText(),strType)
                    QMessageBox.information(self, "Thông Báo", f"Sửa Data Vào DB {strType} OK!!!")            
            else:
                QMessageBox.information(self, "Cảnh Báo", f"PassWord Admin không đúng!!!") 
        except Exception as e:
            common.log.logExport(e)         
    def DeleteDoc(self):
        try:
            passConfirm = self.get_a_str()
            if passConfirm == "21077421$":
                if self.ui.txName.toPlainText() != "" and self.ui.txName.toPlainText() != "-":
                    strType = self.ui.lbNotice.text().split('-')[1]
                    deleleDcm(self.ui.txName.toPlainText(),strType)
                    modelRong = list()
                    modelRong = QStringListModel(modelRong)
                    self.ui.lvFunc.setModel(modelRong)
                    self.ui.cbGroup.setCurrentText("-")
                    self.ui.opAll.setChecked(False)
                    self.ui.opGroup.setChecked(False)
                    QMessageBox.information(self, "Thông Báo", f"Xóa Function {self.ui.txName.toPlainText()} ở DB {strType} OK!!!")      
            else:
                QMessageBox.information(self, "Cảnh Báo", f"PassWord Admin không đúng!!!")
            #common.log.logExport(e) 
        except Exception as e:
            common.log.logExport(e)                   
    def on_item_clicked(self, index: QModelIndex): # phải import QModelIndex từ pyside6.qtcore để lấy ra index của dòng click
        try:
            # Lấy văn bản của dòng được click
            #sttAllOp = self.ui.opAll.isChecked()
            #sttGroupOp = self.ui.opGroup.isChecked()
            row = index.row()
            model = self.ui.lvFunc.model()
            value = model.data(index, role=Qt.DisplayRole)
            cbboValue = self.ui.cbGroup.currentText()
            if self.ui.opGroup.isChecked() == True:
                listRecord = truyVanHaiDk(value,cbboValue)
            elif self.ui.opAll.isChecked() == True:
                listRecord = truyVanMotDk(value)
            if len(listRecord) == 0:
                self.ui.lbNotice.setText("")
                self.ui.lbNotice.setText("Mã Code Không Tồn Tại ")
                self.xoaText()
            else:
                self.ui.lbNotice.setText("")
                self.ui.txName.setText(listRecord[0]['name'])
                self.ui.txLib.setText(listRecord[0]['lib'])
                self.ui.txMean.setText(listRecord[0]['mean'])
                self.ui.txSyn.setText(listRecord[0]['syn'])
                self.ui.txExp.setText(listRecord[0]['exp'])
                self.ui.lbNotice.setText(f"Có Dữ Liệu Trong DB-{listRecord[0]['type']} ")            

            print(listRecord)
        except Exception as e:
            common.log.logExport(e)
    def xoaText(self):
        self.ui.txName.setText("")
        self.ui.txLib.setText("")
        self.ui.txMean.setText("")
        self.ui.txSyn.setText("")
        self.ui.txExp.setText("")        
    def showEvent(self, event):
        try:
            super(MainWindow, self).showEvent(event)
            # Thêm mục vào combobox khi form được hiển thị
            listGroup = showDb("category")
            for item in listGroup:
                self.ui.cbGroup.addItem(item.get('name'))
        except Exception as e:
            common.log.logExport(e)
    def locDataAll(self):
        try:
            #print('ok')
            listData = showDb('CodeRecord')
            #frData = pd.DataFrame(listData)
            # Thêm mỗi mục vào QListWidget
            model = list()
            modelRong = list()
            modelRong = QStringListModel(modelRong)
            for item in listData:
                #listWidgetItem = item.get('name')  # Chọn trường bạn muốn hiển thị
                model.append(item.get('name'))
            kk = QStringListModel(model)
            self.ui.lvFunc.setModel(modelRong)  
            self.ui.lvFunc.setModel(kk)       
            #print(model)
        except Exception as e:
            common.log.logExport(e)
    def open_new_form(self):
        try:
            # Tạo form mới
            self.new_form = formAdd()
            self.new_form.show()     
        except Exception as e:
            common.log.logExport(e)   
class formAdd(QMainWindow):
#------Khoi Tao---------------------------------------------------
    def __init__(self, parent = None ):
        QMainWindow.__init__(self)
        self.ui = Ui_formAdd()
        self.ui.setupUi(self)
        self.setWindowTitle("Add New Data Form")
        self.setWindowIcon(QIcon('img/kca.ico'))
        #show window 
        self.show()
        #event 
        self.ui.btSave.clicked.connect(self.dienData)   
        self.ui.txSyn.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.ui.txExp.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        
    def showEvent(self, event):
        try:
            super(formAdd, self).showEvent(event)
            # Thêm mục vào combobox khi form được hiển thị
            listGroup = showDb("category")
            for item in listGroup:
                self.ui.cbGroup.addItem(item.get('name')) 
        except Exception as e:
            common.log.logExport(e)   
#------Ham thuc thi-------------------------------------------
    def dienData(self):
        try:
            flag = self.kiemTraRong()
            if flag == 0:
                return
            count = self.kiemTraTrung()
            if count > 0:
                QMessageBox.critical(self, "Cảnh Báo", "Tên Function Bị Trùng!!!")
                return
            #print('tiep')
            insertDb('CodeRecord',self.ui.txName.toPlainText()
                    ,self.ui.txName_2.toPlainText(),self.ui.txName_3.toPlainText(),
                    self.ui.txSyn.toPlainText(),self.ui.txExp.toPlainText(),self.ui.cbGroup.currentText())
            self.xoaOldData()
            QMessageBox.information(self, "Thông Báo", "Điền Data Vào DB OK!!!")
        except Exception as e:
            common.log.logExport(e)
    def xoaOldData(self): 
        self.ui.txName.setText("")
        self.ui.txName_2.setText("")
        self.ui.txName_3.setText("")
        self.ui.txSyn.setText("")
        self.ui.txExp.setText("")
        self.ui.txName.setText("")

    def kiemTraTrung(self):
        strName = self.ui.txName.toPlainText()
        strType = self.ui.cbGroup.currentText()
        flag = checkExistName(strName,strType)
        count = len(list(flag))
        return count
    def kiemTraRong(self):
        if self.ui.cbGroup.currentText() == "" or self.ui.txName.toPlainText() == "" \
        or self.ui.txName_2.toPlainText() == "" or self.ui.txName_3.toPlainText() =="" \
        or  self.ui.txSyn.toPlainText() == "" or self.ui.txExp.toPlainText() == "" :  
            QMessageBox.critical(self, "Thông Báo", "Không Được Để Trống Data!!!")
            return 0
        else:
            return 1     
#check xem có phải Hàm main không và show form
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())        