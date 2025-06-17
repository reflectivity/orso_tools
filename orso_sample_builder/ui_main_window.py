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
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QFrame, QHBoxLayout, QLabel, QMainWindow,
                               QPushButton, QSizePolicy, QSpacerItem, QSplitter, QToolButton, QVBoxLayout, QWidget)

from orso_tools.mpl_canvas import MplCanvas
from orso_tools.sample_viewer import SampleViewer

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

        self.editor_toolbar = QFrame(self.widget_2)
        self.editor_toolbar.setObjectName("editor_toolbar")
        self.editor_toolbar.setFrameShape(QFrame.StyledPanel)
        self.editor_toolbar.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.editor_toolbar)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.button_layer = QToolButton(self.editor_toolbar)
        self.button_layer.setObjectName("button_layer")

        self.horizontalLayout.addWidget(self.button_layer)

        self.button_material = QToolButton(self.editor_toolbar)
        self.button_material.setObjectName("button_material")

        self.horizontalLayout.addWidget(self.button_material)

        self.button_composit = QToolButton(self.editor_toolbar)
        self.button_composit.setObjectName("button_composit")

        self.horizontalLayout.addWidget(self.button_composit)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.button_substack = QToolButton(self.editor_toolbar)
        self.button_substack.setObjectName("button_substack")

        self.horizontalLayout.addWidget(self.button_substack)

        self.complex_selector = QComboBox(self.editor_toolbar)
        self.complex_selector.addItem("")
        self.complex_selector.setObjectName("complex_selector")

        self.horizontalLayout.addWidget(self.complex_selector)

        self.toolButton = QToolButton(self.editor_toolbar)
        self.toolButton.setObjectName("toolButton")

        self.horizontalLayout.addWidget(self.toolButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_value = QToolButton(self.editor_toolbar)
        self.button_value.setObjectName("button_value")

        self.horizontalLayout.addWidget(self.button_value)

        self.button_complexvalue = QToolButton(self.editor_toolbar)
        self.button_complexvalue.setObjectName("button_complexvalue")

        self.horizontalLayout.addWidget(self.button_complexvalue)

        self.verticalLayout.addWidget(self.editor_toolbar)

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
        self.model_viewer = SampleViewer(self.frame)
        self.model_viewer.setObjectName("model_viewer")

        self.verticalLayout_3.addWidget(self.model_viewer)

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
        self.button_layer.setText(QCoreApplication.translate("MainWindow", "Layer", None))
        self.button_material.setText(QCoreApplication.translate("MainWindow", "Material", None))
        self.button_composit.setText(QCoreApplication.translate("MainWindow", "Composit", None))
        self.button_substack.setText(QCoreApplication.translate("MainWindow", "SubStack", None))
        self.complex_selector.setItemText(0, QCoreApplication.translate("MainWindow", "Complex Item...", None))

        self.toolButton.setText(QCoreApplication.translate("MainWindow", "ModelParameters", None))
        self.button_value.setText(QCoreApplication.translate("MainWindow", "Value", None))
        self.button_complexvalue.setText(QCoreApplication.translate("MainWindow", "ComplexValue", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", "Update Model", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", "Reflectivity", None))
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("MainWindow", "SLD Profile", None))

    # retranslateUi
