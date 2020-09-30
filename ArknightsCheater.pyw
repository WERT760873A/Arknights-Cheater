# -*- coding: utf-8 -*-

import json,sys,os,socket,subprocess
from PyQt5.QtWidgets import QMainWindow,QApplication,QAbstractItemView,QTableView,QAction,QLabel,QTableWidgetItem,QPushButton,QMessageBox,QFileDialog
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5 import QtCore,QtGui,QtWidgets
import webbrowser
winHeight=720
winWidth=476
#data & default
DebugOff=True
curDir=os.path.abspath(os.path.dirname(__file__))
porxy=12450
#user
isRun=True
isInit=False
isMinors=False
char_isMultiSelect=False
userUID='8888888'
userName='破解用户'
userNameNum='8888'
userLv=120
userAp=135
userApMax=135
userResume='Ta什么都没有留下'
squadsNm=[]
charTableEdit=False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(winHeight, winWidth)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 721, 411))
        self.tabWidget.setStyleSheet("QTabBar::tab:disabled {width: 0; color: transparent;}")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser_init = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_init.setGeometry(QtCore.QRect(10, 20, 511, 311))
        self.textBrowser_init.setObjectName("textBrowser_init")
        self.pushButton_run_init = QtWidgets.QPushButton(self.tab)
        self.pushButton_run_init.setGeometry(QtCore.QRect(580, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_run_init.setFont(font)
        self.pushButton_run_init.setObjectName("pushButton_run_init")
        self.groupBox_porxy_init = QtWidgets.QGroupBox(self.tab)
        self.groupBox_porxy_init.setGeometry(QtCore.QRect(540, 20, 161, 59))
        self.groupBox_porxy_init.setObjectName("groupBox_porxy_init")
        self.gob_porxy_init = QtWidgets.QSpinBox(self.groupBox_porxy_init)
        self.gob_porxy_init.setGeometry(QtCore.QRect(70, 30, 81, 22))
        self.gob_porxy_init.setMaximum(65535)
        self.gob_porxy_init.setProperty("value", 12450)
        self.gob_porxy_init.setObjectName("gob_porxy_init")
        self.label_33 = QtWidgets.QLabel(self.groupBox_porxy_init)
        self.label_33.setGeometry(QtCore.QRect(10, 30, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.inInitInfo = QtWidgets.QLabel(self.tab)
        self.inInitInfo.setGeometry(QtCore.QRect(550, 200, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inInitInfo.setFont(font)
        self.inInitInfo.setObjectName("inInitInfo")
        self.frame_entryInit = QtWidgets.QFrame(self.tab)
        self.frame_entryInit.setGeometry(QtCore.QRect(270, 110, 201, 80))
        self.frame_entryInit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_entryInit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_entryInit.setObjectName("frame_entryInit")
        self.pushButton_initSkip = QtWidgets.QPushButton(self.frame_entryInit)
        self.pushButton_initSkip.setGeometry(QtCore.QRect(70, 50, 131, 31))
        self.pushButton_initSkip.setObjectName("pushButton_initSkip")
        self.label_3 = QtWidgets.QLabel(self.frame_entryInit)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_initCTN = QtWidgets.QPushButton(self.frame_entryInit)
        self.pushButton_initCTN.setGeometry(QtCore.QRect(0, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_initCTN.setFont(font)
        self.pushButton_initCTN.setObjectName("pushButton_initCTN")
        self.pushButton_initSkip_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_initSkip_2.setGeometry(QtCore.QRect(560, 150, 131, 31))
        self.pushButton_initSkip_2.setObjectName("pushButton_initSkip_2")
        self.checkBox_fcm_init = QtWidgets.QCheckBox(self.tab)
        self.checkBox_fcm_init.setGeometry(QtCore.QRect(550, 80, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_fcm_init.setFont(font)
        self.checkBox_fcm_init.setObjectName("checkBox_fcm_init")
        self.tabWidget.addTab(self.tab, "")
        self.tab_userData = QtWidgets.QWidget()
        self.tab_userData.setObjectName("tab_userData")
        self.groupBox_item = QtWidgets.QGroupBox(self.tab_userData)
        self.groupBox_item.setGeometry(QtCore.QRect(240, 10, 231, 141))
        self.groupBox_item.setObjectName("groupBox_item")
        self.item_value = QtWidgets.QSpinBox(self.groupBox_item)
        self.item_value.setGeometry(QtCore.QRect(140, 40, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.item_value.setFont(font)
        self.item_value.setMaximum(999999999)
        self.item_value.setProperty("value", 99999)
        self.item_value.setObjectName("item_value")
        self.list_item = QtWidgets.QListWidget(self.groupBox_item)
        self.list_item.setGeometry(QtCore.QRect(5, 20, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.list_item.setFont(font)
        self.list_item.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.list_item.setObjectName("list_item")
        item = QtWidgets.QListWidgetItem()
        self.list_item.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_item.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_item.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_item.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_item.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_item.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_item.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_item.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_item.addItem(item)
        self.pushButton_itemEdit = QtWidgets.QPushButton(self.groupBox_item)
        self.pushButton_itemEdit.setGeometry(QtCore.QRect(140, 70, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_itemEdit.setFont(font)
        self.pushButton_itemEdit.setObjectName("pushButton_itemEdit")
        self.label_14 = QtWidgets.QLabel(self.tab_userData)
        self.label_14.setGeometry(QtCore.QRect(20, 80, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.tab_userData)
        self.label_16.setGeometry(QtCore.QRect(20, 140, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.user_nameNum = QtWidgets.QLineEdit(self.tab_userData)
        self.user_nameNum.setGeometry(QtCore.QRect(130, 80, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_nameNum.setFont(font)
        self.user_nameNum.setObjectName("user_nameNum")
        self.label_18 = QtWidgets.QLabel(self.tab_userData)
        self.label_18.setGeometry(QtCore.QRect(20, 200, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.user_apMax = QtWidgets.QSpinBox(self.tab_userData)
        self.user_apMax.setGeometry(QtCore.QRect(130, 170, 91, 22))
        self.user_apMax.setMaximum(135)
        self.user_apMax.setProperty("value", 135)
        self.user_apMax.setObjectName("user_apMax")
        self.groupBox_secretary = QtWidgets.QGroupBox(self.tab_userData)
        self.groupBox_secretary.setGeometry(QtCore.QRect(240, 160, 231, 71))
        self.groupBox_secretary.setObjectName("groupBox_secretary")
        self.user_secretarySkin = QtWidgets.QComboBox(self.groupBox_secretary)
        self.user_secretarySkin.setGeometry(QtCore.QRect(120, 40, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.user_secretarySkin.setFont(font)
        self.user_secretarySkin.setObjectName("user_secretarySkin")
        self.label_20 = QtWidgets.QLabel(self.groupBox_secretary)
        self.label_20.setGeometry(QtCore.QRect(120, 20, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.user_secretary = QtWidgets.QComboBox(self.groupBox_secretary)
        self.user_secretary.setGeometry(QtCore.QRect(5, 40, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.user_secretary.setFont(font)
        self.user_secretary.setObjectName("user_secretary")
        self.label_19 = QtWidgets.QLabel(self.groupBox_secretary)
        self.label_19.setGeometry(QtCore.QRect(5, 20, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_13 = QtWidgets.QLabel(self.tab_userData)
        self.label_13.setGeometry(QtCore.QRect(20, 50, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.user_UID = QtWidgets.QLineEdit(self.tab_userData)
        self.user_UID.setGeometry(QtCore.QRect(100, 20, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_UID.setFont(font)
        self.user_UID.setObjectName("user_UID")
        self.user_name = QtWidgets.QLineEdit(self.tab_userData)
        self.user_name.setGeometry(QtCore.QRect(100, 50, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_name.setFont(font)
        self.user_name.setObjectName("user_name")
        self.label_22 = QtWidgets.QLabel(self.tab_userData)
        self.label_22.setGeometry(QtCore.QRect(20, 110, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.user_ap = QtWidgets.QSpinBox(self.tab_userData)
        self.user_ap.setGeometry(QtCore.QRect(130, 140, 91, 22))
        self.user_ap.setMaximum(999999999)
        self.user_ap.setProperty("value", 135)
        self.user_ap.setObjectName("user_ap")
        self.label_17 = QtWidgets.QLabel(self.tab_userData)
        self.label_17.setGeometry(QtCore.QRect(20, 170, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.user_resume = QtWidgets.QLineEdit(self.tab_userData)
        self.user_resume.setGeometry(QtCore.QRect(70, 200, 151, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_resume.setFont(font)
        self.user_resume.setObjectName("user_resume")
        self.label_15 = QtWidgets.QLabel(self.tab_userData)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.user_Lv = QtWidgets.QSpinBox(self.tab_userData)
        self.user_Lv.setGeometry(QtCore.QRect(130, 110, 91, 22))
        self.user_Lv.setMinimum(1)
        self.user_Lv.setMaximum(120)
        self.user_Lv.setProperty("value", 120)
        self.user_Lv.setObjectName("user_Lv")
        self.label_7 = QtWidgets.QLabel(self.tab_userData)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 321, 16))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_userData, "")
        self.tab_charData = QtWidgets.QWidget()
        self.tab_charData.setObjectName("tab_charData")
        self.groupBox_addChar = QtWidgets.QGroupBox(self.tab_charData)
        self.groupBox_addChar.setGeometry(QtCore.QRect(10, 270, 361, 91))
        self.groupBox_addChar.setObjectName("groupBox_addChar")
        self.checkBox_addBest = QtWidgets.QCheckBox(self.groupBox_addChar)
        self.checkBox_addBest.setGeometry(QtCore.QRect(160, 20, 61, 22))
        self.checkBox_addBest.setObjectName("checkBox_addBest")
        self.comboBox_addChar = QtWidgets.QComboBox(self.groupBox_addChar)
        self.comboBox_addChar.setGeometry(QtCore.QRect(10, 20, 121, 22))
        self.comboBox_addChar.setObjectName("comboBox_addChar")
        self.pushButton_addChar = QtWidgets.QPushButton(self.groupBox_addChar)
        self.pushButton_addChar.setGeometry(QtCore.QRect(10, 50, 121, 28))
        self.pushButton_addChar.setObjectName("pushButton_addChar")
        self.checkBox_customChar = QtWidgets.QCheckBox(self.groupBox_addChar)
        self.checkBox_customChar.setGeometry(QtCore.QRect(240, 20, 111, 22))
        self.checkBox_customChar.setObjectName("checkBox_customChar")
        self.pushButton_addAllChar = QtWidgets.QPushButton(self.groupBox_addChar)
        self.pushButton_addAllChar.setGeometry(QtCore.QRect(240, 50, 111, 28))
        self.pushButton_addAllChar.setObjectName("pushButton_addAllChar")
        self.pushButton_clearChar = QtWidgets.QPushButton(self.groupBox_addChar)
        self.pushButton_clearChar.setGeometry(QtCore.QRect(160, 50, 51, 28))
        self.pushButton_clearChar.setObjectName("pushButton_clearChar")
        self.groupBox_customChar = QtWidgets.QGroupBox(self.tab_charData)
        self.groupBox_customChar.setEnabled(False)
        self.groupBox_customChar.setGeometry(QtCore.QRect(470, 10, 231, 351))
        self.groupBox_customChar.setObjectName("groupBox_customChar")
        self.frame_editChar = QtWidgets.QFrame(self.groupBox_customChar)
        self.frame_editChar.setGeometry(QtCore.QRect(10, 50, 211, 251))
        self.frame_editChar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_editChar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_editChar.setObjectName("frame_editChar")
        self.label_10 = QtWidgets.QLabel(self.frame_editChar)
        self.label_10.setGeometry(QtCore.QRect(10, 220, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.frame_editChar)
        self.label_9.setGeometry(QtCore.QRect(166, 160, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.char_skillLv = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_skillLv.setGeometry(QtCore.QRect(160, 130, 42, 22))
        self.char_skillLv.setMinimum(1)
        self.char_skillLv.setMaximum(7)
        self.char_skillLv.setObjectName("char_skillLv")
        self.label_2 = QtWidgets.QLabel(self.frame_editChar)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.char_eliteLv = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_eliteLv.setGeometry(QtCore.QRect(60, 40, 41, 22))
        self.char_eliteLv.setMaximum(2)
        self.char_eliteLv.setObjectName("char_eliteLv")
        self.char_favorPoint = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_favorPoint.setGeometry(QtCore.QRect(151, 100, 51, 22))
        self.char_favorPoint.setMaximum(200)
        self.char_favorPoint.setObjectName("char_favorPoint")
        self.label_5 = QtWidgets.QLabel(self.frame_editChar)
        self.label_5.setGeometry(QtCore.QRect(101, 40, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.frame_editChar)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.frame_editChar)
        self.label.setGeometry(QtCore.QRect(10, 100, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.frame_editChar)
        self.label_8.setGeometry(QtCore.QRect(10, 160, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.char_skin = QtWidgets.QComboBox(self.frame_editChar)
        self.char_skin.setGeometry(QtCore.QRect(71, 70, 131, 22))
        self.char_skin.setObjectName("char_skin")
        self.char_skillIndex = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_skillIndex.setGeometry(QtCore.QRect(121, 160, 42, 22))
        self.char_skillIndex.setMinimum(1)
        self.char_skillIndex.setMaximum(3)
        self.char_skillIndex.setObjectName("char_skillIndex")
        self.char_potLv = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_potLv.setGeometry(QtCore.QRect(160, 220, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.char_potLv.setFont(font)
        self.char_potLv.setMaximum(5)
        self.char_potLv.setObjectName("char_potLv")
        self.char_Lv = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_Lv.setGeometry(QtCore.QRect(161, 40, 41, 22))
        self.char_Lv.setMinimum(1)
        self.char_Lv.setMaximum(80)
        self.char_Lv.setObjectName("char_Lv")
        self.label_6 = QtWidgets.QLabel(self.frame_editChar)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.frame_editChar)
        self.label_11.setGeometry(QtCore.QRect(10, 190, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.char_spLv = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_spLv.setGeometry(QtCore.QRect(160, 190, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.char_spLv.setFont(font)
        self.char_spLv.setMaximum(3)
        self.char_spLv.setObjectName("char_spLv")
        self.checkBox_customBest = QtWidgets.QCheckBox(self.groupBox_customChar)
        self.checkBox_customBest.setGeometry(QtCore.QRect(20, 310, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_customBest.setFont(font)
        self.checkBox_customBest.setObjectName("checkBox_customBest")
        self.label_selectChar = QtWidgets.QLabel(self.groupBox_customChar)
        self.label_selectChar.setGeometry(QtCore.QRect(50, 20, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_selectChar.setFont(font)
        self.label_selectChar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_selectChar.setObjectName("label_selectChar")
        self.pushButton_charEdit = QtWidgets.QPushButton(self.groupBox_customChar)
        self.pushButton_charEdit.setGeometry(QtCore.QRect(130, 310, 93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_charEdit.setFont(font)
        self.pushButton_charEdit.setObjectName("pushButton_charEdit")
        self.comboBox_editChar = QtWidgets.QComboBox(self.groupBox_customChar)
        self.comboBox_editChar.setGeometry(QtCore.QRect(90, 50, 121, 22))
        self.comboBox_editChar.setObjectName("comboBox_editChar")
        self.label_23 = QtWidgets.QLabel(self.groupBox_customChar)
        self.label_23.setGeometry(QtCore.QRect(20, 50, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.table_char = QtWidgets.QTableWidget(self.tab_charData)
        self.table_char.setGeometry(QtCore.QRect(10, 20, 441, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_char.setFont(font)
        self.table_char.setObjectName("table_char")
        self.table_char.setColumnCount(11)
        self.table_char.setRowCount(0)
        self.table_char.setSelectionMode(QAbstractItemView.MultiSelection)
        self.table_char.setEditTriggers(QTableView.NoEditTriggers)
        self.table_char.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_char.horizontalHeader().setVisible(True)
        self.table_char.horizontalHeader().setCascadingSectionResizes(False)
        self.table_char.horizontalHeader().setDefaultSectionSize(75)
        self.table_char.horizontalHeader().setSortIndicatorShown(False)
        self.table_char.horizontalHeader().setStretchLastSection(False)
        self.table_char.verticalHeader().setCascadingSectionResizes(False)
        self.table_char.verticalHeader().setSortIndicatorShown(False)
        self.table_char.verticalHeader().setStretchLastSection(False)
        self.checkBox_selectInv = QtWidgets.QCheckBox(self.tab_charData)
        self.checkBox_selectInv.setGeometry(QtCore.QRect(390, 325, 61, 22))
        self.checkBox_selectInv.setObjectName("checkBox_selectInv")
        self.checkBox_selectAll = QtWidgets.QCheckBox(self.tab_charData)
        self.checkBox_selectAll.setGeometry(QtCore.QRect(390, 290, 61, 22))
        self.checkBox_selectAll.setObjectName("checkBox_selectAll")
        self.tabWidget.addTab(self.tab_charData, "")
        self.tab_squad = QtWidgets.QWidget()
        self.tab_squad.setObjectName("tab_squad")
        self.groupBox_customChar_squad = QtWidgets.QGroupBox(self.tab_squad)
        self.groupBox_customChar_squad.setEnabled(False)
        self.groupBox_customChar_squad.setGeometry(QtCore.QRect(360, 60, 231, 151))
        self.groupBox_customChar_squad.setObjectName("groupBox_customChar_squad")
        self.checkBox_customBest_squad = QtWidgets.QCheckBox(self.groupBox_customChar_squad)
        self.checkBox_customBest_squad.setGeometry(QtCore.QRect(20, 110, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_customBest_squad.setFont(font)
        self.checkBox_customBest_squad.setObjectName("checkBox_customBest_squad")
        self.label_selectChar_squad = QtWidgets.QLabel(self.groupBox_customChar_squad)
        self.label_selectChar_squad.setGeometry(QtCore.QRect(50, 20, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_selectChar_squad.setFont(font)
        self.label_selectChar_squad.setAlignment(QtCore.Qt.AlignCenter)
        self.label_selectChar_squad.setObjectName("label_selectChar_squad")
        self.pushButton_charEdit_squad = QtWidgets.QPushButton(self.groupBox_customChar_squad)
        self.pushButton_charEdit_squad.setGeometry(QtCore.QRect(130, 110, 93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_charEdit_squad.setFont(font)
        self.pushButton_charEdit_squad.setObjectName("pushButton_charEdit_squad")
        self.label_38 = QtWidgets.QLabel(self.groupBox_customChar_squad)
        self.label_38.setGeometry(QtCore.QRect(20, 50, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.char_skillIndex_squad = QtWidgets.QSpinBox(self.groupBox_customChar_squad)
        self.char_skillIndex_squad.setGeometry(QtCore.QRect(130, 80, 42, 22))
        self.char_skillIndex_squad.setMinimum(1)
        self.char_skillIndex_squad.setMaximum(3)
        self.char_skillIndex_squad.setObjectName("char_skillIndex_squad")
        self.label_32 = QtWidgets.QLabel(self.groupBox_customChar_squad)
        self.label_32.setGeometry(QtCore.QRect(175, 80, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_36 = QtWidgets.QLabel(self.groupBox_customChar_squad)
        self.label_36.setGeometry(QtCore.QRect(20, 80, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.customChar_squad = QtWidgets.QComboBox(self.groupBox_customChar_squad)
        self.customChar_squad.setGeometry(QtCore.QRect(100, 50, 121, 22))
        self.customChar_squad.setObjectName("customChar_squad")
        self.table_squad = QtWidgets.QTableWidget(self.tab_squad)
        self.table_squad.setGeometry(QtCore.QRect(10, 20, 331, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_squad.setFont(font)
        self.table_squad.setObjectName("table_squad")
        self.table_squad.setColumnCount(4)
        self.table_squad.setRowCount(12)
        self.table_squad.setSelectionMode(QAbstractItemView.SingleSelection)  
        self.table_squad.setEditTriggers(QTableView.NoEditTriggers)
        self.table_squad.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_squad.horizontalHeader().setVisible(True)
        self.table_squad.horizontalHeader().setCascadingSectionResizes(False)
        self.table_squad.horizontalHeader().setDefaultSectionSize(75)
        self.table_squad.horizontalHeader().setSortIndicatorShown(False)
        self.table_squad.horizontalHeader().setStretchLastSection(False)
        self.table_squad.verticalHeader().setCascadingSectionResizes(False)
        self.table_squad.verticalHeader().setSortIndicatorShown(False)
        self.table_squad.verticalHeader().setStretchLastSection(False)
        self.label_37 = QtWidgets.QLabel(self.tab_squad)
        self.label_37.setGeometry(QtCore.QRect(370, 30, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.currSquad = QtWidgets.QComboBox(self.tab_squad)
        self.currSquad.setGeometry(QtCore.QRect(470, 30, 121, 22))
        self.currSquad.setObjectName("currSquad")
        self.label_12 = QtWidgets.QLabel(self.tab_squad)
        self.label_12.setGeometry(QtCore.QRect(10, 230, 451, 81))
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab_squad, "")
        self.tab_start = QtWidgets.QWidget()
        self.tab_start.setObjectName("tab_start")
        self.log_browser = QtWidgets.QTextBrowser(self.tab_start)
        self.log_browser.setGeometry(QtCore.QRect(178, 0, 541, 381))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.log_browser.setFont(font)
        self.log_browser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.log_browser.setObjectName("log_browser")
        self.groupBox_porxy = QtWidgets.QGroupBox(self.tab_start)
        self.groupBox_porxy.setGeometry(QtCore.QRect(10, 10, 161, 59))
        self.groupBox_porxy.setObjectName("groupBox_porxy")
        self.gob_porxy = QtWidgets.QSpinBox(self.groupBox_porxy)
        self.gob_porxy.setGeometry(QtCore.QRect(70, 30, 81, 22))
        self.gob_porxy.setMaximum(65535)
        self.gob_porxy.setProperty("value", 12450)
        self.gob_porxy.setObjectName("gob_porxy")
        self.label_21 = QtWidgets.QLabel(self.groupBox_porxy)
        self.label_21.setGeometry(QtCore.QRect(10, 30, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.pushButton_run = QtWidgets.QPushButton(self.tab_start)
        self.pushButton_run.setGeometry(QtCore.QRect(40, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setObjectName("pushButton_run")
        self.checkBox_fcm = QtWidgets.QCheckBox(self.tab_start)
        self.checkBox_fcm.setGeometry(QtCore.QRect(20, 80, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_fcm.setFont(font)
        self.checkBox_fcm.setObjectName("checkBox_fcm")
        self.tabWidget.addTab(self.tab_start, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 30))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")

        self.debug = QtWidgets.QMenu(self.menubar)
        self.debug.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.debug.setToolTipDuration(5)
        self.debug.setToolTipsVisible(False)
        self.debug.setObjectName("debug")
        self.action_debug = QAction(MainWindow)
        self.action_debug.setCheckable(False)
        self.action_debug.setObjectName('debugAction')
        self.action_debug.setText('Debug模式')
        
        self.about = QtWidgets.QMenu(self.menubar)
        self.about.setObjectName("about")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.onLabel=QLabel('')
        self.statusBar.addPermanentWidget(self.onLabel, stretch=0)
        self.action_import = QtWidgets.QAction(MainWindow)
        self.action_import.setObjectName("action_import")
        self.action_export = QtWidgets.QAction(MainWindow)
        self.action_export.setObjectName("action_export")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.action_notice = QtWidgets.QAction(MainWindow)
        self.action_notice.setObjectName("action_notice")
        self.file.addAction(self.action_import)
        self.file.addAction(self.action_export)
        self.file.addSeparator()
        self.file.addAction(self.action_exit)
        self.about.addAction(self.action_help)
        self.about.addSeparator()
        self.about.addAction(self.action_notice)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.action_debug)
        self.menubar.addAction(self.about.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.user_UID, self.user_name)
        MainWindow.setTabOrder(self.user_name, self.user_nameNum)
        MainWindow.setTabOrder(self.user_nameNum, self.user_Lv)
        MainWindow.setTabOrder(self.user_Lv, self.user_ap)
        MainWindow.setTabOrder(self.user_ap, self.user_apMax)
        MainWindow.setTabOrder(self.user_apMax, self.user_resume)
        MainWindow.setTabOrder(self.user_resume, self.user_secretary)
        MainWindow.setTabOrder(self.user_secretary, self.user_secretarySkin)
        MainWindow.setTabOrder(self.user_secretarySkin, self.list_item)
        MainWindow.setTabOrder(self.list_item, self.item_value)
        MainWindow.setTabOrder(self.item_value, self.pushButton_itemEdit)
        MainWindow.setTabOrder(self.pushButton_itemEdit, self.gob_porxy)
        MainWindow.setTabOrder(self.gob_porxy, self.table_char)
        MainWindow.setTabOrder(self.table_char, self.comboBox_addChar)
        MainWindow.setTabOrder(self.comboBox_addChar, self.checkBox_addBest)
        MainWindow.setTabOrder(self.checkBox_addBest, self.pushButton_addChar)
        MainWindow.setTabOrder(self.pushButton_addChar, self.checkBox_customChar)
        MainWindow.setTabOrder(self.checkBox_customChar, self.pushButton_addAllChar)
        MainWindow.setTabOrder(self.pushButton_addAllChar, self.char_eliteLv)
        MainWindow.setTabOrder(self.char_eliteLv, self.char_Lv)
        MainWindow.setTabOrder(self.char_Lv, self.char_skin)
        MainWindow.setTabOrder(self.char_skin, self.char_favorPoint)
        MainWindow.setTabOrder(self.char_favorPoint, self.char_skillLv)
        MainWindow.setTabOrder(self.char_skillLv, self.char_skillIndex)
        MainWindow.setTabOrder(self.char_skillIndex, self.char_spLv)
        MainWindow.setTabOrder(self.char_spLv, self.char_potLv)
        MainWindow.setTabOrder(self.char_potLv, self.checkBox_customBest)
        MainWindow.setTabOrder(self.checkBox_customBest, self.pushButton_charEdit)
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ArknightsCheater"))
        self.textBrowser_init.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">此破解方法在安卓7.0以上中受限制(iOS安装描述文件后全版本都可以)，如果你是安卓7.0以上，请参考:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">解决方法1：使用安卓7.0以下版本的手机。</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">解决方式2：Root手机，安装 Xposed + JustTrustMe。</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">解决方式3：不Root，使用 VirtualXposed、太极等 + JustTrustMe。或使用安卓内模拟器 如:VMOS等。</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请在手机或模拟器中完成以下配置：</p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">确保手机或模拟器和电脑在同一局域网下。</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">进入手机或模拟器WLAN(Wi-Fi)设置配置手机代理。<br />安卓：修改网络—高级选项—代理—手动<br />iOS：HTTP代理—配置代理—手动<br />将服务器和端口设置为mitmproxy所监听的主机ip和端口。<br />保存/储存</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">右侧配置设置并点击启动</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">进入网站 http://mitm.it 下载证书(iOS为描述文件)并安装。<br />iOS多一步：设置—通用—关于本机—证书信任设置—mitmproxy—打开</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">重新进入游戏。</li></ol></body></html>"))
        self.pushButton_run_init.setText(_translate("MainWindow", "启动"))
        self.groupBox_porxy_init.setTitle(_translate("MainWindow", "代理设置"))
        self.label_33.setText(_translate("MainWindow", "端口:"))
        self.inInitInfo.setText(_translate("MainWindow", "启动mitmproxy中..."))
        self.pushButton_initSkip.setText(_translate("MainWindow", "跳过/高级修改"))
        self.label_3.setText(_translate("MainWindow", "启动游戏以初始化"))
        self.pushButton_initCTN.setText(_translate("MainWindow", "继续"))
        self.pushButton_initSkip_2.setText(_translate("MainWindow", "跳过/高级修改"))
        self.checkBox_fcm_init.setText(_translate("MainWindow", "防沉迷破解"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "初始化"))
        self.groupBox_item.setTitle(_translate("MainWindow", "物品"))
        __sortingEnabled = self.list_item.isSortingEnabled()
        self.list_item.setSortingEnabled(False)
        item = self.list_item.item(0)
        item.setText(_translate("MainWindow", "龙门币"))
        item = self.list_item.item(1)
        item.setText(_translate("MainWindow", "合成玉"))
        item = self.list_item.item(2)
        item.setText(_translate("MainWindow", "安卓源石"))
        item = self.list_item.item(3)
        item.setText(_translate("MainWindow", "iOS源石"))
        item = self.list_item.item(4)
        item.setText(_translate("MainWindow", "演习券"))
        item = self.list_item.item(5)
        item.setText(_translate("MainWindow", "资深凭证"))
        item = self.list_item.item(6)
        item.setText(_translate("MainWindow", "高级凭证"))
        item = self.list_item.item(7)
        item.setText(_translate("MainWindow", "寻访凭证"))
        item = self.list_item.item(8)
        item.setText(_translate("MainWindow", "十连寻访凭证"))
        self.list_item.setSortingEnabled(__sortingEnabled)
        self.pushButton_itemEdit.setText(_translate("MainWindow", "修改"))
        self.label_14.setText(_translate("MainWindow", "昵称编号:"))
        self.label_16.setText(_translate("MainWindow", "理智:"))
        self.user_nameNum.setPlaceholderText(_translate("MainWindow", "8888"))
        self.label_18.setText(_translate("MainWindow", "签名:"))
        self.groupBox_secretary.setTitle(_translate("MainWindow", "助理"))
        self.label_20.setText(_translate("MainWindow", "助理皮肤:"))
        self.label_19.setText(_translate("MainWindow", "助理:"))
        self.label_13.setText(_translate("MainWindow", "昵称:"))
        self.user_UID.setPlaceholderText(_translate("MainWindow", "8888888"))
        self.user_name.setPlaceholderText(_translate("MainWindow", "破解用户"))
        self.label_22.setText(_translate("MainWindow", "等级:"))
        self.label_17.setText(_translate("MainWindow", "理智上限:"))
        self.user_resume.setPlaceholderText(_translate("MainWindow", "Ta什么都没有留下"))
        self.label_15.setText(_translate("MainWindow", "UID:"))
        self.label_7.setText(_translate("MainWindow", "警告:对以上数据的修改可能导致游戏崩溃"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_userData), _translate("MainWindow", "用户数据"))
        self.groupBox_addChar.setTitle(_translate("MainWindow", "添加干员"))
        self.checkBox_addBest.setText(_translate("MainWindow", "最好"))
        self.pushButton_addChar.setText(_translate("MainWindow", "添加干员"))
        self.checkBox_customChar.setText(_translate("MainWindow", "自定义干员"))
        self.pushButton_addAllChar.setText(_translate("MainWindow", "添加所有干员"))
        self.pushButton_clearChar.setText(_translate("MainWindow", "清空"))
        self.checkBox_selectAll.setText(_translate("MainWindow", "全选"))
        self.checkBox_selectInv.setText(_translate("MainWindow", "反选"))
        self.groupBox_customChar.setTitle(_translate("MainWindow", "自定义干员"))
        self.label_10.setText(_translate("MainWindow", "潜能等级:"))
        self.label_9.setText(_translate("MainWindow", "技能"))
        self.label_2.setText(_translate("MainWindow", "皮肤:"))
        self.label_5.setText(_translate("MainWindow", " 等级:"))
        self.label_4.setText(_translate("MainWindow", "精英:"))
        self.label.setText(_translate("MainWindow", "信赖值:"))
        self.label_8.setText(_translate("MainWindow", "选中技能:"))
        self.label_6.setText(_translate("MainWindow", "技能等级:"))
        self.label_11.setText(_translate("MainWindow", "技能专精等级:"))
        self.label_23.setText(_translate("MainWindow", "修改为:"))
        self.checkBox_customBest.setText(_translate("MainWindow", "最好"))
        self.label_selectChar.setText(_translate("MainWindow", "请选择干员"))
        self.pushButton_charEdit.setText(_translate("MainWindow", "修改"))
        self.table_char.setHorizontalHeaderLabels(['干员','ID','精英','等级','皮肤','信赖值','技能等级','选中技能','专精等级','潜能等级','操作'])
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_charData), _translate("MainWindow", "干员数据"))
        self.groupBox_customChar_squad.setTitle(_translate("MainWindow", "自定义编队"))
        self.checkBox_customBest_squad.setText(_translate("MainWindow", "最好"))
        self.label_selectChar_squad.setText(_translate("MainWindow", "请选择干员"))
        self.pushButton_charEdit_squad.setText(_translate("MainWindow", "修改"))
        self.label_38.setText(_translate("MainWindow", "修改为:"))
        self.label_32.setText(_translate("MainWindow", "技能"))
        self.label_36.setText(_translate("MainWindow", "选中技能:"))
        self.table_squad.setHorizontalHeaderLabels(['干员','装载ID','选中技能','最大技能'])
        self.label_37.setText(_translate("MainWindow", "当前编队:"))
        self.label_12.setText(_translate("MainWindow", "注:编队中不能出现相同装载ID的干员,且装载ID不能大于所拥有的干员数；修改编队后，需要手动在游戏主界面编队选中编队中某一干员，随便修改其技能并且返回到主界面来达到修改效果。"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_squad), _translate("MainWindow", "编队数据"))
        self.log_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:8pt; font-weight:400; font-style:normal;\" bgcolor=\"#293134\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.groupBox_porxy.setTitle(_translate("MainWindow", "代理设置"))
        self.label_21.setText(_translate("MainWindow", "端口:"))
        self.pushButton_run.setText(_translate("MainWindow", "启动"))
        self.checkBox_fcm.setText(_translate("MainWindow", "防沉迷破解"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_start), _translate("MainWindow", "启动"))
        self.file.setTitle(_translate("MainWindow", "文件"))
        self.about.setTitle(_translate("MainWindow", "关于"))
        self.action_import.setText(_translate("MainWindow", "导入配置"))
        self.action_export.setText(_translate("MainWindow", "导出配置"))
        self.action_exit.setText(_translate("MainWindow", "退出"))
        self.action_help.setText(_translate("MainWindow", "如何使用"))
        self.action_notice.setText(_translate("MainWindow", "用户须知"))

#define
def skintable2list(skin_table_path):
    skin = json.loads(open(skin_table_path, 'r', encoding='UTF-8').read())
    skinInner=[]
    for e,skinId in enumerate(skin['charSkins']):
        if skinId[:4]=='char' and not skinId in skinInner:
            skinInner.append(skin['charSkins'][skinId]['charId']+'":"')
    j=json.loads(str(skinInner).replace('\'','"').replace(']','}]').replace('[','[{').replace('""','{}')[1:-1])
    for e,skinId in enumerate(skin['charSkins']):
        if skinId[:4]=='char':
            charId=skin['charSkins'][skinId]['charId']
            skinname=skin['charSkins'][skinId]['displaySkin']['skinGroupName']
            if skinId==charId+'#2':
                skinname='精二服装'
            elif skinId == charId+'#1+':
                skinname='精一服装'
            if str(j[charId])=='{}':
                j[charId]='{\''+skinId+'\':\''+skinname+'\'}'
            else:
                j[charId]=j[charId][:-1]+',\''+skinId+'\':\''+skinname+'\'}'
    return str(j).replace('"','').replace('\'','"')

def getCustomChar(charId,charNum,eliteLv,lv,skin,favPt,skillLv,skillIndex,spLv,potLv):
    skills = charTable[charId]['skills']
    modSkillPath = [{
    'skillId': '',
    'unlock': 1,
    'state': 0,
    'specializeLevel': spLv,
    'completeUpgradeTime': -1
    }]
    if len(skills) == 0:
        modSkill = []
    else:
        modSkillTemp=json.dumps(modSkillPath)[1:-1]
        modSkillPath=json.dumps(modSkillPath)[1:-1]
        for num in range(1,len(skills)):
            modSkillPath=modSkillPath+','+modSkillTemp
        modSkill = json.loads('['+modSkillPath+']') 
        for e in range(0,len(skills)):
            modSkill[e]['skillId'] = charTable[charId]['skills'][e]['skillId']
    CustomChar = {str(charNum):{
    'instId':charNum,
    'charId':charId,
    'favorPoint':favorPointList[favPt],
    'potentialRank':potLv,
    'mainSkillLvl':skillLv,
    'skin':skin,
    'level':lv,
    'exp':0,
    'evolvePhase':eliteLv,
    'defaultSkillIndex':skillIndex,
    'gainTime':1556654400,
    'skills':modSkill}
    }
    return CustomChar

def table_char_selectChanged():
    first=True
    global indexList,char_isMultiSelect
    indexList=[]
    for index in Win.table_char.selectedIndexes():
        if first:
            lastIndex=index.row()
            first=False
            indexList.append(index.row())
        if not lastIndex==index.row():
            indexList.append(index.row())
        lastIndex=index.row()
    if not len(indexList)==0:
        if len(indexList)==1:
            index=Win.table_char.currentIndex().row()
            charId=charList[int(Win.table_char.item(index, 1).text())]
            Win.char_skin.clear()
            for e,skinId in enumerate(skinList[charId]):
                    Win.char_skin.addItem(skinList[charId][skinId])
            if Win.checkBox_customBest.isChecked():
                    Win.checkBox_customBest.setChecked(False)
            customChar_reload(index)
            char_eliteLv_changed()
        else:
            char_isMultiSelect=True
            mulitEditChar_selectChanged()

def mulitEditChar_selectChanged():
    index=Win.table_char.currentIndex().row()
    charId=charList[index]
    Win.label_selectChar.setText('多选')
    Win.char_skin.clear()
    for e,skinId in enumerate(skinList[charId]):
        Win.char_skin.addItem(skinList[charId][skinId])
    if DebugOff:
        Win.char_eliteLv.setMaximum(2)
        Win.char_Lv.setMaximum(90)
        Win.char_skillIndex.setEnabled(True)
        Win.char_skillIndex.setMaximum(3)

def table_squad_selectChanged():
    index=Win.table_squad.currentIndex().row()
    Win.groupBox_customChar_squad.setEnabled(True)
    if Win.table_squad.item(index, 0).text()=='无':
        Win.groupBox_customChar_squad.setEnabled(False)
        Win.label_selectChar_squad.setText('无')
    else:
        customSquads_reload(index)

def customSquads_reload(index):
    Win.label_selectChar_squad.setText(Win.table_squad.item(index, 0).text())
    charIn=int(Win.table_squad.item(index, 1).text())
    charIndex=0
    for e in charTable:
        if charTable[e]['name']==Win.table_squad.item(index, 0).text():
            charIndex=charList.index(e)
            break
    skillIn = Win.table_squad.item(index, 2).text()
    bestCharList=bestChar(charIndex)

    if skillIn in ['1','2','3']:
        maxSkillIndex=Win.table_squad.item(index, 3).text()
        Win.char_skillIndex_squad.setMaximum(int(maxSkillIndex))
        if Win.checkBox_customBest_squad.isChecked():
            Win.char_skillIndex_squad.setEnabled(False)
            Win.char_skillIndex_squad.setValue(int(maxSkillIndex))
        else:
            Win.char_skillIndex_squad.setEnabled(True)
            Win.char_skillIndex_squad.setValue(int(skillIn))
    else:
        Win.char_skillIndex_squad.setEnabled(False)

def customChar_reload(index):
    charIndex=int(Win.table_char.item(index, 1).text())
    charId=charList[charIndex]
    rarity=charTable[charId]['rarity']
    Win.label_selectChar.setText(charTable[charId]['name'])
    bestCharList=bestChar(charIndex)
    if DebugOff:
        Win.char_eliteLv.setMaximum(bestCharList[2])
        Win.char_Lv.setMaximum(bestCharList[3])
    Win.char_eliteLv.setValue(int(Win.table_char.item(index, 2).text()))
    Win.char_Lv.setValue(int(Win.table_char.item(index, 3).text()))
    for e,skinId in enumerate(skinList[charId]):
        if Win.table_char.item(index, 4).text()==skinList[charId][skinId]:
            Win.char_skin.setCurrentIndex(e)
    Win.char_favorPoint.setValue(int(Win.table_char.item(index, 5).text()))
    Win.char_skillLv.setValue(int(Win.table_char.item(index, 6).text()))
    skillIn = Win.table_char.item(index, 7).text()
    if skillIn in ['1','2','3']:
        Win.char_skillIndex.setEnabled(True)
        Win.char_skillIndex.setMaximum(int(bestCharList[7]))
        Win.char_skillIndex.setValue(int(skillIn))
    else:
        Win.char_skillIndex.setEnabled(False)
    Win.char_spLv.setValue(int(Win.table_char.item(index, 8).text()))
    Win.char_potLv.setValue(int(Win.table_char.item(index, 9).text()))

def userSecretary_changed():
    Win.user_secretarySkin.clear()
    charId=charList[Win.user_secretary.currentIndex()]
    for e,skinId in enumerate(skinList[charId]):
        Win.user_secretarySkin.addItem(skinList[charId][skinId])
        
def checkBoxCustomChar_changed():
    if Win.checkBox_customChar.isChecked():
        Win.groupBox_customChar.setEnabled(True)
    else:
        Win.groupBox_customChar.setEnabled(False)

def checkBoxCustomBest_changed():
    if Win.checkBox_customBest.isChecked():
        customChar_setBest()
        Win.frame_editChar.setEnabled(False)
    else:
        Win.frame_editChar.setEnabled(True)

def customChar_setBest():
    if not checkSelectChar():
        return
    index=Win.table_char.currentIndex().row()
    if Win.comboBox_editChar.currentIndex()==0:
        charIndex=int(Win.table_char.item(index, 1).text())
    else:
        charIndex=Win.comboBox_editChar.currentIndex()-1
    charId=charList[charIndex]
    bestCharList=bestChar(charIndex)
    Win.char_eliteLv.setMaximum(bestCharList[2])
    Win.char_eliteLv.setValue(bestCharList[2])
    Win.char_Lv.setMaximum(bestCharList[3])
    Win.char_Lv.setValue(bestCharList[3])
    for e,skinId in enumerate(skinList[charId]):
        if bestCharList[4]==skinList[charId][skinId]:
            Win.char_skin.setCurrentIndex(e)
    Win.char_favorPoint.setValue(bestCharList[5])
    skillIn=bestCharList[6]
    if skillIn in ['1','2','3']:
        Win.char_skillIndex.setEnabled(True)
        Win.char_skillIndex.setMaximum(int(bestCharList[7]))
        Win.char_skillIndex.setValue(int(bestCharList[7]))
    else:
        Win.char_skillIndex.setEnabled(False)
    Win.char_spLv.setValue(bestCharList[8])
    Win.char_potLv.setValue(bestCharList[9])

def debug():
    global DebugOff
    if DebugOff:
        DebugOff=False
        Win.user_Lv.setMaximum(999999999)
        Win.user_apMax.setMaximum(999999999)
        Win.char_eliteLv.setMaximum(999999999)
        Win.char_Lv.setMaximum(999999999)
        Win.char_skillLv.setMaximum(999999999)
        Win.char_spLv.setMaximum(999999999)
        Win.char_potLv.setMaximum(999999999)
        Win.action_debug.setText('关闭Debug模式')
    else:
        DebugOff=True
        Win.user_Lv.setMaximum(120)
        Win.user_apMax.setMaximum(135)
        Win.char_skillLv.setMaximum(7)
        Win.char_eliteLv.setMaximum(2)
        charIndex=Win.table_char.currentIndex().row()
        if charIndex!=-1:
            Win.char_eliteLv.setValue(bestChar(charIndex)[2])
            char_lv_reload()
        Win.char_spLv.setMaximum(3)
        Win.char_potLv.setMaximum(5)
        Win.action_debug.setText('Debug模式')

def run_and_exit():
    global isRun
    if isRun:
        isRun=False
        Win.pushButton_run.setText('停止')
        f=open('.\data.acdata', 'w', encoding='UTF-8')
        f.write(get_data())
        f.close
        Win.log_browser.append('<font color="red">ArknightsCheater:启动mitmproxy中...</font>')
        Win.thread.start()
        Win.onLabel.setText('修改器端已在端口%s上开启'% (str(Win.gob_porxy.value())))
    else:
        isRun=True
        Win.pushButton_run.setText('启动')
        Win.thread.terminate()
        subprocess.Popen("taskkill /f /im mitmdump.exe>nul",shell=True)
        Win.log_browser.document().clear()
        Win.log_browser.setHtml("<html><head></head><body bgcolor=#293134></body></html>")
        Win.log_browser.append('<font color="#fff">用户停止操作</font>')
        Win.onLabel.setText('修改器端已关闭')

def get_data():
    global porxy
    global userUID,userName,userNameNum,userResume,squadsNm
    isFCM=Win.checkBox_fcm.isChecked()
    CustomCharTemp=''
    if not Win.user_UID.text()=='':
        userUID=Win.user_UID.text()
    if not Win.user_name.text()=='':
        userName=Win.user_name.text()
    if not Win.user_nameNum.text()=='':
        userNameNum=Win.user_nameNum.text()
    if not Win.user_resume.text()=='':
        userResume=Win.user_resume.text()
    
    cr_total=Win.table_char.rowCount()
    for index in range(0,cr_total):
        cr_charId=charList[int(Win.table_char.item(index, 1).text())]
        cr_eliteLv=int(Win.table_char.item(index, 2).text())
        cr_lv=int(Win.table_char.item(index, 3).text())
        for e,skinId in enumerate(skinList[cr_charId]):
            if Win.table_char.item(index, 4).text()==skinList[cr_charId][skinId]:
                cr_skinId=skinId
        cr_favPt=int(Win.table_char.item(index, 5).text())
        cr_skillLv=int(Win.table_char.item(index, 6).text())
        cr_skillIn = Win.table_char.item(index, 7).text()
        if cr_skillIn in ['1','2','3']:
            cr_skillIndex=int(cr_skillIn)-1
        else:
            cr_skillIndex=0
        cr_spLv = Win.table_char.item(index, 8).text()
        cr_potLv = Win.table_char.item(index, 9).text()
        if index == 0:
            CustomCharTemp = str(getCustomChar(cr_charId,index+1,cr_eliteLv,cr_lv,cr_skinId,cr_favPt,cr_skillLv,cr_skillIndex,cr_spLv,cr_potLv))[:-1]
        else:
            CustomCharTemp = CustomCharTemp+','+str(getCustomChar(cr_charId,index+1,cr_eliteLv,cr_lv,cr_skinId,cr_favPt,cr_skillLv,cr_skillIndex,cr_spLv,cr_potLv))[1:-1]
    if not cr_total==0:
        char=str(CustomCharTemp+'}').replace('\'','"')[1:-1]
    else:
        char=''
    secretaryCharId=charList[Win.user_secretary.currentIndex()]
    for e,skinId in enumerate(skinList[secretaryCharId]):
        if Win.user_secretarySkin.currentIndex()==e:
            secretarySkinId=skinId
    if len(squadsInfo)==0:
        squadsNm=''
    else:
        squadsInfoJ=json.loads(squadsInfo.replace('\'','"'))
        i=0
        for x,id in enumerate(squadsNm):
            for y in squadsNm[id]['slots']:
                if squadsInfoJ[i]['name']!='无':
                    if not squadsInfoJ[i]['skillIndex'] in ['1','2','3']:
                        skillIn=0
                    else:
                        skillIn=squadsInfoJ[i]['skillIndex']
                    newChar={'charInstId':int(squadsInfoJ[i]['charId']),
                            'skillIndex':int(skillIn)-1}
                    squadsNm[id]['slots'][i%12]=newChar
                i+=1
    data=[{
        'init':'false',
        'fcm':str(isFCM).lower(),
        'uid': userUID,
        'nickName': userName,
        'nickNumber': userNameNum,
        'level': Win.user_Lv.value(),
        'ap': Win.user_ap.value(),
        'maxAp': Win.user_apMax.value(),
        'resume': userResume,
        'secretary':secretaryCharId,
        'secretarySkinId':secretarySkinId,
        'item':item[0],
        'chars':{char},
        'squads':{str(squadsNm).replace('None','null')}
    }]
    return str(data).replace('{\'"','{"').replace('}\'}','}}').replace('\'','"').replace('""','').replace('{"{','{').replace('}"}','}').replace('"true"','true').replace('"false"','false')[1:-1]

def bestChar(index):
    charId=charList[index]
    name=charTable[charId]['name']
    rarity=charTable[charId]['rarity']
    favorPoint=200
    skillLv=7
    spLv=3
    potLv=5
    skin=skinList[charId][charId+'#1']
    skinLen=len(skinList[charId])
    skillIndex=len(charTable[charId]['skills'])
    if skillIndex==0:
        skillIndex='无技能'
    if rarity == 0:
        eliteLv=0
        Lv=30
    elif rarity == 1:
        eliteLv=0
        Lv=30
    elif rarity == 2:
        eliteLv=1
        Lv=55
    elif rarity == 3:
        eliteLv=2
        Lv=70
        if skinLen>=2:
            skin=skinList[charId][charId+'#2']
    elif rarity == 4:
        eliteLv=2
        Lv=80
        if skinLen>=2:
            skin=skinList[charId][charId+'#2']
    elif rarity == 5:
        eliteLv=2
        Lv=90
        if skinLen>=2:
            skin=skinList[charId][charId+'#2']
    return [name,index,eliteLv,Lv,skin,favorPoint,skillLv,skillIndex,spLv,potLv]
        
def addChar(index):
    global charTableEdit
    charTableEdit=True
    item=[]
    charId=charList[index]
    if Win.checkBox_addBest.isChecked():
        char=bestChar(index)
        for e in range(0,len(char)):
            item.append(str(char[e]))
        item.append('')
        addCharList(item)
    else:
        skillIndex=len(charTable[charId]['skills'])
        if skillIndex==0:
            skillIndex='无技能'
        else:
            skillIndex='1'
        addCharList([charTable[charId]['name'],index,'0','1','默认服装','0','1',skillIndex,'0','0',''])

def addCharList(item):
    global tableCharLine
    tableCharLine=tableCharLine+1
    Win.table_char.setRowCount(tableCharLine)
    for e in range(len(item)):
        if e == 10:
            table_char_del = QPushButton("删除")
            table_char_del.clicked.connect(lambda:table_char_del())
            table_char_del.setDown(True)
            table_char_del.setStyleSheet("QPushButton{margin:3px};")
            Win.table_char.setCellWidget(tableCharLine-1, e, table_char_del)
        else:
            Win.table_char.setItem(tableCharLine-1, e, QTableWidgetItem(str(item[e])))

def editCharMulitRow(row):
    if Win.comboBox_editChar.currentIndex()==0:
        charIn=int(Win.table_char.item(row, 1).text())
    else:
        charIn=Win.comboBox_editChar.currentIndex()-1
    charTableEdit=True
    if not checkSelectChar():
        return
    charIdIn=charList[charIn]
    bestCharList=bestChar(charIn)
    char_eliteLv=Win.char_eliteLv.value() if Win.char_eliteLv.value()<bestCharList[2] else bestCharList[2]
    char_Lv=Win.char_Lv.value() if Win.char_Lv.value()<bestCharList[3] else bestCharList[3]
    Win.table_char.setItem(row, 0, QTableWidgetItem(charTable[charList[charIn]]['name']))
    Win.table_char.setItem(row, 1, QTableWidgetItem(str(charIn)))
    Win.table_char.setItem(row, 2, QTableWidgetItem(str(char_eliteLv)))
    Win.table_char.setItem(row, 3, QTableWidgetItem(str(char_Lv)))
    for e,skinId in enumerate(skinList[charIdIn]):
        if Win.char_skin.currentIndex()==e:
            Win.table_char.setItem(row, 4, QTableWidgetItem(skinList[charIdIn][skinId]))
    Win.table_char.setItem(row, 5, QTableWidgetItem(str(Win.char_favorPoint.value())))
    Win.table_char.setItem(row, 6, QTableWidgetItem(str(Win.char_skillLv.value())))
    if not Win.table_char.item(row, 7).text()=='无技能':
        char_skillIndex=Win.char_skillIndex.value() if Win.char_skillIndex.value()<bestCharList[7] else bestCharList[7]
        Win.table_char.setItem(row, 7, QTableWidgetItem(str(char_skillIndex)))
    Win.table_char.setItem(row, 8, QTableWidgetItem(str(Win.char_spLv.value())))
    Win.table_char.setItem(row, 9, QTableWidgetItem(str(Win.char_potLv.value())))

def charEdit():
    global charTableEdit,char_isMultiSelect,indexList
    if not Win.table_char.rowCount()==0:
        charTableEdit=True
        if char_isMultiSelect:
            for index in indexList:
                editCharMulitRow(index)
        else:
            row=Win.table_char.currentIndex().row()
            if Win.comboBox_editChar.currentIndex()==0:
                charIn=int(Win.table_char.item(row, 1).text())
            else:
                charIn=Win.comboBox_editChar.currentIndex()-1
            if not checkSelectChar():
                return
            charIdIn=charList[charIn]
            Win.table_char.setItem(row, 0, QTableWidgetItem(charTable[charList[charIn]]['name']))
            Win.table_char.setItem(row, 1, QTableWidgetItem(str(charIn)))
            Win.table_char.setItem(row, 2, QTableWidgetItem(str(Win.char_eliteLv.value())))
            Win.table_char.setItem(row, 3, QTableWidgetItem(str(Win.char_Lv.value())))
            for e,skinId in enumerate(skinList[charIdIn]):
                if Win.char_skin.currentIndex()==e:
                    Win.table_char.setItem(row, 4, QTableWidgetItem(skinList[charIdIn][skinId]))
            Win.table_char.setItem(row, 5, QTableWidgetItem(str(Win.char_favorPoint.value())))
            Win.table_char.setItem(row, 6, QTableWidgetItem(str(Win.char_skillLv.value())))
            if not Win.table_char.item(row, 7).text()=='无技能':
                Win.table_char.setItem(row, 7, QTableWidgetItem(str(Win.char_skillIndex.value())))
            Win.table_char.setItem(row, 8, QTableWidgetItem(str(Win.char_spLv.value())))
            Win.table_char.setItem(row, 9, QTableWidgetItem(str(Win.char_potLv.value())))

def checkSelectChar():
    row=Win.table_char.currentIndex().row()
    if row==-1:
        QMessageBox.warning(Win,"错误","请选择干员",QMessageBox.Ok)
        return False
    else:
        return True

def charAddAll():
    table_char_delAll()
    charTableEdit=True
    for e in enumerate(charList):
        addChar(e[0])

def help():
    QMessageBox.about(Win,"如何使用","""
请在手机或模拟器中完成以下配置：
1.确保手机或模拟器和电脑在同一局域网下。
2.在游戏开始唤醒时进行以下操作，防止拦截游戏更新。
3.进入手机或模拟器WLAN(Wi-Fi)设置配置手机代理。
    安卓：修改网络--高级选项--代理--手动
    iOS：HTTP代理--配置代理--手动
        服务器(存在多个本机ip时，请输入和手机同一局域网的ip)：
        %s
        端口：%s
    保存/储存
4.进入网站http://mitm.it下载证书(iOS为描述文件)并安装。
    iOS多一步：设置--通用--关于本机--证书信任设置--mitmproxy--打开
5.重新进入游戏。
如果手机为安卓7.0及以上，请参考:
    方法1：使用安卓7.0以下版本的手机。
    方式2：Root手机，安装 Xposed + JustTrustMe。
    方式3：不Root，使用 VirtualXposed、太极等 + JustTrustMe。或将游戏安装到安卓内模拟器 如:VMOS等。
""" % (str(socket.gethostbyname_ex(socket.gethostname())[-1])[1:-1].replace('\'',''),Win.gob_porxy.value()))

def notice():
    QMessageBox.about(Win,"用户须知","""
本软件仅供个人学习研究使用，请在下载24小时之后删除。
禁止对其宣传，宣传后对鹰角网络造成的经济损失后果自负。
""")

def export_data():
    global curDir
    fileName, filetype = QFileDialog.getSaveFileName(Win,"文件保存",curDir,"Arknights Cheat Data文件 (*.acdata)")
    if not fileName == '':
        f=open(fileName, 'w', encoding='UTF-8')
        f.write(get_data())
        f.close

def str2bool(str):
    return True if str.lower() == 'true' else False

def import_data():
    global curDir
    fileName, filetype = QFileDialog.getOpenFileName(Win,"打开文件",curDir,"Arknights Cheat Data文件 (*.acdata)")
    import_dataFrom(fileName)

def import_dataFrom(fileName):
    global item,squadsInfo,squadsNm,charTableEdit,isMinors
    charTableEdit=True
    if not fileName == '':
        with open(fileName, 'r', encoding='utf-8') as f:
            strF = f.read()
            if len(strF) > 0:
                j=json.loads(strF)
            else:
                QMessageBox.warning(Win,"错误","文件为空",QMessageBox.Ok)
                return
        Win.user_UID.setText(j['uid'])
        Win.user_name.setText(j['nickName'])
        Win.user_nameNum.setText(j['nickNumber'])
        Win.user_Lv.setValue(j['level'])
        Win.user_ap.setValue(j['ap'])
        Win.user_apMax.setValue(j['maxAp'])
        Win.user_resume.setText(j['resume'])
        if isInit:
            isMinors=str2bool(j['userIsMinors'])
        else:
            Win.checkBox_fcm.setChecked(j['fcm'])
        secretary=j['secretary']
        Win.user_secretary.setCurrentIndex(charList.index(secretary))
        userSecretary_changed()
        for e,skinId in enumerate(skinList[secretary]):
            if skinList[secretary][j['secretarySkinId']]==skinList[secretary][skinId]:
                Win.user_secretarySkin.setCurrentIndex(e)
        item=eval('['+str(j['item'])+']')
        for e in j['chars']:  
            charId=j['chars'][e]['charId']
            for fp in favorPointList:
                if j['chars'][e]['favorPoint'] >= fp:
                    favPt=favorPointList.index(fp)
            potLV=j['chars'][e]['potentialRank']
            skillLv=j['chars'][e]['mainSkillLvl']
            skinId=j['chars'][e]['skin']
            lv=j['chars'][e]['level']
            eliteLv=j['chars'][e]['evolvePhase']
            skillIn=j['chars'][e]['defaultSkillIndex']
            skillIndex=len(charTable[charId]['skills'])
            if skillIndex==0:
                spLv=0
                skillIndex='无技能'
            else:
                spLv=j['chars'][e]['skills'][0]['specializeLevel']
                skillIndex=skillIn
            addCharList([charTable[charId]['name'],charList.index(charId),eliteLv,lv,skinList[charId][skinId],favPt,skillLv,skillIndex,spLv,potLV,''])
        squadsFirst=True
        squadsNm=j['squads']
        for e in j['squads']:
            Win.currSquad.addItem(j['squads'][e]['name'])
            for i,char in enumerate(j['squads'][e]['slots']):
                if char is not None:
                    charId=j['chars'][str(char['charInstId'])]['charId']
                    charIn=str(char['charInstId'])
                    if char['skillIndex']==-1:
                        maxSkillIn=skillIn='无技能'
                    else:
                        skillIn=str(char['skillIndex']+1)
                    name=charTable[charId]['name']
                    maxSkillIn=str(getBestSkill(char['charInstId']-1))
                else:
                    name='无'
                    charIn=''
                    skillIn=''
                    maxSkillIn=''
                if squadsFirst:
                    squadsInfo=[{'name':name,'charId':charIn,'skillIndex':skillIn,'maxSkillIndex':maxSkillIn}]
                    squadsFirst=False
                else:
                    squadsInfo=str(squadsInfo)[:-1]+','+str({'name':name,'charId':charIn,'skillIndex':skillIn,'maxSkillIndex':maxSkillIn})+']'
        currSquad_changed()

def editSquads():
    global squadsInfo
    squadsInfoJ=json.loads(squadsInfo.replace('\'','"'))
    cr_total=Win.table_char.rowCount()
    index=Win.customChar_squad.currentIndex()
    squadIndex=Win.table_squad.currentIndex().row()
    squadIn=Win.currSquad.currentIndex()*12+squadIndex
    newName=Win.table_char.item(index, 0).text()
    Win.table_squad.setItem(squadIndex,0,QTableWidgetItem(newName))
    squadsInfoJ[squadIn]['name']=newName
    Win.table_squad.setItem(squadIndex,1,QTableWidgetItem(str(index+1)))
    squadsInfoJ[squadIn]['charId']=str(index+1)
    newSkillIn=Win.char_skillIndex_squad.value()
    maxSkillLv=Win.table_squad.item(squadIndex, 3).text()
    if not maxSkillLv in ['1','2','3']:
        maxSkillLv=0
        squadsInfoJ[squadIn]['skillIndex']='无'
    else:
        squadsInfoJ[squadIn]['skillIndex']=newSkillIn
        maxSkillLv=int(maxSkillLv)
    if Win.char_skillIndex_squad.value() <= maxSkillLv:
        Win.table_squad.setItem(squadIndex,2,QTableWidgetItem(str(newSkillIn)))
    squadsInfo=json.dumps(squadsInfoJ)
    
def table_char_del():
    global tableCharLine
    tableCharLine=tableCharLine-1
    Win.table_char.removeRow(Win.table_char.currentIndex().row())

def table_char_delAll():
    global tableCharLine,charTableEdit
    charTableEdit=True
    tableCharLine=0
    for e in range(Win.table_char.rowCount()-1,-1,-1):
        Win.table_char.removeRow(e)

def listItem_changed():
    Win.item_value.setValue(item[0][itemList[Win.list_item.currentRow()]])

def char_eliteLv_changed():
    if not checkSelectChar():
        return
    char_lv_reload()
    
def char_lv_reload():
    global DebugOff
    index=Win.table_char.currentIndex().row()
    charIndex=int(Win.table_char.item(index, 1).text())
    charId=charList[charIndex]
    rarity=charTable[charId]['rarity']
    if int(Win.char_eliteLv.value())==2 and DebugOff:
        if rarity == 3:
            Win.char_Lv.setMaximum(70)
        elif rarity == 4:
            Win.char_Lv.setMaximum(80)
        elif rarity == 5:
            Win.char_Lv.setMaximum(90)
    if int(Win.char_eliteLv.value())==1 and DebugOff:
        if rarity == 2:
            Win.char_Lv.setMaximum(55)
        elif rarity == 3:
            Win.char_Lv.setMaximum(60)
        elif rarity == 4:
            Win.char_Lv.setMaximum(70)
        elif rarity == 5:
            Win.char_Lv.setMaximum(80)
    elif int(Win.char_eliteLv.value())==0 and DebugOff:
        if rarity <= 2:
            Win.char_Lv.setMaximum(30)
        elif rarity == 3:
            Win.char_Lv.setMaximum(45)
        elif rarity >= 4:
            Win.char_Lv.setMaximum(50)

def itemEdit_clicked():
    item[0][itemList[Win.list_item.currentRow()]]=Win.item_value.value()

def currSquad_changed():
    squadsIndex=Win.currSquad.currentIndex()
    squadsInfoJ=json.loads(squadsInfo.replace('\'','"'))
    squadsInfoList=['name','charId','skillIndex','maxSkillIndex']
    for y in range(0,12):
        for x in range(0,4):
            Win.table_squad.setItem(y, x, QTableWidgetItem(squadsInfoJ[squadsIndex*12+y][squadsInfoList[x]]))

def tab_changed():
    global charTableEdit
    if Win.tabWidget.currentIndex()==3 and charTableEdit:
        cr_total=Win.table_char.rowCount()
        charTableEdit=False
        Win.customChar_squad.clear()
        for index in range(0,cr_total):
            cr_charId=charList[int(Win.table_char.item(index, 1).text())]
            cr_name=Win.table_char.item(index, 0).text()
            Win.customChar_squad.addItem(cr_name+'|'+str(index)+'|'+str(getBestSkill(index)))

def editChar_changed():
    charIndex=Win.comboBox_editChar.currentIndex()-1
    charId=charList[charIndex]
    bestCharList=bestChar(charIndex)
    if DebugOff:
        Win.char_eliteLv.setMaximum(bestCharList[2])
        Win.char_Lv.setMaximum(bestCharList[3])
    Win.char_skin.clear()
    for e,skinId in enumerate(skinList[charId]):
        Win.char_skin.addItem(skinList[charId][skinId])
    skillIn = bestCharList[7]
    if skillIn in [1,2,3]:
        Win.char_skillIndex.setEnabled(True)
        Win.char_skillIndex.setMaximum(skillIn)
    else:
        Win.char_skillIndex.setEnabled(False)
    if Win.checkBox_customBest.isChecked():
        customChar_setBest()

def charSelectAll():
    if Win.checkBox_selectInv.isChecked():
        Win.checkBox_selectInv.setChecked(False)
    if Win.checkBox_selectAll.isChecked():
        for i in range(0,Win.table_char.rowCount()):
            if not i in indexList:
                Win.table_char.selectRow(i)
    else:
        for i in range(0,Win.table_char.rowCount()):
            Win.table_char.selectRow(i)
    table_char_selectChanged()

def charSelectInv():
    if Win.checkBox_selectAll.isChecked():
        Win.checkBox_selectAll.setChecked(False)
    for i in range(0,Win.table_char.rowCount()):
        Win.table_char.selectRow(i)
    table_char_selectChanged()

    global isRun
    if isRun:
        isRun=False
        Win.pushButton_run.setText('停止')
        f=open('.\data.acdata', 'w', encoding='UTF-8')
        f.write(get_data())
        f.close
        Win.log_browser.append('<font color="red">ArknightsCheater:启动mitmproxy中...</font>')
        Win.thread.start()
        Win.onLabel.setText('修改器端已在端口%s上开启'% (str(Win.gob_porxy.value())))
    else:
        isRun=True
        Win.pushButton_run.setText('启动')
        Win.thread.terminate()
        subprocess.Popen("taskkill /f /im mitmdump.exe>nul",shell=True)
        Win.log_browser.document().clear()
        Win.log_browser.setHtml("<html><head></head><body bgcolor=#293134></body></html>")
        Win.log_browser.append('<font color="#fff">用户停止操作</font>')
        Win.onLabel.setText('修改器端已关闭')

def initFromGame():
    global isInit
    if isInit:
        isInit=False
        Win.pushButton_run_init.setText('启动')
        Win.thread.terminate()
        subprocess.Popen("taskkill /f /im mitmdump.exe>nul",shell=True)
        Win.inInitInfo.setText('修改器端已关闭')
    else:
        isInit=True
        Win.pushButton_run_init.setText('停止')
        f=open('.\data.acdata', 'w', encoding='UTF-8')
        f.write('{"init":true,"fcm":'+str(Win.checkBox_fcm_init.isChecked()).lower()+'}')
        f.close
        Win.inInitInfo.setVisible(True)
        Win.thread.start()
        Win.inInitInfo.setText('启动mitmproxy中...')

def initDataFromGame():
    global isInit
    import_dataFrom('.\datafromgame.acdata')
    isInit=False
    Win.thread.terminate()
    subprocess.Popen("taskkill /f /im mitmdump.exe>nul",shell=True)
    skipInit()

def getBestSkill(charTableIndex):
    charIndex=int(Win.table_char.item(charTableIndex, 1).text())
    charEliteLv=int(Win.table_char.item(charTableIndex, 2).text())
    charId=charList[charIndex]
    name=charTable[charId]['name']
    skillIndex=len(charTable[charId]['skills'])
    if skillIndex==0:
        rt_skill='无'
    elif skillIndex==3:
        if charEliteLv==0:
            rt_skill=1
        elif charEliteLv==1:
            rt_skill=2
        elif charEliteLv==2:
            rt_skill=3
    elif skillIndex==2:
        if charEliteLv==0:
            rt_skill=1
        elif charEliteLv>=1:
            rt_skill=2
    elif skillIndex==1:
        if charEliteLv>=0:
            rt_skill=1
    return rt_skill
#init 

itemList=['gold','diamondShard','androidDiamond','iosDiamond','practiceTicket','lggShard','hggShard','gachaTicket','tenGachaTicket']
item=[{
    'gold': 99999,
    'diamondShard': 99999,
    'androidDiamond': 99999,
    'iosDiamond': 99999,
    'practiceTicket': 99999,
    'lggShard': 99999,
    'hggShard': 99999,
    'gachaTicket': 99999,
    'tenGachaTicket': 99999
}]
indexList=[]
squadsInfo=[]
if os.path.isfile('.\character_table.json'):   
    charTable=json.loads(open('.\character_table.json', 'r', encoding='UTF-8').read())
favorPointList = [0, 8, 16, 28, 40, 56, 72, 92, 112, 137, 162, 192, 222, 255, 288, 325, 362, 404, 446, 491, 536, 586, 636, 691, 746, 804, 862, 924, 986, 1052, 1118, 1184, 1250, 1316, 1382, 1457, 1532, 1607, 1682, 1757, 1832, 1917, 2002, 2087, 2172, 2257, 2352, 2447, 2542, 2637, 2732, 2840, 2960, 3080, 3200, 3320, 3450, 3580, 3710, 3840, 3970, 4110, 4250, 4390, 4530, 4670, 4820, 4970, 5120, 5270, 5420, 5575, 5730, 5885, 6040, 6195, 6350, 6505, 6660, 6815, 6970, 7125, 7280, 7435, 7590, 7745, 7900, 8055, 8210, 8365, 8520, 8675, 8830, 8985, 9140, 9295, 9450, 9605, 9760, 9915, 10070, 10225, 10380, 10535, 10690, 10845, 11000, 11155, 11310, 11465, 11620, 11775, 11930, 12085, 12240, 12395, 12550, 12705, 12860, 13015, 13170, 13325, 13480, 13635, 13790, 13945, 14100, 14255, 14410, 14565, 14720, 14875, 15030, 15185, 15340, 15495, 15650, 15805, 15960, 16115, 16270, 16425, 16580, 16735, 16890, 17045, 17200, 17355, 17510, 17665, 17820, 17975, 18130, 18285, 18440, 18595, 18750, 18905, 19060, 19215, 19370, 19525, 19680, 19835, 19990, 20145, 20300, 20455, 20610, 20765, 20920, 21075, 21230, 21385, 21540, 21695, 21850, 22005, 22160, 22315, 22470, 22625, 22780, 22935, 23090, 23245, 23400, 23555, 23710, 23865, 24020, 24175, 24330, 24485, 24640, 24795, 24950, 25105, 25260, 25415, 25570]
if os.path.isfile('.\skin_table.json'): 
    skinList=json.loads(skintable2list('.\skin_table.json'))
charList=[]
tableCharLine=0

def init():
    global charList
    if os.path.exists(curDir+'\data.acdata'):
        os.remove(curDir+'\data.acdata')
    elif os.path.exists(curDir+'\datafromgame.acdata'):
        os.remove(curDir+'\datafromgame.acdata')
    Win.comboBox_editChar.addItem('不修改')
    for e,charId in enumerate(charTable):
        if charId[:4]=='char':
            charList.append(charId)
            Win.comboBox_addChar.addItem(charTable[charId]['name'])
            Win.comboBox_editChar.addItem(charTable[charId]['name'])
            Win.user_secretary.addItem(charTable[charId]['name'])
    userSecretary_changed()

def dataInit():
    Win.textBrowser_init.setVisible(False)
    Win.groupBox_porxy_init.setVisible(False)
    Win.checkBox_fcm_init.setVisible(False)
    Win.pushButton_initSkip_2.setVisible(False)
    Win.inInitInfo.setVisible(False)
    Win.pushButton_run_init.setVisible(False)
    Win.action_import.setEnabled(False)
    Win.action_export.setEnabled(False)
    for e in range(1,5):
        Win.tabWidget.setTabEnabled(e,False)

def init_CNT():
    Win.frame_entryInit.setVisible(False)
    Win.textBrowser_init.setVisible(True)
    Win.groupBox_porxy_init.setVisible(True)
    Win.checkBox_fcm_init.setVisible(True)
    Win.pushButton_initSkip_2.setVisible(True)
    Win.pushButton_run_init.setVisible(True)

def skipInit():
    Win.tabWidget.setTabEnabled(0,False)
    Win.tabWidget.setCurrentIndex(1)
    for e in range(1,5):
        Win.tabWidget.setTabEnabled(e,True)
    Win.tabWidget.setStyleSheet("")
    Win.tabWidget.setStyleSheet("QTabBar::tab:disabled {width: 0; color: transparent;}")
    Win.action_import.setEnabled(True)
    Win.action_export.setEnabled(True)


#link
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
    
    def closeEvent(self, event):
        dataJson = curDir+'\data.acdata'
        dataFromGame = curDir+'\datafromgame.acdata'
        if os.path.exists(dataJson):
            os.remove(dataJson)
        if os.path.exists(dataFromGame):
            os.remove(dataFromGame)
        subprocess.Popen("taskkill /f /im mitmdump.exe>nul",shell=True)
    
    def resizeEvent(self, event):
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, self.width()+1, self.height()-self.statusBar.height()))
        self.log_browser.setGeometry(QtCore.QRect(178, 0, self.tabWidget.width()-self.groupBox_porxy.width()-17, self.tabWidget.height()-self.statusBar.height()-20))
        QtWidgets.QWidget.resizeEvent(self, event)

    def update_logtext(self, str):
        if isInit:
            if str[:12]=='initFinished':
                initDataFromGame()
            if str[19:28]=='mitmproxy':
                self.inInitInfo.setText('等待游戏启动中...')
        elif not isRun:
            if str[:16]=='ArknightsCheater':
                self.log_browser.append('<font color="red">'+str+'</font>')
            else:
                strhtml=str.replace('Loading script .\main.py','加载配置中...').replace('Proxy server listening at','修改器端开启于').replace('clientconnect','客户端连接').replace('clientdisconnect','客户端断开连接').replace(': GET',': <font color="green">获取数据从:</font>').replace(': POST',': <font color="Fuchsia">提交数据到:</font>').replace(': CONNECT',': <font color="Fuchsia">连接到:</font>')
                self.log_browser.append('<font color="white">'+strhtml+'</font>')

class RunThread(QThread):
    update_log = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()

    def run(self):
        global isInit
        if isInit:
            proxy=str(Win.gob_porxy_init.value())
        else:
            proxy=str(Win.gob_porxy.value())
        mitmRun = subprocess.Popen('mitmdump.exe -s .\main.py --ssl-insecure -p '+proxy+' --no-http2', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        while True:
            data = mitmRun.stdout.readline()
            if data == b'':
                if mitmRun.poll() is not None:
                    break
            else:
                self.update_log.emit(data.decode('gbk'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = Window()
    
    if not os.path.exists('.\character_table.json'):
        QMessageBox.warning(Win,"错误","请将character_table.json放入同目录下",QMessageBox.Ok)
        webbrowser.open_new_tab('https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/character_table.json')
        sys.exit()
    elif not os.path.exists('.\skin_table.json'):
        QMessageBox.warning(Win,"错误","请将skin_table.json放入同目录下",QMessageBox.Ok)
        webbrowser.open_new_tab('https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/skin_table.json')
        sys.exit()
    elif not os.path.exists('.\mitmdump.exe'):
        QMessageBox.warning(Win,"错误","请将mitmdump.exe放入同目录下",QMessageBox.Ok)
        webbrowser.open_new_tab('https://mitmproxy.org/downloads/')
        sys.exit()
    elif not os.path.exists('.\main.py'):
        QMessageBox.warning(Win,"错误","请将main.py放入同目录下",QMessageBox.Ok)
        webbrowser.open_new_tab('https://github.com/Tao0Lu/Arknights-Cheater/blob/master/main.py')
        sys.exit()
    
    init()
    
    dataInit()
    
    Win.show()
    
    Win.thread = RunThread()
    Win.thread.update_log.connect(Win.update_logtext)

    Win.pushButton_run.clicked.connect(lambda:run_and_exit())
    Win.pushButton_addChar.clicked.connect(lambda:addChar(Win.comboBox_addChar.currentIndex()))
    Win.pushButton_itemEdit.clicked.connect(lambda:itemEdit_clicked())
    Win.pushButton_charEdit.clicked.connect(lambda:charEdit())
    Win.pushButton_addAllChar.clicked.connect(lambda:charAddAll())
    Win.pushButton_clearChar.clicked.connect(lambda:table_char_delAll())
    Win.pushButton_initCTN.clicked.connect(lambda:init_CNT())
    Win.pushButton_initSkip.clicked.connect(lambda:skipInit())
    Win.pushButton_initSkip_2.clicked.connect(lambda:skipInit())
    Win.pushButton_charEdit_squad.clicked.connect(lambda:editSquads())
    Win.pushButton_run_init.clicked.connect(lambda:initFromGame())
    
    Win.tabWidget.currentChanged.connect(lambda:tab_changed())
    
    Win.action_exit.triggered.connect(lambda:sys.exit())
    Win.action_debug.triggered.connect(lambda:debug())
    Win.action_export.triggered.connect(lambda:export_data())
    Win.action_import.triggered.connect(lambda:import_data())
    Win.action_help.triggered.connect(lambda:help())
    Win.action_notice.triggered.connect(lambda:notice())
    
    Win.table_char.itemClicked.connect(lambda:table_char_selectChanged())
    Win.table_squad.itemClicked.connect(lambda:table_squad_selectChanged())
    
    Win.checkBox_customChar.stateChanged.connect(lambda:checkBoxCustomChar_changed())
    Win.checkBox_customBest.stateChanged.connect(lambda:checkBoxCustomBest_changed())
    Win.checkBox_customBest_squad.stateChanged.connect(lambda:table_squad_selectChanged())
    Win.checkBox_selectAll.stateChanged.connect(lambda:charSelectAll())
    Win.checkBox_selectInv.stateChanged.connect(lambda:charSelectInv())
    
    Win.list_item.itemClicked.connect(lambda:listItem_changed())

    Win.char_eliteLv.valueChanged.connect(lambda:char_eliteLv_changed())
    Win.char_Lv.valueChanged.connect(lambda:checkSelectChar())
    Win.char_favorPoint.valueChanged.connect(lambda:checkSelectChar())
    Win.char_skillLv.valueChanged.connect(lambda:checkSelectChar())
    Win.char_skillIndex.valueChanged.connect(lambda:checkSelectChar())
    Win.char_spLv.valueChanged.connect(lambda:checkSelectChar())
    Win.char_potLv.valueChanged.connect(lambda:checkSelectChar())
    
    Win.user_secretary.activated.connect(lambda:userSecretary_changed())
    Win.comboBox_editChar.activated.connect(lambda:editChar_changed())
    Win.currSquad.activated.connect(lambda:currSquad_changed())
    sys.exit(app.exec_())
start.setObjectName("tab_start")
        self.log_browser = QtWidgets.QTextBrowser(self.tab_start)
        self.log_browser.setGeometry(QtCore.QRect(178, 0, 541, 381))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.log_browser.setFont(font)
        self.log_browser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.log_browser.setObjectName("log_browser")
        self.groupBox_porxy = QtWidgets.QGroupBox(self.tab_start)
        self.groupBox_porxy.setGeometry(QtCore.QRect(10, 10, 161, 59))
        self.groupBox_porxy.setObjectName("groupBox_porxy")
        self.gob_porxy = QtWidgets.QSpinBox(self.groupBox_porxy)
        self.gob_porxy.setGeometry(QtCore.QRect(70, 30, 81, 22))
        self.gob_porxy.setMaximum(65535)
        self.gob_porxy.setProperty("value", 12450)
        self.gob_porxy.setObjectName("gob_porxy")
        self.label_21 = QtWidgets.QLabel(self.groupBox_porxy)
        self.label_21.setGeometry(QtCore.QRect(10, 30, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.pushButton_run = QtWidgets.QPushButton(self.tab_start)
        self.pushButton_run.setGeometry(QtCore.QRect(40, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setObjectName("pushButton_run")
        self.checkBox_fcm = QtWidgets.QCheckBox(self.tab_start)
        self.checkBox_fcm.setGeometry(QtCore.QRect(20, 80, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_fcm.setFont(font)
        self.checkBox_fcm.setObjectName("checkBox_fcm")
        self.tabWidget.addTab(self.tab_start, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 30))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")

        self.debug = QtWidgets.QMenu(self.menubar)
        self.debug.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.debug.setToolTipDuration(5)
        self.debug.setToolTipsVisible(False)
        self.debug.setObjectName("debug")
        self.action_debug = QAction(MainWindow)
        self.action_debug.setCheckable(False)
        self.action_debug.setObjectName('debugAction')
        self.action_debug.setText('Debug模式')
        
        self.about = QtWidgets.QMenu(self.menubar)
        self.about.setObjectName("about")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.onLabel=QLabel('')
        self.statusBar.addPermanentWidget(self.onLabel, stretch=0)
        self.action_import = QtWidgets.QAction(MainWindow)
        self.action_import.setObjectName("action_import")
        self.action_export = QtWidgets.QAction(MainWindow)
        self.action_export.setObjectName("action_export")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.action_notice = QtWidgets.QAction(MainWindow)
        self.action_notice.setObjectName("action_notice")
        self.file.addAction(self.action_import)
        self.file.addAction(self.action_export)
        self.file.addSeparator()
        self.file.addAction(self.action_exit)
        self.about.addAction(self.action_help)
        self.about.addSeparator()
        self.about.addAction(self.action_notice)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.action_debug)
        self.menubar.addAction(self.about.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.user_UID, self.user_name)
        MainWindow.setTabOrder(self.user_name, self.user_nameNum)
        MainWindow.setTabOrder(self.user_nameNum, self.user_Lv)
        MainWindow.setTabOrder(self.user_Lv, self.user_ap)
        MainWindow.setTabOrder(self.user_ap, self.user_apMax)
        MainWindow.setTabOrder(self.user_apMax, self.user_resume)
        MainWindow.setTabOrder(self.user_resume, self.user_secretary)
        MainWindow.setTabOrder(self.user_secretary, self.user_secretarySkin)
        MainWindow.setTabOrder(self.user_secretarySkin, self.list_item)
        MainWindow.setTabOrder(self.list_item, self.item_value)
        MainWindow.setTabOrder(self.item_value, self.pushButton_itemEdit)
        MainWindow.setTabOrder(self.pushButton_itemEdit, self.gob_porxy)
        MainWindow.setTabOrder(self.gob_porxy, self.table_char)
        MainWindow.setTabOrder(self.table_char, self.comboBox_addChar)
        MainWindow.setTabOrder(self.comboBox_addChar, self.checkBox_addBest)
        MainWindow.setTabOrder(self.checkBox_addBest, self.pushButton_addChar)
        MainWindow.setTabOrder(self.pushButton_addChar, self.checkBox_customChar)
        MainWindow.setTabOrder(self.checkBox_customChar, self.pushButton_addAllChar)
        MainWindow.setTabOrder(self.pushButton_addAllChar, self.char_eliteLv)
        MainWindow.setTabOrder(self.char_eliteLv, self.char_Lv)
        MainWindow.setTabOrder(self.char_Lv, self.char_skin)
        MainWindow.setTabOrder(self.char_skin, self.char_favorPoint)
        MainWindow.setTabOrder(self.char_favorPoint, self.char_skillLv)
        MainWindow.setTabOrder(self.char_skillLv, self.char_skillIndex)
        MainWindow.setTabOrder(self.char_skillIndex, self.char_spLv)
        MainWindow.setTabOrder(self.char_spLv, self.char_potLv)
        MainWindow.setTabOrder(self.char_potLv, self.checkBox_customBest)
        MainWindow.setTabOrder(self.checkBox_customBest, self.pushButton_charEdit)
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ArknightsCheater"))
        self.textBrowser_init.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">此破解方法在安卓7.0以上中受限制(iOS安装描述文件后全版本都可以)，如果你是安卓7.0以上，请参考:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">解决方法1：使用安卓7.0以下版本的手机。</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">解决方式2：Root手机，安装 Xposed + JustTrustMe。</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">解决方式3：不Root，使用 VirtualXposed、太极等 + JustTrustMe。或使用安卓内模拟器 如:VMOS等。</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请在手机或模拟器中完成以下配置：</p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">确保手机或模拟器和电脑在同一局域网下。</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">进入手机或模拟器WLAN(Wi-Fi)设置配置手机代理。<br />安卓：修改网络—高级选项—代理—手动<br />iOS：HTTP代理—配置代理—手动<br />将服务器和端口设置为mitmproxy所监听的主机ip和端口。<br />保存/储存</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">右侧配置设置并点击启动</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">进入网站 http://mitm.it 下载证书(iOS为描述文件)并安装。<br />iOS多一步：设置—通用—关于本机—证书信任设置—mitmproxy—打开</li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">重新进入游戏。</li></ol></body></html>"))
        self.pushButton_run_init.setText(_translate("MainWindow", "启动"))
        self.groupBox_porxy_init.setTitle(_translate("MainWindow", "代理设置"))
        self.label_33.setText(_translate("MainWindow", "端口:"))
        self.inInitInfo.setText(_translate("MainWindow", "启动mitmproxy中..."))
        self.pushButton_initSkip.setText(_translate("MainWindow", "跳过/高级修改"))
        self.label_3.setText(_translate("MainWindow", "启动游戏以初始化"))
        self.pushButton_initCTN.setText(_translate("MainWindow", "继续"))
        self.pushButton_initSkip_2.setText(_translate("MainWindow", "跳过/高级修改"))
        self.checkBox_fcm_init.setText(_translate("MainWindow", "防沉迷破解"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "初始化"))
        self.groupBox_item.setTitle(_translate("MainWindow", "物品"))
        __sortingEnabled = self.list_item.isSortingEnabled()
        self.list_item.setSortingEnabled(False)
        item = self.list_item.item(0)
        item.setText(_translate("MainWindow", "龙门币"))
        item = self.list_item.item(1)
        item.setText(_translate("MainWindow", "合成玉"))
        item = self.list_item.item(2)
        item.setText(_translate("MainWindow", "安卓源石"))
        item = self.list_item.item(3)
        item.setText(_translate("MainWindow", "iOS源石"))
        item = self.list_item.item(4)
        item.setText(_translate("MainWindow", "演习券"))
        item = self.list_item.item(5)
        item.setText(_translate("MainWindow", "资深凭证"))
        item = self.list_item.item(6)
        item.setText(_translate("MainWindow", "高级凭证"))
        item = self.list_item.item(7)
        item.setText(_translate("MainWindow", "寻访凭证"))
        item = self.list_item.item(8)
        item.setText(_translate("MainWindow", "十连寻访凭证"))
        self.list_item.setSortingEnabled(__sortingEnabled)
        self.pushButton_itemEdit.setText(_translate("MainWindow", "修改"))
        self.label_14.setText(_translate("MainWindow", "昵称编号:"))
        self.label_16.setText(_translate("MainWindow", "理智:"))
        self.user_nameNum.setPlaceholderText(_translate("MainWindow", "8888"))
        self.label_18.setText(_translate("MainWindow", "签名:"))
        self.groupBox_secretary.setTitle(_translate("MainWindow", "助理"))
        self.label_20.setText(_translate("MainWindow", "助理皮肤:"))
        self.label_19.setText(_translate("MainWindow", "助理:"))
        self.label_13.setText(_translate("MainWindow", "昵称:"))
        self.user_UID.setPlaceholderText(_translate("MainWindow", "8888888"))
        self.user_name.setPlaceholderText(_translate("MainWindow", "破解用户"))
        self.label_22.setText(_translate("MainWindow", "等级:"))
        self.label_17.setText(_translate("MainWindow", "理智上限:"))
        self.user_resume.setPlaceholderText(_translate("MainWindow", "Ta什么都没有留下"))
        self.label_15.setText(_translate("MainWindow", "UID:"))
        self.label_7.setText(_translate("MainWindow", "警告:对以上数据的修改可能导致游戏崩溃"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_userData), _translate("MainWindow", "用户数据"))
        self.groupBox_addChar.setTitle(_translate("MainWindow", "添加干员"))
        self.checkBox_addBest.setText(_translate("MainWindow", "最好"))
        self.pushButton_addChar.setText(_translate("MainWindow", "添加干员"))
        self.checkBox_customChar.setText(_translate("MainWindow", "自定义干员"))
        self.pushButton_addAllChar.setText(_translate("MainWindow", "添加所有干员"))
        self.pushButton_clearChar.setText(_translate("MainWindow", "清空"))
        self.checkBox_selectAll.setText(_translate("MainWindow", "全选"))
        self.checkBox_selectInv.setText(_translate("MainWindow", "反选"))
        self.groupBox_customChar.setTitle(_translate("MainWindow", "自定义干员"))
        self.label_10.setText(_translate("MainWindow", "潜能等级:"))
        self.label_9.setText(_translate("MainWindow", "技能"))
        self.label_2.setText(_translate("MainWindow", "皮肤:"))
        self.label_5.setText(_translate("MainWindow", " 等级:"))
        self.label_4.setText(_translate("MainWindow", "精英:"))
        self.label.setText(_translate("MainWindow", "信赖值:"))
        self.label_8.setText(_translate("MainWindow", "选中技能:"))
        self.label_6.setText(_translate("MainWindow", "技能等级:"))
        self.label_11.setText(_translate("MainWindow", "技能专精等级:"))
        self.label_23.setText(_translate("MainWindow", "修改为:"))
        self.checkBox_customBest.setText(_translate("MainWindow", "最好"))
        self.label_selectChar.setText(_translate("MainWindow", "请选择干员"))
        self.pushButton_charEdit.setText(_translate("MainWindow", "修改"))
        self.table_char.setHorizontalHeaderLabels(['干员','ID','精英','等级','皮肤','信赖值','技能等级','选中技能','专精等级','潜能等级','操作'])
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_charData), _translate("MainWindow", "干员数据"))
        self.groupBox_customChar_squad.setTitle(_translate("MainWindow", "自定义编队"))
        self.checkBox_customBest_squad.setText(_translate("MainWindow", "最好"))
        self.label_selectChar_squad.setText(_translate("MainWindow", "请选择干员"))
        self.pushButton_charEdit_squad.setText(_translate("MainWindow", "修改"))
        self.label_38.setText(_translate("MainWindow", "修改为:"))
        self.label_32.setText(_translate("MainWindow", "技能"))
        self.label_36.setText(_translate("MainWindow", "选中技能:"))
        self.table_squad.setHorizontalHeaderLabels(['干员','装载ID','选中技能','最大技能'])
        self.label_37.setText(_translate("MainWindow", "当前编队:"))
        self.label_12.setText(_translate("MainWindow", "注:编队中不能出现相同装载ID的干员,且装载ID不能大于所拥有的干员数；修改编队后，需要手动在游戏主界面编队选中编队中某一干员，随便修改其技能并且返回到主界面来达到修改效果。"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_squad), _translate("MainWindow", "编队数据"))
        self.log_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:8pt; font-weight:400; font-style:normal;\" bgcolor=\"#293134\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.groupBox_porxy.setTitle(_translate("MainWindow", "代理设置"))
        self.label_21.setText(_translate("MainWindow", "端口:"))
        self.pushButton_run.setText(_translate("MainWindow", "启动"))
        self.checkBox_fcm.setText(_translate("MainWindow", "防沉迷破解"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_start), _translate("MainWindow", "启动"))
        self.file.setTitle(_translate("MainWindow", "文件"))
        self.about.setTitle(_translate("MainWindow", "关于"))
        self.action_import.setText(_translate("MainWindow", "导入配置"))
        self.action_export.setText(_translate("MainWindow", "导出配置"))
        self.action_exit.setText(_translate("MainWindow", "退出"))
        self.action_help.setText(_translate("MainWindow", "如何使用"))
        self.action_notice.setText(_translate("MainWindow", "用户须知"))

#define
def skintable2list(skin_table_path):
    skin = json.loads(open(skin_table_path, 'r', encoding='UTF-8').read())
    skinInner=[]
    for e,skinId in enumerate(skin['charSkins']):
        if skinId[:4]=='char' and not skinId in skinInner:
            skinInner.append(skin['charSkins'][skinId]['charId']+'":"')
    j=json.loads(str(skinInner).replace('\'','"').replace(']','}]').replace('[','[{').replace('""','{}')[1:-1])
    for e,skinId in enumerate(skin['charSkins']):
        if skinId[:4]=='char':
            charId=skin['charSkins'][skinId]['charId']
            skinname=skin['charSkins'][skinId]['displaySkin']['skinGroupName']
            if skinId==charId+'#2':
                skinname='精二服装'
            elif skinId == charId+'#1+':
                skinname='精一服装'
            if str(j[charId])=='{}':
                j[charId]='{\''+skinId+'\':\''+skinname+'\'}'
            else:
                j[charId]=j[charId][:-1]+',\''+skinId+'\':\''+skinname+'\'}'
    return str(j).replace('"','').replace('\'','"')

def getCustomChar(charId,charNum,eliteLv,lv,skin,favPt,skillLv,skillIndex,spLv,potLv):
    skills = charTable[charId]['skills']
    modSkillPath = [{
    'skillId': '',
    'unlock': 1,
    'state': 0,
    'specializeLevel': spLv,
    'completeUpgradeTime': -1
    }]
    if len(skills) == 0:
        modSkill = []
    else:
        modSkillTemp=json.dumps(modSkillPath)[1:-1]
        modSkillPath=json.dumps(modSkillPath)[1:-1]
        for num in range(1,len(skills)):
            modSkillPath=modSkillPath+','+modSkillTemp
        modSkill = json.loads('['+modSkillPath+']') 
        for e in range(0,len(skills)):
            modSkill[e]['skillId'] = charTable[charId]['skills'][e]['skillId']
    CustomChar = {str(charNum):{
    'instId':charNum,
    'charId':charId,
    'favorPoint':favorPointList[favPt],
    'potentialRank':potLv,
    'mainSkillLvl':skillLv,
    'skin':skin,
    'level':lv,
    'exp':0,
    'evolvePhase':eliteLv,
    'defaultSkillIndex':skillIndex,
    'gainTime':1556654400,
    'skills':modSkill}
    }
    return CustomChar

def table_char_selectChanged():
    first=True
    global indexList,char_isMultiSelect
    indexList=[]
    for index in Win.table_char.selectedIndexes():
        if first:
            lastIndex=index.row()
            first=False
            indexList.append(index.row())
        if not lastIndex==index.row():
            indexList.append(index.row())
        lastIndex=index.row()
    if not len(indexList)==0:
        if len(indexList)==1:
            index=Win.table_char.currentIndex().row()
            charId=charList[int(Win.table_char.item(index, 1).text())]
            Win.char_skin.clear()
            for e,skinId in enumerate(skinList[charId]):
                    Win.char_skin.addItem(skinList[charId][skinId])
            if Win.checkBox_customBest.isChecked():
                    Win.checkBox_customBest.setChecked(False)
            customChar_reload(index)
            char_eliteLv_changed()
        else:
            char_isMultiSelect=True
            mulitEditChar_selectChanged()

def mulitEditChar_selectChanged():
    index=Win.table_char.currentIndex().row()
    charId=charList[index]
    Win.label_selectChar.setText('多选')
    Win.char_skin.clear()
    for e,skinId in enumerate(skinList[charId]):
        Win.char_skin.addItem(skinList[charId][skinId])
    if DebugOff:
        Win.char_eliteLv.setMaximum(2)
        Win.char_Lv.setMaximum(90)
        Win.char_skillIndex.setEnabled(True)
        Win.char_skillIndex.setMaximum(3)

def table_squad_selectChanged():
    index=Win.table_squad.currentIndex().row()
    Win.groupBox_customChar_squad.setEnabled(True)
    if Win.table_squad.item(index, 0).text()=='无':
        Win.groupBox_customChar_squad.setEnabled(False)
        Win.label_selectChar_squad.setText('无')
    else:
        customSquads_reload(index)

def customSquads_reload(index):
    Win.label_selectChar_squad.setText(Win.table_squad.item(index, 0).text())
    charIn=int(Win.table_squad.item(index, 1).text())
    charIndex=0
    for e in charTable:
        if charTable[e]['name']==Win.table_squad.item(index, 0).text():
            charIndex=charList.index(e)
            break
    skillIn = Win.table_squad.item(index, 2).text()
    bestCharList=bestChar(charIndex)

    if skillIn in ['1','2','3']:
        maxSkillIndex=Win.table_squad.item(index, 3).text()
        Win.char_skillIndex_squad.setMaximum(int(maxSkillIndex))
        if Win.checkBox_customBest_squad.isChecked():
            Win.char_skillIndex_squad.setEnabled(False)
            Win.char_skillIndex_squad.setValue(int(maxSkillIndex))
        else:
            Win.char_skillIndex_squad.setEnabled(True)
            Win.char_skillIndex_squad.setValue(int(skillIn))
    else:
        Win.char_skillIndex_squad.setEnabled(False)

def customChar_reload(index):
    charIndex=int(Win.table_char.item(index, 1).text())
    charId=charList[charIndex]
    rarity=charTable[charId]['rarity']
    Win.label_selectChar.setText(charTable[charId]['name'])
    bestCharList=bestChar(charIndex)
    if DebugOff:
        Win.char_eliteLv.setMaximum(bestCharList[2])
        Win.char_Lv.setMaximum(bestCharList[3])
    Win.char_eliteLv.setValue(int(Win.table_char.item(index, 2).text()))
    Win.char_Lv.setValue(int(Win.table_char.item(index, 3).text()))
    for e,skinId in enumerate(skinList[charId]):
        if Win.table_char.item(index, 4).text()==skinList[charId][skinId]:
            Win.char_skin.setCurrentIndex(e)
    Win.char_favorPoint.setValue(int(Win.table_char.item(index, 5).text()))
    Win.char_skillLv.setValue(int(Win.table_char.item(index, 6).text()))
    skillIn = Win.table_char.item(index, 7).text()
    if skillIn in ['1','2','3']:
        Win.char_skillIndex.setEnabled(True)
        Win.char_skillIndex.setMaximum(int(bestCharList[7]))
        Win.char_skillIndex.setValue(int(skillIn))
    else:
        Win.char_skillIndex.setEnabled(False)
    Win.char_spLv.setValue(int(Win.table_char.item(index, 8).text()))
    Win.char_potLv.setValue(int(Win.table_char.item(index, 9).text()))

def userSecretary_changed():
    Win.user_secretarySkin.clear()
    charId=charList[Win.user_secretary.currentIndex()]
    for e,skinId in enumerate(skinList[charId]):
        Win.user_secretarySkin.addItem(skinList[charId][skinId])
        
def checkBoxCustomChar_changed():
    if Win.checkBox_customChar.isChecked():
        Win.groupBox_customChar.setEnabled(True)
    else:
        Win.groupBox_customChar.setEnabled(False)

def checkBoxCustomBest_changed():
    if Win.checkBox_customBest.isChecked():
        customChar_setBest()
        Win.frame_editChar.setEnabled(False)
    else:
        Win.frame_editChar.setEnabled(True)

def customChar_setBest():
    if not checkSelectChar():
        return
    index=Win.table_char.currentIndex().row()
    charIndex=int(Win.table_char.item(index, 1).text())
    charId=charList[charIndex]
    bestCharList=bestChar(charIndex)
    Win.char_eliteLv.setValue(bestCharList[2])
    Win.char_Lv.setValue(bestCharList[3])
    for e,skinId in enumerate(skinList[charId]):
        if bestCharList[4]==skinList[charId][skinId]:
            Win.char_skin.setCurrentIndex(e)
    Win.char_favorPoint.setValue(bestCharList[5])
    skillIn=bestCharList[6]
    if skillIn in ['1','2','3']:
        Win.char_skillIndex.setEnabled(True)
        Win.char_skillIndex.setMaximum(int(bestCharList[7]))
        Win.char_skillIndex.setValue(int(bestCharList[7]))
    else:
        Win.char_skillIndex.setEnabled(False)
    Win.char_spLv.setValue(bestCharList[8])
    Win.char_potLv.setValue(bestCharList[9])

def debug():
    global DebugOff
    if DebugOff:
        DebugOff=False
        Win.user_Lv.setMaximum(999999999)
        Win.user_apMax.setMaximum(999999999)
        Win.char_eliteLv.setMaximum(999999999)
        Win.char_Lv.setMaximum(999999999)
        Win.char_skillLv.setMaximum(999999999)
        Win.char_spLv.setMaximum(999999999)
        Win.char_potLv.setMaximum(999999999)
        Win.action_debug.setText('关闭Debug模式')
    else:
        DebugOff=True
        Win.user_Lv.setMaximum(120)
        Win.user_apMax.setMaximum(135)
        Win.char_skillLv.setMaximum(7)
        Win.char_eliteLv.setMaximum(2)
        charIndex=Win.table_char.currentIndex().row()
        if charIndex!=-1:
            Win.char_eliteLv.setValue(bestChar(charIndex)[2])
            char_lv_reload()
        Win.char_spLv.setMaximum(3)
        Win.char_potLv.setMaximum(5)
        Win.action_debug.setText('Debug模式')

def run_and_exit():
    global isRun
    if isRun:
        isRun=False
        Win.pushButton_run.setText('停止')
        f=open('.\data.acdata', 'w', encoding='UTF-8')
        f.write(get_data())
        f.close
        Win.log_browser.append('<font color="red">ArknightsCheater:启动mitmproxy中...</font>')
        Win.thread.start()
        Win.onLabel.setText('修改器端已在端口%s上开启'% (str(Win.gob_porxy.value())))
    else:
        isRun=True
        Win.pushButton_run.setText('启动')
        Win.thread.terminate()
        subprocess.Popen("taskkill /f /im mitmdump.exe>nul",shell=True)
        Win.log_browser.document().clear()
        Win.log_browser.setHtml("<html><head></head><body bgcolor=#293134></body></html>")
        Win.log_browser.append('<font color="#fff">用户停止操作</font>')
        Win.onLabel.setText('修改器端已关闭')

def get_data():
    global porxy
    global userUID,userName,userNameNum,userResume,squadsNm
    isFCM=Win.checkBox_fcm.isChecked()
    CustomCharTemp=''
    if not Win.user_UID.text()=='':
        userUID=Win.user_UID.text()
    if not Win.user_name.text()=='':
        userName=Win.user_name.text()
    if not Win.user_nameNum.text()=='':
        userNameNum=Win.user_nameNum.text()
    if not Win.user_resume.text()=='':
        userResume=Win.user_resume.text()
    
    cr_total=Win.table_char.rowCount()
    for index in range(0,cr_total):
        cr_charId=charList[int(Win.table_char.item(index, 1).text())]
        cr_eliteLv=int(Win.table_char.item(index, 2).text())
        cr_lv=int(Win.table_char.item(index, 3).text())
        for e,skinId in enumerate(skinList[cr_charId]):
            if Win.table_char.item(index, 4).text()==skinList[cr_charId][skinId]:
                cr_skinId=skinId
        cr_favPt=int(Win.table_char.item(index, 5).text())
        cr_skillLv=int(Win.table_char.item(index, 6).text())
        cr_skillIn = Win.table_char.item(index, 7).text()
        if cr_skillIn in ['1','2','3']:
            cr_skillIndex=int(cr_skillIn)-1
        else:
            cr_skillIn
