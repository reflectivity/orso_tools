# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QListWidget, QListWidgetItem, QMainWindow, QMenu, QMenuBar,
                               QSizePolicy, QSplitter, QStatusBar, QTabWidget, QTextBrowser, QTreeView, QVBoxLayout,
                               QWidget)

from .mpl_canvas import MplCanvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(945, 634)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.dataset_list = QListWidget(self.splitter)
        self.dataset_list.setObjectName("dataset_list")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataset_list.sizePolicy().hasHeightForWidth())
        self.dataset_list.setSizePolicy(sizePolicy)
        self.dataset_list.setMinimumSize(QSize(120, 0))
        self.splitter.addWidget(self.dataset_list)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.plot_tab = QWidget()
        self.plot_tab.setObjectName("plot_tab")
        self.verticalLayout = QVBoxLayout(self.plot_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.data_plot = MplCanvas(self.plot_tab)
        self.data_plot.setObjectName("data_plot")

        self.verticalLayout.addWidget(self.data_plot)

        self.tabWidget.addTab(self.plot_tab, "")
        self.header_tab = QWidget()
        self.header_tab.setObjectName("header_tab")
        self.verticalLayout_3 = QVBoxLayout(self.header_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_2 = QSplitter(self.header_tab)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.header_tree = QTreeView(self.splitter_2)
        self.header_tree.setObjectName("header_tree")
        self.splitter_2.addWidget(self.header_tree)
        self.header_data = QTextBrowser(self.splitter_2)
        self.header_data.setObjectName("header_data")
        self.splitter_2.addWidget(self.header_data)

        self.verticalLayout_3.addWidget(self.splitter_2)

        self.tabWidget.addTab(self.header_tab, "")
        self.sample_tab = QWidget()
        self.sample_tab.setObjectName("sample_tab")
        self.tabWidget.addTab(self.sample_tab, "")
        self.splitter.addWidget(self.tabWidget)

        self.verticalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 945, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)
        self.dataset_list.currentRowChanged.connect(MainWindow.dataset_selected)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", "Open...", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.plot_tab), QCoreApplication.translate("MainWindow", "Data", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.header_tab),
            QCoreApplication.translate("MainWindow", "Header Information", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.sample_tab), QCoreApplication.translate("MainWindow", "Sample", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))

    # retranslateUi
