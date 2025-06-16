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
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGraphicsView, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QSplitter, QVBoxLayout, QWidget)

from orso_tools.mpl_canvas import MplCanvas

from .model_editor import ModelEditor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1256, 927)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget_2 = QWidget(self.splitter)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName("label")
        font = QFont()
        font.setFamilies(["Courier New"])
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.model_editor = ModelEditor(self.widget_2)
        self.model_editor.setObjectName("model_editor")
        self.model_editor.setAcceptRichText(False)

        self.verticalLayout.addWidget(self.model_editor)

        self.splitter.addWidget(self.widget_2)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.model_builder = QGraphicsView(self.frame)
        self.model_builder.setObjectName("model_builder")

        self.verticalLayout_3.addWidget(self.model_builder)

        self.splitter.addWidget(self.frame)

        self.verticalLayout_6.addWidget(self.splitter)

        self.update_button = QPushButton(self.widget)
        self.update_button.setObjectName("update_button")

        self.verticalLayout_6.addWidget(self.update_button)

        self.verticalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graph_refl = MplCanvas(self.dockWidgetContents)
        self.graph_refl.setObjectName("graph_refl")

        self.verticalLayout_4.addWidget(self.graph_refl)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget)
        self.dockWidget_2 = QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graph_sld = MplCanvas(self.dockWidgetContents_2)
        self.graph_sld.setObjectName("graph_sld")

        self.verticalLayout_5.addWidget(self.graph_sld)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget_2)

        self.retranslateUi(MainWindow)
        self.update_button.pressed.connect(MainWindow.update_model)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", "Open...", None))
        self.label.setText(
            QCoreApplication.translate("MainWindow", "data_source:\n" "   sample:\n" "     model:", None)
        )
        self.update_button.setText(QCoreApplication.translate("MainWindow", "Update Model", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", "Reflectivity", None))
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("MainWindow", "SLD Profile", None))

    # retranslateUi
