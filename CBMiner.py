from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle, sys, subprocess, os, json, time as t, platform, multiprocessing, threading, requests, datetime
from subprocess import DEVNULL, STDOUT, check_call, check_output



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 604)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Umpush")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Umpush")
        self.tabWidget.setFont(font)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.Mining = QtWidgets.QPushButton(self.Home)
        self.Mining.setEnabled(False)
        self.Mining.setGeometry(QtCore.QRect(280, 110, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Mining.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/tstartminingicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Mining.setIcon(icon)
        self.Mining.setIconSize(QtCore.QSize(64, 64))
        self.Mining.setObjectName("Mining")
        self.Benchmark = QtWidgets.QPushButton(self.Home)
        self.Benchmark.setGeometry(QtCore.QRect(330, 40, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Benchmark.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/tspeedicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Benchmark.setIcon(icon1)
        self.Benchmark.setIconSize(QtCore.QSize(32, 32))
        self.Benchmark.setObjectName("Benchmark")
        self.progressBar = QtWidgets.QProgressBar(self.Home)
        self.progressBar.setGeometry(QtCore.QRect(7, 460, 781, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.label_7 = QtWidgets.QLabel(self.Home)
        self.label_7.setGeometry(QtCore.QRect(370, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.coinselectingcombo = QtWidgets.QComboBox(self.Home)
        self.coinselectingcombo.setEnabled(False)
        self.coinselectingcombo.setGeometry(QtCore.QRect(360, 250, 81, 27))
        self.coinselectingcombo.setObjectName("coinselectingcombo")
        self.coinselectingcombo.addItem("")
        self.coinselectingcombo.addItem("")
        self.coinselectingcombo.addItem("")
        self.coinselectingcombo.addItem("")
        self.coinselectingcombo.addItem("")
        self.coinselectingcombo.addItem("")
        self.coinselectingcombo.addItem("")
        self.coinselectingcombo.addItem("")
        self.noticeautomine = QtWidgets.QLabel(self.Home)
        self.noticeautomine.setGeometry(QtCore.QRect(200, 290, 421, 20))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(12)
        self.noticeautomine.setFont(font)
        self.noticeautomine.setObjectName("noticeautomine")
        self.youare = QtWidgets.QLabel(self.Home)
        self.youare.setGeometry(QtCore.QRect(100, 320, 211, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.youare.sizePolicy().hasHeightForWidth())
        self.youare.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.youare.setFont(font)
        self.youare.setObjectName("youare")
        self.sollcd = QtWidgets.QLCDNumber(self.Home)
        self.sollcd.setGeometry(QtCore.QRect(340, 310, 91, 51))
        self.sollcd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sollcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sollcd.setLineWidth(2)
        self.sollcd.setSmallDecimalPoint(True)
        self.sollcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.sollcd.setObjectName("sollcd")
        self.persecond = QtWidgets.QLabel(self.Home)
        self.persecond.setGeometry(QtCore.QRect(440, 320, 211, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.persecond.sizePolicy().hasHeightForWidth())
        self.persecond.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.persecond.setFont(font)
        self.persecond.setObjectName("persecond")
        self.andmaking = QtWidgets.QLabel(self.Home)
        self.andmaking.setGeometry(QtCore.QRect(90, 380, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.andmaking.sizePolicy().hasHeightForWidth())
        self.andmaking.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.andmaking.setFont(font)
        self.andmaking.setObjectName("andmaking")
        self.moneylcd = QtWidgets.QLCDNumber(self.Home)
        self.moneylcd.setGeometry(QtCore.QRect(240, 370, 91, 51))
        self.moneylcd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.moneylcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.moneylcd.setLineWidth(2)
        self.moneylcd.setSmallDecimalPoint(True)
        self.moneylcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.moneylcd.setObjectName("moneylcd")
        self.money = QtWidgets.QLabel(self.Home)
        self.money.setGeometry(QtCore.QRect(350, 380, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.money.sizePolicy().hasHeightForWidth())
        self.money.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.money.setFont(font)
        self.money.setObjectName("money")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Downloads/thomeicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Home, icon2, "")
        self.Address = QtWidgets.QWidget()
        self.Address.setObjectName("Address")
        self.Savebutton = QtWidgets.QPushButton(self.Address)
        self.Savebutton.setGeometry(QtCore.QRect(630, 390, 99, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Savebutton.sizePolicy().hasHeightForWidth())
        self.Savebutton.setSizePolicy(sizePolicy)
        self.Savebutton.setObjectName("Savebutton")
        self.tableWidget = QtWidgets.QTableWidget(self.Address)
        self.tableWidget.setGeometry(QtCore.QRect(100, 40, 100, 299))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(32)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.Addresstable = QtWidgets.QTableWidget(self.Address)
        self.Addresstable.setGeometry(QtCore.QRect(210, 40, 380, 299))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Addresstable.setFont(font)
        self.Addresstable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Addresstable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Addresstable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Addresstable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Addresstable.setAutoScroll(False)
        self.Addresstable.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.Addresstable.setDragDropOverwriteMode(False)
        self.Addresstable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.Addresstable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.Addresstable.setWordWrap(True)
        self.Addresstable.setCornerButtonEnabled(True)
        self.Addresstable.setRowCount(8)
        self.Addresstable.setObjectName("Addresstable")
        self.Addresstable.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Addresstable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Addresstable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Addresstable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Addresstable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Addresstable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Addresstable.setHorizontalHeaderItem(0, item)
        self.Addresstable.horizontalHeader().setStretchLastSection(True)
        self.Addresstable.verticalHeader().setVisible(False)
        self.Addresstable.verticalHeader().setDefaultSectionSize(32)
        self.Addresstable.verticalHeader().setStretchLastSection(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Downloads/tfileicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Address, icon3, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.gridLayoutWidget = QtWidgets.QWidget(self.Settings)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 781, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Currencycombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Currencycombo.sizePolicy().hasHeightForWidth())
        self.Currencycombo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Currencycombo.setFont(font)
        self.Currencycombo.setObjectName("Currencycombo")
        self.Currencycombo.addItem("")
        self.Currencycombo.addItem("")
        self.Currencycombo.addItem("")
        self.gridLayout.addWidget(self.Currencycombo, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.Themecombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Themecombo.sizePolicy().hasHeightForWidth())
        self.Themecombo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Themecombo.setFont(font)
        self.Themecombo.setObjectName("Themecombo")
        self.Themecombo.addItem("")
        self.Themecombo.addItem("")
        self.gridLayout.addWidget(self.Themecombo, 0, 3, 1, 1)
        self.Autocombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Autocombo.sizePolicy().hasHeightForWidth())
        self.Autocombo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Autocombo.setFont(font)
        self.Autocombo.setObjectName("Autocombo")
        self.Autocombo.addItem("")
        self.Autocombo.addItem("")
        self.gridLayout.addWidget(self.Autocombo, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStatusTip("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.Minercombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Minercombo.sizePolicy().hasHeightForWidth())
        self.Minercombo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Minercombo.setFont(font)
        self.Minercombo.setObjectName("Minercombo")
        self.Minercombo.addItem("")
        self.Minercombo.addItem("")
        self.Minercombo.addItem("")
        self.gridLayout.addWidget(self.Minercombo, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.Regioncombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Regioncombo.sizePolicy().hasHeightForWidth())
        self.Regioncombo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Regioncombo.setFont(font)
        self.Regioncombo.setObjectName("Regioncombo")
        self.Regioncombo.addItem("")
        self.Regioncombo.addItem("")
        self.gridLayout.addWidget(self.Regioncombo, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.Goalcombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Goalcombo.sizePolicy().hasHeightForWidth())
        self.Goalcombo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Goalcombo.setFont(font)
        self.Goalcombo.setObjectName("Goalcombo")
        self.Goalcombo.addItem("")
        self.Goalcombo.addItem("")
        self.gridLayout.addWidget(self.Goalcombo, 2, 3, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../Downloads/tsettingsicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Settings, icon4, "")
        self.Advanced = QtWidgets.QWidget()
        self.Advanced.setObjectName("Advanced")
        self.label_8 = QtWidgets.QLabel(self.Advanced)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 321, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.swaphours = QtWidgets.QSpinBox(self.Advanced)
        self.swaphours.setGeometry(QtCore.QRect(400, 30, 71, 27))
        self.swaphours.setPrefix("")
        self.swaphours.setMaximum(1000)
        self.swaphours.setProperty("value", 1)
        self.swaphours.setObjectName("swaphours")
        self.label_10 = QtWidgets.QLabel(self.Advanced)
        self.label_10.setGeometry(QtCore.QRect(30, 130, 331, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.profitabilityswap = QtWidgets.QDoubleSpinBox(self.Advanced)
        self.profitabilityswap.setGeometry(QtCore.QRect(390, 130, 69, 27))
        self.profitabilityswap.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.profitabilityswap.setAccelerated(False)
        self.profitabilityswap.setPrefix("")
        self.profitabilityswap.setDecimals(1)
        self.profitabilityswap.setProperty("value", 5.0)
        self.profitabilityswap.setObjectName("profitabilityswap")
        self.label_11 = QtWidgets.QLabel(self.Advanced)
        self.label_11.setGeometry(QtCore.QRect(30, 240, 311, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.exactness = QtWidgets.QSpinBox(self.Advanced)
        self.exactness.setGeometry(QtCore.QRect(410, 240, 48, 27))
        self.exactness.setMinimum(1)
        self.exactness.setMaximum(10)
        self.exactness.setObjectName("exactness")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../Downloads/tadvancedicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Advanced, icon5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Mining.setText(_translate("MainWindow", "Start Mining!"))
        self.Benchmark.setToolTip(_translate("MainWindow", "Exactness can be adjusted in the \"Advanced\" tab"))
        self.Benchmark.setText(_translate("MainWindow", "Benchmark"))
        self.progressBar.setFormat(_translate("MainWindow", "%p% Benchmarking"))
        self.label_7.setText(_translate("MainWindow", "Coin"))
        self.coinselectingcombo.setItemText(0, _translate("MainWindow", "BTG"))
        self.coinselectingcombo.setItemText(1, _translate("MainWindow", "HUSH"))
        self.coinselectingcombo.setItemText(2, _translate("MainWindow", "KMD"))
        self.coinselectingcombo.setItemText(3, _translate("MainWindow", "BTCZ"))
        self.coinselectingcombo.setItemText(4, _translate("MainWindow", "ZEL"))
        self.coinselectingcombo.setItemText(5, _translate("MainWindow", "CMM"))
        self.coinselectingcombo.setItemText(6, _translate("MainWindow", "BTCP"))
        self.coinselectingcombo.setItemText(7, _translate("MainWindow", "RVN"))
        self.noticeautomine.setText(_translate("MainWindow", "Disable Automining in the settings to choose manually"))
        self.youare.setText(_translate("MainWindow", "You are mining at "))
        self.persecond.setText(_translate("MainWindow", "H/sol per second"))
        self.andmaking.setText(_translate("MainWindow", "And making"))
        self.money.setText(_translate("MainWindow", " "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("MainWindow", "Home"))
        self.Savebutton.setText(_translate("MainWindow", "Save"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Coin"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "BTG"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "HUSH"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "KMD"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "BTCZ"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "ZEL"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "CMM"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "BTCP"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "RVN"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.Addresstable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Addresstable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Addresstable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Addresstable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Addresstable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Addresstable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Address), _translate("MainWindow", "Address"))
        self.Currencycombo.setItemText(0, _translate("MainWindow", "BTC"))
        self.Currencycombo.setItemText(1, _translate("MainWindow", "EUR"))
        self.Currencycombo.setItemText(2, _translate("MainWindow", "USD"))
        self.label.setText(_translate("MainWindow", "Miner"))
        self.label_5.setText(_translate("MainWindow", "Main Currency"))
        self.label_6.setText(_translate("MainWindow", "Theme"))
        self.Themecombo.setItemText(0, _translate("MainWindow", "Light"))
        self.Themecombo.setItemText(1, _translate("MainWindow", "Dark"))
        self.Autocombo.setItemText(0, _translate("MainWindow", "ON"))
        self.Autocombo.setItemText(1, _translate("MainWindow", "OFF"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>When turned on this will automatically switch to the coin that fits your goal the most. You can change the goal with the option to the right.</p></body></html>"))
        self.label_3.setWhatsThis(_translate("MainWindow", "When turned on this will automatically switch to the coin that fits your goal the most. You can change the goal with the option to the right."))
        self.label_3.setText(_translate("MainWindow", "Automining"))
        self.Minercombo.setItemText(0, _translate("MainWindow", "EFWB miner"))
        self.Minercombo.setItemText(1, _translate("MainWindow", "DSTM miner"))
        self.Minercombo.setItemText(2, _translate("MainWindow", "CBMiner"))
        self.label_2.setText(_translate("MainWindow", "Region"))
        self.Regioncombo.setItemText(0, _translate("MainWindow", "EU"))
        self.Regioncombo.setItemText(1, _translate("MainWindow", "US"))
        self.label_4.setText(_translate("MainWindow", "Goal"))
        self.Goalcombo.setItemText(0, _translate("MainWindow", "Profit"))
        self.Goalcombo.setItemText(1, _translate("MainWindow", "Coin ammount"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))
        self.label_8.setText(_translate("MainWindow", "More profit check frequency"))
        self.swaphours.setSuffix(_translate("MainWindow", " h"))
        self.label_10.setText(_translate("MainWindow", "Swap at % more profitability"))
        self.profitabilityswap.setSuffix(_translate("MainWindow", "%"))
        self.label_11.setText(_translate("MainWindow", "Benchmark Exactness 1-10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Advanced), _translate("MainWindow", "Advanced"))


class CBMiner(Ui_MainWindow):
	def __init__(self, MainWindow):
		Ui_MainWindow.__init__(self)
		self.setupUi(MainWindow)
		MainWindow.setFixedSize(MainWindow.size())
		# MainWindow.setWindowIcon(QtGui.QIcon("coinblockers.png"))
		try:
			os.system("killall -9 miner")
		except Exception:
			pass



		

		self.progressBar.hide()
		self.youare.hide()
		self.persecond.hide()
		self.sollcd.hide()
		self.andmaking.hide()
		self.moneylcd.hide()
		self.money.hide()




		# defaults:


		# load config file
		with open("config.json","r") as f:
			self.config = json.load(f)
		# get todays date
		today = datetime.date.today()
		# check if time has past since the last conversion rates update. If so update them
		if self.config["Conversion"]["time"] != str(today):
			# get data from api and parse
			self.usdtoeuro = float(self.get_data("http://apilayer.net/api/live?access_key=3fd1a210f65c7ea120f5a5625aa0a6aa&currencies=EUR,GBP&source=USD&format=1")["quotes"]["USDEUR"])
			self.config["Conversion"]["time"] = str(today)
			self.config["Conversion"]["conversion"] = self.usdtoeuro
			print("new conversion data pulled")

		else:
			# if not enough time has passed (1 day) load the still up to date values
			self.usdtoeuro = self.config["Conversion"]["conversion"]

		# check if a benchmark has been made
		if self.config["Benchmark"]["Hashrate"] != "":
			# allow mining and load values
			self.Mining.setEnabled(True)
			self.averagehash = self.config["Benchmark"]["Hashrate"]

		else:
			# keep mining forbiden and set the average to 0
			self.averagehash = "0"

		# save any changes to the config file
		with open("./config.json","w") as f:
			print(json.dumps(self.config,indent=4),file=f)

		# setting the addresses

		# get number of rows incase more are added later
		allrows = self.Addresstable.rowCount()

		for r in range(0,allrows):
			# load the address for each coin from the config file
			self.Addresstable.setItem(r,0, QtWidgets.QTableWidgetItem(self.config["Address"][self.tableWidget.item(r,0).text()]))


		# set profitcheck spinbox to saved value
		self.swaphours.setValue(self.config["Profit"]["Timer"])

		# set all the default settings
		self.theme = "Light"
		self.region = "EU"
		self.goal = "Profit"
		self.automining = "ON"
		self.maincurrency = "BTC"
		self.miner = "EFWB miner"
		self.workername = "worker1"
		self.ammining = False
		self.ambenching = False

		#Timer for getting average hashrate
		self._updatetimer = QtCore.QTimer()
		self._updatetimer.timeout.connect(self.get_hash)

		#Timer for getting the most profitable coin
		self._profittimer = QtCore.QTimer()
		self._profittimer.timeout.connect(self.choosebestcoin)

		#Timer for performing a benchmark
		self._benchmarktimer = QtCore.QTimer()
		self._benchmarktimer.timeout.connect(self.startbenchmark)

		#connecting all widgets
		self.Minercombo.currentIndexChanged.connect(self.minerchange)
		self.Regioncombo.currentIndexChanged.connect(self.regionchange)
		self.Currencycombo.currentIndexChanged.connect(self.currencychange)
		self.Autocombo.currentIndexChanged.connect(self.autochange)
		self.Goalcombo.currentIndexChanged.connect(self.goalchange)
		self.Themecombo.currentIndexChanged.connect(self.themechange)

		self.swaphours.valueChanged.connect(self.swapchange)

		self.Savebutton.clicked.connect(self.saveaddress)

		self.Benchmark.clicked.connect(self.startbenchmark)

		self.Mining.clicked.connect(self.startmining)





	def startmining(self):
		# function that starts the mining process
		if self.ammining or self.ambenching:
			self.killminer()
		else:
			self._profittimer.start(self.config["Profit"]["Timer"]*1000*60*60)

			self.i = 0
			self.avhash = [0]
			self.Mining.setText("Stop Mining")
			self.Benchmark.setEnabled(False)
			if self.automining == "OFF":
				self.mine(self.coinselectingcombo.currentText())
			else:
				self.choosebestcoin()

	def choosebestcoin(self):
		# function that chooses the best coin based on the goal. Only used if automining is turned on
		high = (0,0)
		# query apis for all data from coins
		for i in ["BTG","HUSH","KMD","BTCP","BTCZ"]:
			if i == "BTG":
				data = self.get_data("https://whattomine.com/coins/214.json")
			if i == "HUSH":
				data = self.get_data("https://whattomine.com/coins/168.json")
			if i == "KMD":
				data = self.get_data("https://whattomine.com/coins/174.json")
			if i == "BTCP":
				data = self.get_data("https://whattomine.com/coins/230.json")
			if i == "BTCZ":
				data = self.get_data("https://whattomine.com/coins/207.json")


			blocktime = float(data["block_time"])
			blockreward = float(data["block_reward"])
			networkhashrate = float(data["nethash"])
			exchange = float(data["exchange_rate"])

			# get values for BTCZ and BTCP as Whattomine didnt have any price values
			if i == "BTCZ":
				data = self.get_data("https://api.coinmarketcap.com/v1/ticker/bitcoinz/")
				exchange = float(data[0]["price_btc"])
			if i == "BTCP":
				data = self.get_data("https://api.coinmarketcap.com/v1/ticker/bitcoin-private/")
				exchange = float(data[0]["price_btc"])


			# get btc to usd conversion rate from coinmarketcap
			btctousd = float(self.get_data("https://api.coinmarketcap.com/v1/ticker/bitcoin/")[0]["price_usd"])

			# calculate different earnings
			timetoblock = (networkhashrate / int(self.averagehash) * blocktime)/(24 * 60 * 60)
			coinperday = blockreward/timetoblock
			btcperday = exchange*coinperday
			usdperday = btctousd*btcperday
			europerday = usdperday*self.usdtoeuro


			# select the correct output currency based on the settings
			if self.maincurrency == "BTC":
				moneyperday = btcperday

			
			elif self.maincurrency == "USD":
				moneyperday = usdperday
			elif self.maincurrency == "EUR":
				moneyperday = europerday

			
			if self.goal == "Profit":
				if moneyperday > high[0]:
					high = (moneyperday,i)

			else:
				if coinperday > high[0]:
					high = (coinperday,i)

		self.ammining = True
		self.coinselectingcombo.setCurrentText(high[1])
		self.andmaking.show()
		self.moneylcd.show()
		self.money.show()
		self.moneylcd.display(high[0])
		if self.goal == "Profit":
			self.money.setText(self.maincurrency+" per day")
		else:
			self.money.setText(" "+high[1]+"/day")
		self._updatetimer.start()
		self.mine(high[1])
		print(str(t.ctime())+" | "+str(high))

	def get_hash(self):
		# function for monitoring and averaging the hashrate gets called ever second
		## ONLY WORKS FOR ONE OF THE MINERS ##
		hashrate = 0
		# get hashrate from internal api
		try:
			data = self.get_data("127.0.0.1:1111/getstat")

			for i in data["result"]:
				# add values from multiple gpus
				hashrate = hashrate+int(i["speed_sps"])
			self.avhash.append(int(hashrate))
		except Exception:
			pass
		self.youare.show()
		self.persecond.show()
		self.sollcd.show()
		self.sollcd.display(int(hashrate))
		# update progress bar
		if self.ambenching:
			self.i+=1
			self.progressBar.setValue(self.i)
			# calculate average hashrate and save to file
			if self.i == 100:
				self.averagehash = int(sum(self.avhash)/len(self.avhash))
				with open("config.json","r") as f:
					fulldict = json.load(f)
				fulldict["Benchmark"]["Hashrate"] = self.averagehash
				with open("./config.json","w") as f:
					print(json.dumps(fulldict,indent=4),file=f)
				#cleanup
				self.killminer()
				self.progressBar.hide()
				self.Mining.setEnabled(True)
				self._updatetimer.stop()

	def startbenchmark(self):
		self.ambenching = True
		# function for starting the benchmarking process
		if self.ammining or self.ammining:
			self.killminer()
		else:
			self.avhash = [0]
			self.i = 0
			self.Mining.setEnabled(False)
			# exactness makes the benchmarking timeframe bigger and thereby makes the average more acurate
			self._updatetimer.start(1000*self.exactness.value())
			self.progressBar.show()
			self.mine("BTG")
			self.Benchmark.setText("Cancel")

	def themechange(self):
		# function for changing the theme of the window
		self.theme = self.Themecombo.currentText()
		if self.theme == "Light":
			app.setStyleSheet("")
		elif self.theme == "Dark":
			app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	# setting internal values for easier handling
	##
	def goalchange(self):
		self.goal = self.Goalcombo.currentText()

	def autochange(self):
		self.automining = self.Autocombo.currentText()
		if self.automining == "OFF":
			self.noticeautomine.hide()
			self.coinselectingcombo.setEnabled(True)
		if self.automining == "ON":
			self.noticeautomine.show()
			self.coinselectingcombo.setEnabled(False)

	def currencychange(self):
		self.maincurrency = self.Currencycombo.currentText()

	def regionchange(self):
		self.region = str(self.Regioncombo.currentText())

	def minerchange(self):
		self.miner = self.Minercombo.currentText()
	
	def swapchange(self):
		self._profittimer.stop()
		if self.swaphours.value != 0:
			self._profittimer.start(self.swaphours.value()*1000*60*60)
		self.config["Profit"]["Timer"] = self.swaphours.value()
		with open("./config.json","w") as f:
			print(json.dumps(self.config,indent=4),file=f)

	##

	def killminer(self):
		#kills the miner and cleans up
		try:
			os.system("killall -9 miner")
			os.system("killall -9 zm")
		except Exception:
			pass
		self.ambenching = False
		self.youare.hide()
		self.sollcd.hide()
		self.persecond.hide()
		self.andmaking.hide()
		self.moneylcd.hide()
		self.money.hide()
		self.Benchmark.setEnabled(True)
		self._updatetimer.stop()
		self.progressBar.hide()
		self.progressBar.setValue(0)
		self.ammining = False
		self.Benchmark.setText("Benchmark")
		self.Mining.setText("Start Mining!")

	def mine(self, coin):
		# funtion for mining a coin based on the arguments
		try:
			os.system("killall -9 miner")
			os.system("killall -9 zm")
		except Exception:
			pass

		with open("./config.json") as f:
			self.config = json.load(f)


		self.noticeautomine.hide()
		#example command: ./miner --server eu-de01.miningrigrentals.com --port 3333 --user Leterax.73309 --pass x --api 192.168.2.70:1111
		if self.miner == "EFWB miner":
			command = "'"+cwd+"/miner"+"'"+str(" --server "+self.config["Pool"][coin]["Stratums"][self.region] + " --port "+ str(self.config["Pool"][coin]["Port"]) + \
			" --user " + self.config["Address"][coin]+"."+ self.workername +" --pass x")+" --api 127.0.0.1:1111 >/dev/null 2>&1"
		if self.miner == "DSTM miner":
			command = "'"+cwd+"/zm"+"'"+""+" --server "+self.config["Pool"][coin]["Stratums"][self.region] + " --port "+ str(self.config["Pool"][coin]["Port"]) + \
			" --user " + self.config["Address"][coin]+"."+ self.workername +" --pass x --telemetry=127.0.0.1:1111 >/dev/null 2>&1"

		# print(command)
		process = subprocess.Popen([command], shell=True)
		self.ammining = True

	def saveaddress(self):
		# after addresses have been eddited here they are saved
		i=0
		with open("config.json","r") as f:
			fulldict = json.load(f)

		addresses = []
		allrows = self.Addresstable.rowCount()
		for r in range(0,allrows):
			addresses.append(self.Addresstable.item(r,0).text())
		for key in fulldict["Address"]:
			fulldict["Address"][key]=addresses[i]
			i+=1

		with open("./config.json","w") as f:
			print(json.dumps(fulldict,indent=4),file=f)

	def get_data(self, link):
		# function for fetching data from json apis and parsing them to a python dict
		data = requests.get(link)
		data_text = data.text
		json_acceptable_string = data_text.replace('"', "\"")
		data = json.loads(json_acceptable_string)

		return data




cwd = os.path.dirname(sys.argv[0])
cwd = os.path.abspath(cwd)

# Start main Qt app
app = QtWidgets.QApplication(sys.argv)
# app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
MainWindow = QtWidgets.QMainWindow()
prog = CBMiner(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
