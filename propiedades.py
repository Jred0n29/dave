# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'propiedadesxRifZv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow2(object):
    def setupUi2(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(438, 319)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 30, 411, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(50, -1, 0, -1)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setStyleSheet(u"font: 75 10pt \"Segoe Print\";")

        self.horizontalLayout_2.addWidget(self.label)

        self.Entry_titulo = QLineEdit(self.verticalLayoutWidget)
        self.Entry_titulo.setObjectName(u"Entry_titulo")
        self.Entry_titulo.setMaximumSize(QSize(280, 16777215))

        self.horizontalLayout_2.addWidget(self.Entry_titulo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(120, 16777215))
        self.label_2.setStyleSheet(u"font: 75 10pt \"Segoe Print\";")

        self.horizontalLayout.addWidget(self.label_2)

        self.Combox_dato = QComboBox(self.verticalLayoutWidget)
        self.Combox_dato.addItem("")
        self.Combox_dato.addItem("")
        self.Combox_dato.addItem("")
        self.Combox_dato.addItem("")
        self.Combox_dato.setObjectName(u"Combox_dato")

        self.horizontalLayout.addWidget(self.Combox_dato)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn_aceptar = QPushButton(self.centralwidget)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setGeometry(QRect(110, 240, 141, 31))
        self.btn_aceptar.setStyleSheet(u"font: 75 10pt \"Segoe Print\";")
        self.btn_cerrar = QPushButton(self.centralwidget)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setGeometry(QRect(270, 240, 141, 31))
        self.btn_cerrar.setStyleSheet(u"font: 75 10pt \"Segoe Print\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Propiedades", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Titulo: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tipo de dato:", None))
        self.Combox_dato.setItemText(0, QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.Combox_dato.setItemText(1, QCoreApplication.translate("MainWindow", u"INTEGER", None))
        self.Combox_dato.setItemText(2, QCoreApplication.translate("MainWindow", u"BLOB", None))
        self.Combox_dato.setItemText(3, QCoreApplication.translate("MainWindow", u"REAL", None))

        self.btn_aceptar.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.btn_cerrar.setText(QCoreApplication.translate("MainWindow", u"Cerrar", None))
    # retranslateUi

