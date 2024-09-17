# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formAdd.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject, QSize)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QTextEdit, QWidget)

class Ui_formAdd(object):
    def setupUi(self, formAdd):
        if not formAdd.objectName():
            formAdd.setObjectName(u"formAdd")
        formAdd.resize(934, 539)
        formAdd.setMinimumSize(QSize(934, 539))
        self.centralwidget = QWidget(formAdd)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frFunc_2 = QFrame(self.centralwidget)
        self.frFunc_2.setObjectName(u"frFunc_2")
        self.frFunc_2.setStyleSheet(u"background-color: rgb(38, 54, 77);\n"
"QTextEdit\n"
"{\n"
"color: rgb(38, 54, 77);\n"
"}")
        self.frFunc_2.setFrameShape(QFrame.StyledPanel)
        self.frFunc_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frFunc_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.frFunc_2)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(13)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.txName = QTextEdit(self.frFunc_2)
        self.txName.setObjectName(u"txName")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setItalic(True)
        self.txName.setFont(font1)
        self.txName.setStyleSheet(u"#txName\n"
"{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"#txName:focus\n"
"{\n"
"	background-color: #55557f;\n"
"}")

        self.gridLayout_3.addWidget(self.txName, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frFunc_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.txName_2 = QTextEdit(self.frFunc_2)
        self.txName_2.setObjectName(u"txName_2")
        self.txName_2.setFont(font1)
        self.txName_2.setStyleSheet(u"QTextEdit\n"
"{\n"
"color: rgb(255,255,255);\n"
"}\n"
"QTextEdit:focus\n"
"{\n"
"background-color: #55557f;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.txName_2, 3, 0, 1, 1)

        self.label_6 = QLabel(self.frFunc_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)

        self.txName_3 = QTextEdit(self.frFunc_2)
        self.txName_3.setObjectName(u"txName_3")
        self.txName_3.setFont(font1)
        self.txName_3.setStyleSheet(u"#txName_3{\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"#txName_3:focus\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"background-color: #55557f;\n"
"}")

        self.gridLayout_3.addWidget(self.txName_3, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.frFunc_2, 1, 0, 1, 1)

        self.frFunc_3 = QFrame(self.centralwidget)
        self.frFunc_3.setObjectName(u"frFunc_3")
        self.frFunc_3.setStyleSheet(u"background-color: rgb(38, 54, 77);")
        self.frFunc_3.setFrameShape(QFrame.StyledPanel)
        self.frFunc_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frFunc_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.frFunc_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.txSyn = QTextEdit(self.frFunc_3)
        self.txSyn.setObjectName(u"txSyn")
        self.txSyn.setFont(font1)
        self.txSyn.setStyleSheet(u"#txSyn\n"
"{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"#txSyn:focus\n"
"{\n"
"	background-color: #55557f;\n"
"}")

        self.gridLayout_4.addWidget(self.txSyn, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frFunc_3, 1, 1, 1, 1)

        self.frFunc_4 = QFrame(self.centralwidget)
        self.frFunc_4.setObjectName(u"frFunc_4")
        self.frFunc_4.setStyleSheet(u"background-color: rgb(38, 54, 77);")
        self.frFunc_4.setFrameShape(QFrame.StyledPanel)
        self.frFunc_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frFunc_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.frFunc_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)

        self.txExp = QTextEdit(self.frFunc_4)
        self.txExp.setObjectName(u"txExp")
        self.txExp.setFont(font1)
        self.txExp.setStyleSheet(u"#txExp\n"
"{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"#txExp:focus\n"
"{\n"
"	background-color: #55557f;\n"
"}")

        self.gridLayout_5.addWidget(self.txExp, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frFunc_4, 1, 2, 1, 1)

        self.frFunc = QFrame(self.centralwidget)
        self.frFunc.setObjectName(u"frFunc")
        self.frFunc.setStyleSheet(u"#frFunc \n"
"{background-color: rgb(38, 54, 77);\n"
"}\n"
"QPushButton \n"
"{\n"
"background-color: #26364d;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255,255,255);\n"
"border-width: 1.5px;\n"
"border-style: solid;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: #55557f;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255,255,255);\n"
"border-width: 1.5px;\n"
"border-style: solid;\n"
"}")
        self.frFunc.setFrameShape(QFrame.StyledPanel)
        self.frFunc.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frFunc)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, -1, -1, -1)
        self.label_9 = QLabel(self.frFunc)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_9)

        self.cbGroup = QComboBox(self.frFunc)
        self.cbGroup.setObjectName(u"cbGroup")
        self.cbGroup.setMinimumSize(QSize(250, 30))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setItalic(True)
        self.cbGroup.setFont(font3)
        self.cbGroup.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.cbGroup)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.label_10 = QLabel(self.frFunc)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_10, 0, 2, 1, 1)

        self.btSave = QPushButton(self.frFunc)
        self.btSave.setObjectName(u"btSave")
        self.btSave.setMinimumSize(QSize(50, 45))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.btSave.setFont(font4)
        self.btSave.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.btSave, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frFunc, 0, 0, 1, 3)

        formAdd.setCentralWidget(self.centralwidget)

        self.retranslateUi(formAdd)

        QMetaObject.connectSlotsByName(formAdd)
    # setupUi

    def retranslateUi(self, formAdd):
        formAdd.setWindowTitle(QCoreApplication.translate("formAdd", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("formAdd", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("formAdd", u"Library", None))
        self.label_6.setText(QCoreApplication.translate("formAdd", u"Mean", None))
        self.label_7.setText(QCoreApplication.translate("formAdd", u"Syntax", None))
        self.label_8.setText(QCoreApplication.translate("formAdd", u"Example", None))
        self.label_9.setText(QCoreApplication.translate("formAdd", u"Group", None))
        self.label_10.setText("")
        self.btSave.setText(QCoreApplication.translate("formAdd", u"Save Data", None))
    # retranslateUi

