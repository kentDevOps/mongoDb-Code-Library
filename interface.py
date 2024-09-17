# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
'''from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QWidget)'''
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject,QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,QMainWindow, QPushButton, QRadioButton,QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1272, 793)
        MainWindow.setMinimumSize(QSize(1272, 793))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1272, 793))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frTim = QFrame(self.centralwidget)
        self.frTim.setObjectName(u"frTim")
        self.frTim.setStyleSheet(u"#frTim\n"
"{\n"
"background-color: #26364d;\n"
"}")
        self.frTim.setFrameShape(QFrame.StyledPanel)
        self.frTim.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frTim)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cbGroup = QComboBox(self.frTim)
        self.cbGroup.setObjectName(u"cbGroup")
        self.cbGroup.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setPointSize(8)
        font.setItalic(True)
        fontZ = QFont()
        fontZ.setPointSize(12)
        fontZ.setItalic(True)        
        self.cbGroup.setFont(fontZ)
        self.cbGroup.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.cbGroup, 0, 1, 1, 2)

        self.label_2 = QLabel(self.frTim)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_9 = QLabel(self.frTim)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.txTim = QLineEdit(self.frTim)
        self.txTim.setObjectName(u"txTim")
        self.txTim.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.txTim.setFont(font2)
        self.txTim.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.txTim, 1, 1, 1, 2)

        self.label_3 = QLabel(self.frTim)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.opGroup = QRadioButton(self.frTim)
        self.opGroup.setObjectName(u"opGroup")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setItalic(True)
        self.opGroup.setFont(font3)
        self.opGroup.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.opGroup, 3, 2, 1, 1)

        self.opAll = QRadioButton(self.frTim)
        self.opAll.setObjectName(u"opAll")
        self.opAll.setFont(font3)
        self.opAll.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.opAll, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.frTim, 1, 0, 1, 2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"\n"
"#frame_2\n"
"{\n"
"   background-color: #26364d;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_8, 0, 2, 1, 1)

        self.txName = QTextEdit(self.frame_2)
        self.txName.setObjectName(u"txName")
        self.txName.setFont(fontZ)

        self.gridLayout_4.addWidget(self.txName, 1, 0, 1, 1)

        self.txSyn = QTextEdit(self.frame_2)
        self.txSyn.setObjectName(u"txSyn")
        self.txSyn.setFont(font)
        

        self.gridLayout_4.addWidget(self.txSyn, 1, 1, 5, 1)

        self.txExp = QTextEdit(self.frame_2)
        self.txExp.setObjectName(u"txExp")
        self.txExp.setFont(font)

        self.gridLayout_4.addWidget(self.txExp, 1, 2, 5, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)

        self.txLib = QTextEdit(self.frame_2)
        self.txLib.setObjectName(u"txLib")
        self.txLib.setFont(fontZ)

        self.gridLayout_4.addWidget(self.txLib, 3, 0, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.txMean = QTextEdit(self.frame_2)
        self.txMean.setObjectName(u"txMean")
        self.txMean.setFont(fontZ)

        self.gridLayout_4.addWidget(self.txMean, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 2, 1, 1)

        self.frDisplay = QFrame(self.centralwidget)
        self.frDisplay.setObjectName(u"frDisplay")
        self.frDisplay.setStyleSheet(u"#frDisplay\n"
"{\n"
"	background-color: #26364d;\n"
"}\n"
"")
        self.frDisplay.setFrameShape(QFrame.StyledPanel)
        self.frDisplay.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frDisplay)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lbNotice = QLabel(self.frDisplay)
        self.lbNotice.setObjectName(u"lbNotice")
        font4 = QFont()
        font4.setPointSize(8)
        font4.setItalic(True)
        self.lbNotice.setFont(font4)
        self.lbNotice.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.lbNotice, 2, 0, 1, 1)

        self.lvFunc = QListView(self.frDisplay)
        self.lvFunc.setObjectName(u"lvFunc")
        self.lvFunc.setFont(font3)

        self.gridLayout_5.addWidget(self.lvFunc, 1, 0, 1, 1)

        self.label_10 = QLabel(self.frDisplay)
        self.label_10.setObjectName(u"label_10")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frDisplay, 2, 0, 1, 2)

        self.frHeader = QFrame(self.centralwidget)
        self.frHeader.setObjectName(u"frHeader")
        self.frHeader.setStyleSheet(u"#frHeader\n"
"{\n"
" background-color: #26364d;\n"
"}")
        self.frHeader.setFrameShape(QFrame.StyledPanel)
        self.frHeader.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frHeader)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbHeader = QLabel(self.frHeader)
        self.lbHeader.setObjectName(u"lbHeader")
        font6 = QFont()
        font6.setFamilies([u"Stencil"])
        font6.setPointSize(53)
        self.lbHeader.setFont(font6)
        self.lbHeader.setLayoutDirection(Qt.LeftToRight)
        self.lbHeader.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbHeader.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbHeader, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frHeader, 0, 0, 1, 3)

        self.frNutBam = QFrame(self.centralwidget)
        self.frNutBam.setObjectName(u"frNutBam")
        self.frNutBam.setMinimumSize(QSize(935, 112))
        self.frNutBam.setStyleSheet(u"QPushButton \n"
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
"}\n"
"QPushButton:hover#btAddNew\n"
"{\n"
"background-color: #55557f;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255,255,255);\n"
"border-width: 1.5px;\n"
"border-style: solid;\n"
"}\n"
"#frNutBam\n"
"{\n"
"background-color: #26364d;\n"
"}\n"
"")
        self.frNutBam.setFrameShape(QFrame.StyledPanel)
        self.frNutBam.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frNutBam)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btAdd = QPushButton(self.frNutBam)
        self.btAdd.setObjectName(u"btAdd")
        self.btAdd.setMinimumSize(QSize(150, 45))
        self.btAdd.setFont(font5)
        self.btAdd.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.btAdd)

        self.btFix = QPushButton(self.frNutBam)
        self.btFix.setObjectName(u"btFix")
        self.btFix.setMinimumSize(QSize(150, 45))
        self.btFix.setFont(font5)
        self.btFix.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.btFix)

        self.btDel = QPushButton(self.frNutBam)
        self.btDel.setObjectName(u"btDel")
        self.btDel.setMinimumSize(QSize(150, 45))
        self.btDel.setFont(font5)
        self.btDel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.btDel)

        self.btLog = QPushButton(self.frNutBam)
        self.btLog.setObjectName(u"btLog")
        self.btLog.setMinimumSize(QSize(150, 45))
        self.btLog.setFont(font5)
        self.btLog.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.btLog)

        self.btExp = QPushButton(self.frNutBam)
        self.btExp.setObjectName(u"btExp")
        self.btExp.setMinimumSize(QSize(150, 45))
        self.btExp.setFont(font5)
        self.btExp.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.btExp)


        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frNutBam, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Filter Option", None))
        self.opGroup.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.opAll.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Syntax", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Example", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Meaning", None))
        self.lbNotice.setText(QCoreApplication.translate("MainWindow", u"Notice", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Main Code Name", None))
        self.lbHeader.setText(QCoreApplication.translate("MainWindow", u"Record Code System", None))
        self.btAdd.setText(QCoreApplication.translate("MainWindow", u"Add Data", None))
        self.btFix.setText(QCoreApplication.translate("MainWindow", u"Fix Data", None))
        self.btDel.setText(QCoreApplication.translate("MainWindow", u"Delete Data", None))
        self.btLog.setText(QCoreApplication.translate("MainWindow", u"Check Log", None))
        self.btExp.setText(QCoreApplication.translate("MainWindow", u"Export Doc", None))
    # retranslateUi

