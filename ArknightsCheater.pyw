# -*- coding: utf-8 -*-

import json,sys,os,socket,subprocess
from PyQt5.QtWidgets import QMainWindow,QApplication,QAbstractItemView,QTableView,QAction,QLabel,QTableWidgetItem,QPushButton,QMessageBox,QFileDialog
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5 import QtCore,QtGui,QtWidgets
import webbrowser
#data & default
DebugOff=True
curDir=os.path.abspath(os.path.dirname(__file__))
porxy=12450
#user
isRun=True
userUID='8888888'
userName='破解用户'
userNameNum='8888'
userLv=120
userAp=135
userApMax=135
userResume='Ta什么都没有留下'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(810, 630)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_userData = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_userData.setGeometry(QtCore.QRect(10, 10, 221, 431))
        self.groupBox_userData.setObjectName("groupBox_userData")
        self.label_14 = QtWidgets.QLabel(self.groupBox_userData)
        self.label_14.setGeometry(QtCore.QRect(10, 80, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_18 = QtWidgets.QLabel(self.groupBox_userData)
        self.label_18.setGeometry(QtCore.QRect(10, 200, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_16 = QtWidgets.QLabel(self.groupBox_userData)
        self.label_16.setGeometry(QtCore.QRect(10, 140, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_userData)
        self.label_17.setGeometry(QtCore.QRect(10, 170, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_13 = QtWidgets.QLabel(self.groupBox_userData)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.user_ap = QtWidgets.QSpinBox(self.groupBox_userData)
        self.user_ap.setGeometry(QtCore.QRect(120, 140, 91, 22))
        self.user_ap.setMaximum(999999999)
        self.user_ap.setProperty("value", 135)
        self.user_ap.setObjectName("user_ap")
        self.user_apMax = QtWidgets.QSpinBox(self.groupBox_userData)
        self.user_apMax.setGeometry(QtCore.QRect(120, 170, 91, 22))
        self.user_apMax.setMaximum(135)
        self.user_apMax.setProperty("value", 135)
        self.user_apMax.setObjectName("user_apMax")
        self.groupBox_item = QtWidgets.QGroupBox(self.groupBox_userData)
        self.groupBox_item.setGeometry(QtCore.QRect(10, 310, 201, 111))
        self.groupBox_item.setObjectName("groupBox_item")
        self.item_value = QtWidgets.QSpinBox(self.groupBox_item)
        self.item_value.setGeometry(QtCore.QRect(135, 30, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.item_value.setFont(font)
        self.item_value.setMaximum(999999999)
        self.item_value.setProperty("value", 99999)
        self.item_value.setObjectName("item_value")
        self.list_item = QtWidgets.QListWidget(self.groupBox_item)
        self.list_item.setGeometry(QtCore.QRect(5, 20, 121, 81))
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
        self.pushButton_itemEdit.setGeometry(QtCore.QRect(135, 60, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_itemEdit.setFont(font)
        self.pushButton_itemEdit.setObjectName("pushButton_itemEdit")
        self.groupBox_secretary = QtWidgets.QGroupBox(self.groupBox_userData)
        self.groupBox_secretary.setGeometry(QtCore.QRect(10, 230, 201, 71))
        self.groupBox_secretary.setObjectName("groupBox_secretary")
        self.user_secretarySkin = QtWidgets.QComboBox(self.groupBox_secretary)
        self.user_secretarySkin.setGeometry(QtCore.QRect(105, 40, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.user_secretarySkin.setFont(font)
        self.user_secretarySkin.setObjectName("user_secretarySkin")
        self.label_20 = QtWidgets.QLabel(self.groupBox_secretary)
        self.label_20.setGeometry(QtCore.QRect(105, 20, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.user_secretary = QtWidgets.QComboBox(self.groupBox_secretary)
        self.user_secretary.setGeometry(QtCore.QRect(5, 40, 91, 22))
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
        self.label_15 = QtWidgets.QLabel(self.groupBox_userData)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_22 = QtWidgets.QLabel(self.groupBox_userData)
        self.label_22.setGeometry(QtCore.QRect(10, 110, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.user_Lv = QtWidgets.QSpinBox(self.groupBox_userData)
        self.user_Lv.setGeometry(QtCore.QRect(120, 110, 91, 22))
        self.user_Lv.setMinimum(1)
        self.user_Lv.setMaximum(120)
        self.user_Lv.setProperty("value", 120)
        self.user_Lv.setObjectName("user_Lv")
        self.user_UID = QtWidgets.QLineEdit(self.groupBox_userData)
        self.user_UID.setGeometry(QtCore.QRect(90, 20, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.user_UID.setFont(font)
        self.user_UID.setObjectName("user_UID")
        self.user_name = QtWidgets.QLineEdit(self.groupBox_userData)
        self.user_name.setGeometry(QtCore.QRect(90, 50, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.user_name.setFont(font)
        self.user_name.setObjectName("user_name")
        self.user_nameNum = QtWidgets.QLineEdit(self.groupBox_userData)
        self.user_nameNum.setGeometry(QtCore.QRect(120, 80, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.user_nameNum.setFont(font)
        self.user_nameNum.setObjectName("user_nameNum")
        self.user_resume = QtWidgets.QLineEdit(self.groupBox_userData)
        self.user_resume.setGeometry(QtCore.QRect(90, 200, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.user_resume.setFont(font)
        self.user_resume.setObjectName("user_resume")
        self.groupBox_charData = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_charData.setGeometry(QtCore.QRect(240, 10, 561, 361))
        self.groupBox_charData.setObjectName("groupBox_charData")
        self.table_Char = QtWidgets.QTableWidget(self.groupBox_charData)
        self.table_Char.setGeometry(QtCore.QRect(10, 30, 301, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table_Char.setFont(font)
        self.table_Char.setShowGrid(True)
        self.table_Char.setObjectName("table_Char")
        self.table_Char.setColumnCount(11)
        self.table_Char.setRowCount(0)
        self.table_Char.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        self.table_Char.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.table_Char.setSelectionBehavior(QAbstractItemView.SelectItems);  # 设置只能选中单元格
        self.table_Char.horizontalHeader().setVisible(True)
        self.table_Char.horizontalHeader().setCascadingSectionResizes(False)
        self.table_Char.horizontalHeader().setDefaultSectionSize(75)
        self.table_Char.horizontalHeader().setSortIndicatorShown(False)
        self.table_Char.horizontalHeader().setStretchLastSection(False)
        self.table_Char.verticalHeader().setCascadingSectionResizes(False)
        self.table_Char.verticalHeader().setSortIndicatorShown(False)
        self.table_Char.verticalHeader().setStretchLastSection(False)
        self.groupBox_customChar = QtWidgets.QGroupBox(self.groupBox_charData)
        self.groupBox_customChar.setEnabled(False)
        self.groupBox_customChar.setGeometry(QtCore.QRect(320, 20, 231, 331))
        self.groupBox_customChar.setObjectName("groupBox_customChar")
        self.frame_editChar = QtWidgets.QFrame(self.groupBox_customChar)
        self.frame_editChar.setGeometry(QtCore.QRect(10, 60, 211, 211))
        self.frame_editChar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_editChar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_editChar.setObjectName("frame_editChar")
        self.label_10 = QtWidgets.QLabel(self.frame_editChar)
        self.label_10.setGeometry(QtCore.QRect(10, 180, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.frame_editChar)
        self.label_9.setGeometry(QtCore.QRect(166, 120, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.char_skillLv = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_skillLv.setGeometry(QtCore.QRect(160, 90, 42, 22))
        self.char_skillLv.setMinimum(1)
        self.char_skillLv.setMaximum(7)
        self.char_skillLv.setObjectName("char_skillLv")
        self.label_2 = QtWidgets.QLabel(self.frame_editChar)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.char_eliteLv = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_eliteLv.setGeometry(QtCore.QRect(60, 0, 41, 22))
        self.char_eliteLv.setMaximum(2)
        self.char_eliteLv.setObjectName("char_eliteLv")
        self.char_favorPoint = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_favorPoint.setGeometry(QtCore.QRect(151, 60, 51, 22))
        self.char_favorPoint.setMaximum(200)
        self.char_favorPoint.setObjectName("char_favorPoint")
        self.label_5 = QtWidgets.QLabel(self.frame_editChar)
        self.label_5.setGeometry(QtCore.QRect(101, 0, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.frame_editChar)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.frame_editChar)
        self.label.setGeometry(QtCore.QRect(10, 60, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.frame_editChar)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.char_skin = QtWidgets.QComboBox(self.frame_editChar)
        self.char_skin.setGeometry(QtCore.QRect(71, 30, 131, 22))
        self.char_skin.setObjectName("char_skin")
        self.char_skillIndex = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_skillIndex.setGeometry(QtCore.QRect(121, 120, 42, 22))
        self.char_skillIndex.setMinimum(1)
        self.char_skillIndex.setMaximum(3)
        self.char_skillIndex.setObjectName("char_skillIndex")
        self.char_potLv = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_potLv.setGeometry(QtCore.QRect(160, 180, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.char_potLv.setFont(font)
        self.char_potLv.setMaximum(5)
        self.char_potLv.setObjectName("char_potLv")
        self.char_Lv = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_Lv.setGeometry(QtCore.QRect(161, 0, 41, 22))
        self.char_Lv.setMinimum(1)
        self.char_Lv.setMaximum(80)
        self.char_Lv.setObjectName("char_Lv")
        self.label_6 = QtWidgets.QLabel(self.frame_editChar)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.frame_editChar)
        self.label_11.setGeometry(QtCore.QRect(10, 150, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.char_spLv = QtWidgets.QSpinBox(self.frame_editChar)
        self.char_spLv.setGeometry(QtCore.QRect(160, 150, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.char_spLv.setFont(font)
        self.char_spLv.setMaximum(3)
        self.char_spLv.setObjectName("char_spLv")
        self.checkBox_customBest = QtWidgets.QCheckBox(self.groupBox_customChar)
        self.checkBox_customBest.setGeometry(QtCore.QRect(20, 290, 61, 30))
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
        self.pushButton_charEdit.setGeometry(QtCore.QRect(130, 290, 93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_charEdit.setFont(font)
        self.pushButton_charEdit.setObjectName("pushButton_charEdit")
        self.groupBox_addChar = QtWidgets.QGroupBox(self.groupBox_charData)
        self.groupBox_addChar.setGeometry(QtCore.QRect(10, 260, 301, 91))
        self.groupBox_addChar.setObjectName("groupBox_addChar")
        self.checkBox_addBest = QtWidgets.QCheckBox(self.groupBox_addChar)
        self.checkBox_addBest.setGeometry(QtCore.QRect(120, 20, 61, 22))
        self.checkBox_addBest.setObjectName("checkBox_addBest")
        self.comboBox_addChar = QtWidgets.QComboBox(self.groupBox_addChar)
        self.comboBox_addChar.setGeometry(QtCore.QRect(10, 20, 101, 22))
        self.comboBox_addChar.setObjectName("comboBox_addChar")
        self.pushButton_addChar = QtWidgets.QPushButton(self.groupBox_addChar)
        self.pushButton_addChar.setGeometry(QtCore.QRect(10, 50, 101, 28))
        self.pushButton_addChar.setObjectName("pushButton_addChar")
        self.checkBox_customChar = QtWidgets.QCheckBox(self.groupBox_addChar)
        self.checkBox_customChar.setGeometry(QtCore.QRect(180, 20, 111, 22))
        self.checkBox_customChar.setObjectName("checkBox_customChar")
        self.pushButton_addAllChar = QtWidgets.QPushButton(self.groupBox_addChar)
        self.pushButton_addAllChar.setGeometry(QtCore.QRect(180, 50, 111, 28))
        self.pushButton_addAllChar.setObjectName("pushButton_addAllChar")
        self.pushButton_clearChar = QtWidgets.QPushButton(self.groupBox_addChar)
        self.pushButton_clearChar.setGeometry(QtCore.QRect(120, 50, 51, 28))
        self.pushButton_clearChar.setObjectName("pushButton_clearChar")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.log_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.log_browser.setFont(font)
        self.log_browser.setGeometry(QtCore.QRect(240, 380, 571, 192))
        self.log_browser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.log_browser.setObjectName("log_browser")
        self.groupBox_porxy = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_porxy.setGeometry(QtCore.QRect(10, 450, 221, 61))
        self.groupBox_porxy.setObjectName("groupBox_porxy")
        self.gob_porxy = QtWidgets.QSpinBox(self.groupBox_porxy)
        self.gob_porxy.setGeometry(QtCore.QRect(130, 30, 81, 22))
        self.gob_porxy.setMaximum(65535)
        self.gob_porxy.setProperty("value", porxy)
        self.gob_porxy.setObjectName("gob_porxy")
        self.label_21 = QtWidgets.QLabel(self.groupBox_porxy)
        self.label_21.setGeometry(QtCore.QRect(10, 30, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run.setGeometry(QtCore.QRect(70, 520, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setObjectName("pushButton_run")
        
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(70, 520, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_stop.setVisible(False)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 30))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        
        self.debug = QtWidgets.QMenu(self.menubar)
        self.debug.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.debug.setToolTipDuration(5)
        self.debug.setToolTipsVisible(False)
        self.debug.setObjectName("debug")
        self.debug_action = QAction(MainWindow)
        self.debug_action.setCheckable(False)
        self.debug_action.setObjectName('debugAction')
        self.debug_action.setText('Debug模式')
        
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
        self.menubar.addAction(self.debug_action)
        self.menubar.addAction(self.about.menuAction())

        self.retranslateUi(MainWindow)
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
        MainWindow.setTabOrder(self.gob_porxy, self.table_Char)
        MainWindow.setTabOrder(self.table_Char, self.comboBox_addChar)
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
        MainWindow.setTabOrder(self.pushButton_charEdit, self.pushButton_run)
        MainWindow.setTabOrder(self.pushButton_run, self.log_browser)
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ArknightsCheater"))
        self.groupBox_userData.setTitle(_translate("MainWindow", "用户数据"))
        self.label_14.setText(_translate("MainWindow", "昵称编号:"))
        self.label_18.setText(_translate("MainWindow", "签名:"))
        self.label_16.setText(_translate("MainWindow", "理智:"))
        self.label_17.setText(_translate("MainWindow", "理智上限:"))
        self.label_13.setText(_translate("MainWindow", "昵称:"))
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
        self.groupBox_secretary.setTitle(_translate("MainWindow", "助理"))
        self.label_20.setText(_translate("MainWindow", "助理皮肤:"))
        self.label_19.setText(_translate("MainWindow", "助理:"))
        self.label_15.setText(_translate("MainWindow", "UID:"))
        self.label_22.setText(_translate("MainWindow", "等级:"))
        self.user_UID.setPlaceholderText(_translate("MainWindow", userUID))
        self.user_name.setPlaceholderText(_translate("MainWindow", userName))
        self.user_nameNum.setPlaceholderText(_translate("MainWindow", userNameNum))
        self.user_resume.setPlaceholderText(_translate("MainWindow", userResume))
        self.groupBox_charData.setTitle(_translate("MainWindow", "干员数据"))
        self.table_Char.setHorizontalHeaderLabels(['干员','ID','精英','等级','皮肤','信赖值','技能等级','选中技能','专精等级','潜能等级','操作'])
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
        self.checkBox_customBest.setText(_translate("MainWindow", "最好"))
        self.label_selectChar.setText(_translate("MainWindow", "请选择干员"))
        self.pushButton_charEdit.setText(_translate("MainWindow", "修改"))
        self.groupBox_addChar.setTitle(_translate("MainWindow", "添加干员"))
        self.checkBox_addBest.setText(_translate("MainWindow", "最好"))
        self.pushButton_addChar.setText(_translate("MainWindow", "添加干员"))
        self.checkBox_customChar.setText(_translate("MainWindow", "自定义干员"))
        self.pushButton_addAllChar.setText(_translate("MainWindow", "添加所有干员"))
        self.pushButton_clearChar.setText(_translate("MainWindow", "清空"))
        self.log_browser.setHtml(_translate("MainWindow", "<html><head></head><body bgcolor=#293134></body></html>"))
        self.groupBox_porxy.setTitle(_translate("MainWindow", "代理设置"))
        self.label_21.setText(_translate("MainWindow", "端口:"))
        self.pushButton_run.setText(_translate("MainWindow", "启动"))
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

def table_Char_selectChanged():
    index=Win.table_Char.currentIndex().row()
    charId=charList[int(Win.table_Char.item(index, 1).text())]
    Win.char_skin.clear()
    for e,skinId in enumerate(skinList[charId]):
        Win.char_skin.addItem(skinList[charId][skinId])
    if Win.checkBox_customBest.isChecked():
        Win.checkBox_customBest.setChecked(False)
    customChar_reload(index)
    char_eliteLv_changed()

def customChar_reload(index):
    charIndex=int(Win.table_Char.item(index, 1).text())
    charId=charList[charIndex]
    rarity=charTable[charId]['rarity']
    Win.label_selectChar.setText(charTable[charId]['name'])
    bestCharList=bestChar(charIndex)
    if DebugOff:
        Win.char_eliteLv.setMaximum(bestCharList[2])
        Win.char_Lv.setMaximum(bestCharList[3])
    Win.char_eliteLv.setValue(int(Win.table_Char.item(index, 2).text()))
    Win.char_Lv.setValue(int(Win.table_Char.item(index, 3).text()))
    for e,skinId in enumerate(skinList[charId]):
        if Win.table_Char.item(index, 4).text()==skinList[charId][skinId]:
            Win.char_skin.setCurrentIndex(e)
    Win.char_favorPoint.setValue(int(Win.table_Char.item(index, 5).text()))
    Win.char_skillLv.setValue(int(Win.table_Char.item(index, 6).text()))
    skillIn = Win.table_Char.item(index, 7).text()
    if skillIn in ['1','2','3']:
        Win.char_skillIndex.setEnabled(True)
        Win.char_skillIndex.setMaximum(int(bestCharList[7]))
        Win.char_skillIndex.setValue(int(skillIn))
    else:
        Win.char_skillIndex.setEnabled(False)
    Win.char_spLv.setValue(int(Win.table_Char.item(index, 8).text()))
    Win.char_potLv.setValue(int(Win.table_Char.item(index, 9).text()))

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
    index=Win.table_Char.currentIndex().row()
    charIndex=int(Win.table_Char.item(index, 1).text())
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
        Win.debug_action.setText('关闭Debug模式')
        
    else:
        DebugOff=True
        Win.user_Lv.setMaximum(120)
        Win.user_apMax.setMaximum(135)
        Win.char_skillLv.setMaximum(7)
        Win.char_eliteLv.setMaximum(2)
        charIndex=Win.table_Char.currentIndex().row()
        if charIndex!=-1:
            Win.char_eliteLv.setValue(bestChar(charIndex)[2])
            char_lv_reload()
        Win.char_spLv.setMaximum(3)
        Win.char_potLv.setMaximum(5)
        Win.debug_action.setText('Debug模式')

def run_and_exit():
    global isRun
    if isRun:
        isRun=False
        Win.pushButton_run.setText('停止')
        f=open('.\data.json', 'w', encoding='UTF-8')
        f.write(get_data())
        f.close
        Win.log_browser.append('<font color="red">ArknightsCheater:启动mitmproxy中...</font>')
        Win.thread = RunThread()
        Win.thread.update_log.connect(Win.update_logtext)
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
    global userUID,userName,userNameNum,userResume
    CustomCharTemp=''
    if not Win.user_UID.text()=='':
        userUID=Win.user_UID.text()
    if not Win.user_name.text()=='':
        userName=Win.user_name.text()
    if not Win.user_nameNum.text()=='':
        userNameNum=Win.user_nameNum.text()
    if not Win.user_resume.text()=='':
        userResume=Win.user_resume.text()
    
    cr_total=Win.table_Char.rowCount()
    for index in range(0,cr_total):
        cr_charId=charList[int(Win.table_Char.item(index, 1).text())]
        cr_eliteLv=int(Win.table_Char.item(index, 2).text())
        cr_lv=int(Win.table_Char.item(index, 3).text())
        for e,skinId in enumerate(skinList[cr_charId]):
            if Win.table_Char.item(index, 4).text()==skinList[cr_charId][skinId]:
                cr_skinId=skinId
        cr_favPt=int(Win.table_Char.item(index, 5).text())
        cr_skillLv=int(Win.table_Char.item(index, 6).text())
        cr_skillIn = Win.table_Char.item(index, 7).text()
        if cr_skillIn in ['1','2','3']:
            cr_skillIndex=int(cr_skillIn)-1
        else:
            cr_skillIndex=0
        cr_spLv = Win.table_Char.item(index, 8).text()
        cr_potLv = Win.table_Char.item(index, 9).text()
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
    data=[{
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
        'chars':{char}
    }]
    return str(data).replace('{\'"','{"').replace('}\'}','}}').replace('\'','"').replace('""','')[1:-1]

def bestChar(index):
    charId=charList[index]
    name=charTable[charId]['name']
    rarity=charTable[charId]['rarity']
    favorPoint=200
    skillLv=7
    spLv=3
    potLv=5
    skin=skinList[charId][charId+'#1']
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
        skin=skinList[charId][charId+'#2']
    elif rarity == 4:
        eliteLv=2
        Lv=80
        skin=skinList[charId][charId+'#2']
    elif rarity == 5:
        eliteLv=2
        Lv=90
        skin=skinList[charId][charId+'#2']
    return [name,index,eliteLv,Lv,skin,favorPoint,skillLv,skillIndex,spLv,potLv]
        
def addChar(index):
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
    Win.table_Char.setRowCount(tableCharLine)
    for e in range(len(item)):
        if e == 10:
            table_Char_del = QPushButton("删除")
            table_Char_del.clicked.connect(lambda:table_char_del())
            table_Char_del.setDown(True)
            table_Char_del.setStyleSheet("QPushButton{margin:3px};")
            Win.table_Char.setCellWidget(tableCharLine-1, e, table_Char_del)
        else:
            Win.table_Char.setItem(tableCharLine-1, e, QTableWidgetItem(str(item[e])))

def charEdit():
    if not checkSelectChar():
        return
    row=Win.table_Char.currentIndex().row()
    charIdIn=charList[int(Win.table_Char.item(row, 1).text())]
    Win.table_Char.setItem(row, 2, QTableWidgetItem(str(Win.char_eliteLv.value())))
    Win.table_Char.setItem(row, 3, QTableWidgetItem(str(Win.char_Lv.value())))
    for e,skinId in enumerate(skinList[charIdIn]):
        if Win.char_skin.currentIndex()==e:
            Win.table_Char.setItem(row, 4, QTableWidgetItem(skinList[charIdIn][skinId]))
    Win.table_Char.setItem(row, 5, QTableWidgetItem(str(Win.char_favorPoint.value())))
    Win.table_Char.setItem(row, 6, QTableWidgetItem(str(Win.char_skillLv.value())))
    if not Win.table_Char.item(row, 7).text()=='无技能':
        Win.table_Char.setItem(row, 7, QTableWidgetItem(str(Win.char_skillIndex.value())))
    Win.table_Char.setItem(row, 8, QTableWidgetItem(str(Win.char_spLv.value())))
    Win.table_Char.setItem(row, 9, QTableWidgetItem(str(Win.char_potLv.value())))

def checkSelectChar():
    row=Win.table_Char.currentIndex().row()
    if row==-1:
        QMessageBox.warning(Win,"错误","请选择干员",QMessageBox.Ok)
        return False
    else:
        return True

def charAddAll():
    table_char_delAll()
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

def import_data():
    global curDir,item
    fileName, filetype = QFileDialog.getOpenFileName(Win,"打开文件",curDir,"Arknights Cheat Data文件 (*.acdata)")
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
        secretary=j['secretary']
        Win.user_secretary.setCurrentIndex(charList.index(secretary))
        userSecretary_changed()
        for e,skinId in enumerate(skinList[secretary]):
            if skinList[secretary][j['secretarySkinId']]==skinList[secretary][skinId]:
                Win.user_secretarySkin.setCurrentIndex(e)
        item='['+str(j['item'])+']'
        for e in j['chars']:  
            charId=j['chars'][e]['charId']
            favPt=favorPointList.index(j['chars'][e]['favorPoint'])
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
        
def table_char_del():
    global tableCharLine
    tableCharLine=tableCharLine-1
    Win.table_Char.removeRow(Win.table_Char.currentIndex().row())

def table_char_delAll():
    global tableCharLine
    tableCharLine=0
    for e in range(Win.table_Char.rowCount()-1,-1,-1):
        Win.table_Char.removeRow(e)

def listItem_changed():
    Win.item_value.setValue(item[0][itemList[Win.list_item.currentRow()]])

def char_eliteLv_changed():
    if not checkSelectChar():
        return
    char_lv_reload()
    
def char_lv_reload():
    global DebugOff
    index=Win.table_Char.currentIndex().row()
    charIndex=int(Win.table_Char.item(index, 1).text())
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
if os.path.isfile('.\character_table.json'):   
    charTable=json.loads(open('.\character_table.json', 'r', encoding='UTF-8').read())
favorPointList = [0, 8, 16, 28, 40, 56, 72, 92, 112, 137, 162, 192, 222, 255, 288, 325, 362, 404, 446, 491, 536, 586, 636, 691, 746, 804, 862, 924, 986, 1052, 1118, 1184, 1250, 1316, 1382, 1457, 1532, 1607, 1682, 1757, 1832, 1917, 2002, 2087, 2172, 2257, 2352, 2447, 2542, 2637, 2732, 2840, 2960, 3080, 3200, 3320, 3450, 3580, 3710, 3840, 3970, 4110, 4250, 4390, 4530, 4670, 4820, 4970, 5120, 5270, 5420, 5575, 5730, 5885, 6040, 6195, 6350, 6505, 6660, 6815, 6970, 7125, 7280, 7435, 7590, 7745, 7900, 8055, 8210, 8365, 8520, 8675, 8830, 8985, 9140, 9295, 9450, 9605, 9760, 9915, 10070, 10225, 10380, 10535, 10690, 10845, 11000, 11155, 11310, 11465, 11620, 11775, 11930, 12085, 12240, 12395, 12550, 12705, 12860, 13015, 13170, 13325, 13480, 13635, 13790, 13945, 14100, 14255, 14410, 14565, 14720, 14875, 15030, 15185, 15340, 15495, 15650, 15805, 15960, 16115, 16270, 16425, 16580, 16735, 16890, 17045, 17200, 17355, 17510, 17665, 17820, 17975, 18130, 18285, 18440, 18595, 18750, 18905, 19060, 19215, 19370, 19525, 19680, 19835, 19990, 20145, 20300, 20455, 20610, 20765, 20920, 21075, 21230, 21385, 21540, 21695, 21850, 22005, 22160, 22315, 22470, 22625, 22780, 22935, 23090, 23245, 23400, 23555, 23710, 23865, 24020, 24175, 24330, 24485, 24640, 24795, 24950, 25105, 25260, 25415, 25570]
if os.path.isfile('.\skin_table.json'): 
    skinList=json.loads(skintable2list('.\skin_table.json'))
charList=[]
tableCharLine=0

def init():
    global charList
    for e,charId in enumerate(charTable):
        if charId[:4]=='char':
            charList.append(charId)
            Win.comboBox_addChar.addItem(charTable[charId]['name'])
            Win.user_secretary.addItem(charTable[charId]['name'])
    userSecretary_changed()

#link
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
    
    def closeEvent(self, event):
        dataJson = curDir+'\data.json'  # 文件路径
        if os.path.exists(dataJson):
            os.remove(dataJson)
        subprocess.Popen("taskkill /f /im mitmdump.exe>nul",shell=True)

    def resizeEvent(self, event):
        if self.width()>809 and self.height()>629:
            self.groupBox_charData.setGeometry(QtCore.QRect(240, 10, self.width()-245,361))
            self.groupBox_customChar.setGeometry(QtCore.QRect(self.groupBox_charData.width()-242, 20, 231, 331))
            self.checkBox_addBest.setGeometry(QtCore.QRect(int((self.groupBox_addChar.width()-111-91-70)/2)+106, 20, 61, 22))
            self.pushButton_clearChar.setGeometry(QtCore.QRect(int((self.groupBox_addChar.width()-111-91-70)/2)+106, 50, 51, 28))
            self.table_Char.setGeometry(QtCore.QRect(10, 30, self.groupBox_charData.width()-self.groupBox_customChar.width()-30, 221))
            self.groupBox_addChar.setGeometry(QtCore.QRect(10, 260, self.groupBox_charData.width()-self.groupBox_customChar.width()-30, 91))
            self.checkBox_customChar.setGeometry(QtCore.QRect(self.groupBox_addChar.width()-121, 20, 111, 22))
            self.pushButton_addAllChar.setGeometry(QtCore.QRect(self.groupBox_addChar.width()-121, 50, 111, 28))
        self.log_browser.setGeometry(QtCore.QRect(240, 380, self.width()-240,self.height()-380-59))
        QtWidgets.QWidget.resizeEvent(self, event)
    
    def update_logtext(self, str):
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
        mitmRun = subprocess.Popen('mitmdump.exe -s .\main.py --ssl-insecure -p '+str(Win.gob_porxy.value())+' --no-http2', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
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
    
    if not os.path.isfile('.\character_table.json'):
        QMessageBox.warning(Win,"错误","请将character_table.json放入同目录下",QMessageBox.Ok)
        webbrowser.open_new_tab('https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/character_table.json')
        sys.exit()
    elif not os.path.isfile('.\skin_table.json'):
        QMessageBox.warning(Win,"错误","请将skin_table.json放入同目录下",QMessageBox.Ok)
        webbrowser.open_new_tab('https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/skin_table.json')
        sys.exit()
    elif not os.path.isfile('.\mitmdump.exe'):
        QMessageBox.warning(Win,"错误","请将mitmdump.exe放入同目录下",QMessageBox.Ok)
        webbrowser.open_new_tab('https://mitmproxy.org/downloads/')
        sys.exit()
    elif not os.path.isfile('.\main.py'):
        QMessageBox.warning(Win,"错误","请将main.py放入同目录下",QMessageBox.Ok)
        webbrowser.open_new_tab('https://github.com/Tao0Lu/Arknights-Cheater/blob/master/main.py')
        sys.exit()
    init()
    
    Win.show()
    
    Win.pushButton_run.clicked.connect(lambda:run_and_exit())
    Win.pushButton_addChar.clicked.connect(lambda:addChar(Win.comboBox_addChar.currentIndex()))
    Win.pushButton_itemEdit.clicked.connect(lambda:itemEdit_clicked())
    Win.pushButton_charEdit.clicked.connect(lambda:charEdit())
    Win.pushButton_addAllChar.clicked.connect(lambda:charAddAll())
    Win.pushButton_clearChar.clicked.connect(lambda:table_char_delAll())
    
    Win.action_exit.triggered.connect(lambda:sys.exit())
    Win.debug_action.triggered.connect(lambda:debug())
    Win.action_export.triggered.connect(lambda:export_data())
    Win.action_import.triggered.connect(lambda:import_data())
    Win.action_help.triggered.connect(lambda:help())
    Win.action_notice.triggered.connect(lambda:notice())
    
    Win.table_Char.itemClicked.connect(lambda:table_Char_selectChanged())
    
    Win.checkBox_customChar.stateChanged.connect(lambda:checkBoxCustomChar_changed())
    Win.checkBox_customBest.stateChanged.connect(lambda:checkBoxCustomBest_changed())

    Win.list_item.itemClicked.connect(lambda:listItem_changed())

    Win.char_eliteLv.valueChanged.connect(lambda:char_eliteLv_changed())
    Win.char_Lv.valueChanged.connect(lambda:checkSelectChar())
    Win.char_favorPoint.valueChanged.connect(lambda:checkSelectChar())
    Win.char_skillLv.valueChanged.connect(lambda:checkSelectChar())
    Win.char_skillIndex.valueChanged.connect(lambda:checkSelectChar())
    Win.char_spLv.valueChanged.connect(lambda:checkSelectChar())
    Win.char_potLv.valueChanged.connect(lambda:checkSelectChar())
    
    Win.user_secretary.activated.connect(lambda:userSecretary_changed())
    sys.exit(app.exec_())
