# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dive1UthomL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import iconos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1220, 749)
        MainWindow.setMinimumSize(QSize(40, 60))
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 70))
        self.frame_top.setStyleSheet(u"QFrame\n"
"{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.573, x2:0.379, y2:0.567, stop:0.144279 rgba(160, 37, 78, 246), stop:0.557214 rgba(0, 0, 0, 255));\n"
"	border: none;\n"
"}")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(10, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.frame = QFrame(self.frame_top)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(720, 0))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.573, x2:0.598, y2:0.578364, stop:0.144279 rgba(160, 37, 78, 246), stop:0.646766 rgba(0, 0, 0, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.frame)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMaximumSize(QSize(150, 90))
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet(u"background-color: none;\n"
"font: 18pt \"Segoe Print\";\n"
"color:rgb(255, 255, 255);\n"
"border: none;\n"
"")
        icon = QIcon()
        icon.addFile(u":/top/Imagenes/Menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.btn_menu)

        self.horizontalSpacer_4 = QSpacerItem(550, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_2.addWidget(self.frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_mmc = QFrame(self.frame_top)
        self.frame_mmc.setObjectName(u"frame_mmc")
        self.frame_mmc.setMaximumSize(QSize(300, 90))
        self.frame_mmc.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.frame_mmc.setFrameShape(QFrame.StyledPanel)
        self.frame_mmc.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_mmc)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 8, 0)
        self.btn_MINIMIZAR = QPushButton(self.frame_mmc)
        self.btn_MINIMIZAR.setObjectName(u"btn_MINIMIZAR")
        self.btn_MINIMIZAR.setMaximumSize(QSize(30, 30))
        self.btn_MINIMIZAR.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/top/Imagenes/Minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_MINIMIZAR.setIcon(icon1)
        self.btn_MINIMIZAR.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_MINIMIZAR)

        self.btn_MAXIMIZAR = QPushButton(self.frame_mmc)
        self.btn_MAXIMIZAR.setObjectName(u"btn_MAXIMIZAR")
        self.btn_MAXIMIZAR.setMaximumSize(QSize(30, 30))
        self.btn_MAXIMIZAR.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/top/Imagenes/Maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/top/Imagenes/Restaurar.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_MAXIMIZAR.setIcon(icon2)
        self.btn_MAXIMIZAR.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_MAXIMIZAR)

        self.btn_CERRAR = QPushButton(self.frame_mmc)
        self.btn_CERRAR.setObjectName(u"btn_CERRAR")
        self.btn_CERRAR.setMaximumSize(QSize(30, 30))
        self.btn_CERRAR.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/top/Imagenes/Cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_CERRAR.setIcon(icon3)
        self.btn_CERRAR.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_CERRAR)


        self.horizontalLayout_2.addWidget(self.frame_mmc)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.centralwidget)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setStyleSheet(u"background-color: rgb(31, 30, 46);\n"
"border: none;")
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_center)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_sideBar = QFrame(self.frame_center)
        self.frame_sideBar.setObjectName(u"frame_sideBar")
        self.frame_sideBar.setMinimumSize(QSize(0, 0))
        self.frame_sideBar.setMaximumSize(QSize(310, 16777215))
        self.frame_sideBar.setStyleSheet(u"QFrame\n"
"{\n"
"	border: none;\n"
"	background-color: qlineargradient(spread:pad, x1:0.269, y1:0.0454545, x2:1, y2:0.011, stop:0.0149254 rgba(160, 37, 78, 255), stop:0.985075 rgba(0, 0, 0, 250));\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_sideBar.setFrameShape(QFrame.StyledPanel)
        self.frame_sideBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_sideBar)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_inicio = QFrame(self.frame_sideBar)
        self.frame_inicio.setObjectName(u"frame_inicio")
        self.frame_inicio.setMaximumSize(QSize(320, 100))
        self.frame_inicio.setStyleSheet(u"")
        self.frame_inicio.setFrameShape(QFrame.StyledPanel)
        self.frame_inicio.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_inicio)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 10, 0, 0)
        self.btn_dive = QPushButton(self.frame_inicio)
        self.btn_dive.setObjectName(u"btn_dive")
        self.btn_dive.setMinimumSize(QSize(0, 50))
        self.btn_dive.setMaximumSize(QSize(320, 180))
        self.btn_dive.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dive.setStyleSheet(u"QPushButton{\n"
"font: 75 20pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgba(255,255,255, 0);\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-radius: 8px;\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/center/Imagenes/images.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dive.setIcon(icon4)
        self.btn_dive.setIconSize(QSize(60, 60))

        self.verticalLayout_2.addWidget(self.btn_dive)

        self.label = QLabel(self.frame_inicio)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(280, 2))
        self.label.setStyleSheet(u"border-bottom:2px solid#ffffff;")

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_8.addWidget(self.frame_inicio)

        self.frame_personas = QFrame(self.frame_sideBar)
        self.frame_personas.setObjectName(u"frame_personas")
        self.frame_personas.setMaximumSize(QSize(320, 16777215))
        self.frame_personas.setStyleSheet(u"")
        self.frame_personas.setFrameShape(QFrame.StyledPanel)
        self.frame_personas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_personas)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 40, 0, 0)
        self.btn_clientes = QPushButton(self.frame_personas)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMinimumSize(QSize(0, 50))
        self.btn_clientes.setMaximumSize(QSize(320, 180))
        self.btn_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clientes.setStyleSheet(u"QPushButton{\n"
"font: 75 17pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgba(255,255,255, 0);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:clicked\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-radius: 8px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/center/Imagenes/Clientes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clientes.setIcon(icon5)
        self.btn_clientes.setIconSize(QSize(60, 60))

        self.verticalLayout_3.addWidget(self.btn_clientes)

        self.btn_vendedores = QPushButton(self.frame_personas)
        self.btn_vendedores.setObjectName(u"btn_vendedores")
        self.btn_vendedores.setMinimumSize(QSize(0, 50))
        self.btn_vendedores.setMaximumSize(QSize(320, 180))
        self.btn_vendedores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_vendedores.setStyleSheet(u"QPushButton{\n"
"font: 75 17pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgba(255,255,255, 0);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-radius: 8px;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/center/Imagenes/Vendedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_vendedores.setIcon(icon6)
        self.btn_vendedores.setIconSize(QSize(60, 60))

        self.verticalLayout_3.addWidget(self.btn_vendedores)

        self.label_2 = QLabel(self.frame_personas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(280, 2))
        self.label_2.setStyleSheet(u"border-bottom:2px solid#ffffff;\n"
"backgraound-color: none;")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_8.addWidget(self.frame_personas)

        self.frame_dinero = QFrame(self.frame_sideBar)
        self.frame_dinero.setObjectName(u"frame_dinero")
        self.frame_dinero.setMinimumSize(QSize(0, 50))
        self.frame_dinero.setMaximumSize(QSize(320, 16777215))
        self.frame_dinero.setStyleSheet(u"")
        self.frame_dinero.setFrameShape(QFrame.StyledPanel)
        self.frame_dinero.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_dinero)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 40, 0, 0)
        self.btn_ventas = QPushButton(self.frame_dinero)
        self.btn_ventas.setObjectName(u"btn_ventas")
        self.btn_ventas.setMinimumSize(QSize(0, 50))
        self.btn_ventas.setMaximumSize(QSize(320, 180))
        self.btn_ventas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ventas.setStyleSheet(u"QPushButton{\n"
"font: 75 17pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgba(255,255,255, 0);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	border-radius: 8px;\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/center/Imagenes/Ventas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ventas.setIcon(icon7)
        self.btn_ventas.setIconSize(QSize(70, 70))

        self.verticalLayout_6.addWidget(self.btn_ventas)

        self.btn_contabilidad = QPushButton(self.frame_dinero)
        self.btn_contabilidad.setObjectName(u"btn_contabilidad")
        self.btn_contabilidad.setMinimumSize(QSize(0, 50))
        self.btn_contabilidad.setMaximumSize(QSize(320, 180))
        self.btn_contabilidad.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contabilidad.setStyleSheet(u"QPushButton{\n"
"font: 75 17pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgba(255,255,255, 0);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/center/Imagenes/Contabilidad.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_contabilidad.setIcon(icon8)
        self.btn_contabilidad.setIconSize(QSize(60, 60))

        self.verticalLayout_6.addWidget(self.btn_contabilidad)

        self.btn_estadisticas = QPushButton(self.frame_dinero)
        self.btn_estadisticas.setObjectName(u"btn_estadisticas")
        self.btn_estadisticas.setMinimumSize(QSize(0, 50))
        self.btn_estadisticas.setMaximumSize(QSize(320, 180))
        self.btn_estadisticas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_estadisticas.setStyleSheet(u"QPushButton{\n"
"font: 75 17pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgba(255,255,255, 0);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/center/Imagenes/Estadistica.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_estadisticas.setIcon(icon9)
        self.btn_estadisticas.setIconSize(QSize(60, 60))

        self.verticalLayout_6.addWidget(self.btn_estadisticas)

        self.label_5 = QLabel(self.frame_dinero)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(280, 2))
        self.label_5.setStyleSheet(u"border-bottom:2px solid#ffffff;\n"
"background-color: none;\n"
"")

        self.verticalLayout_6.addWidget(self.label_5)


        self.verticalLayout_8.addWidget(self.frame_dinero)

        self.frame_insumos = QFrame(self.frame_sideBar)
        self.frame_insumos.setObjectName(u"frame_insumos")
        self.frame_insumos.setMaximumSize(QSize(320, 16777215))
        self.frame_insumos.setStyleSheet(u"")
        self.frame_insumos.setFrameShape(QFrame.StyledPanel)
        self.frame_insumos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_insumos)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 0, 20)
        self.btn_insumos = QPushButton(self.frame_insumos)
        self.btn_insumos.setObjectName(u"btn_insumos")
        self.btn_insumos.setMinimumSize(QSize(0, 50))
        self.btn_insumos.setMaximumSize(QSize(320, 70))
        self.btn_insumos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_insumos.setStyleSheet(u"QPushButton{\n"
"font: 75 17pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgba(255,255,255, 0);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/center/Imagenes/Insumos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_insumos.setIcon(icon10)
        self.btn_insumos.setIconSize(QSize(60, 60))

        self.verticalLayout_7.addWidget(self.btn_insumos)


        self.verticalLayout_8.addWidget(self.frame_insumos)


        self.horizontalLayout.addWidget(self.frame_sideBar)

        self.frame_body = QFrame(self.frame_center)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setMinimumSize(QSize(0, 50))
        self.frame_body.setMaximumSize(QSize(16777215, 16777215))
        self.frame_body.setStyleSheet(u"background-color: #000000;")
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_body)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_Header = QFrame(self.frame_body)
        self.frame_Header.setObjectName(u"frame_Header")
        self.frame_Header.setMinimumSize(QSize(0, 80))
        self.frame_Header.setStyleSheet(u"")
        self.frame_Header.setFrameShape(QFrame.StyledPanel)
        self.frame_Header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_Header)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_buscar = QFrame(self.frame_Header)
        self.frame_buscar.setObjectName(u"frame_buscar")
        self.frame_buscar.setMaximumSize(QSize(16777215, 60))
        self.frame_buscar.setStyleSheet(u"background-color: none;")
        self.frame_buscar.setFrameShape(QFrame.StyledPanel)
        self.frame_buscar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_buscar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_before = QPushButton(self.frame_buscar)
        self.btn_before.setObjectName(u"btn_before")
        self.btn_before.setMinimumSize(QSize(40, 40))
        self.btn_before.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_before.setStyleSheet(u"QPushButton{\n"
"font: 75 10pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: none;\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-radius: 8px;\n"
"\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/center/Imagenes/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_before.setIcon(icon11)

        self.horizontalLayout_4.addWidget(self.btn_before)

        self.btn_next = QPushButton(self.frame_buscar)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumSize(QSize(40, 40))
        self.btn_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_next.setStyleSheet(u"QPushButton{\n"
"font: 75 10pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color:none;\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-radius: 8px;\n"
"\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/center/Imagenes/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.btn_next)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.frame_sombraBuscar = QFrame(self.frame_buscar)
        self.frame_sombraBuscar.setObjectName(u"frame_sombraBuscar")
        self.frame_sombraBuscar.setMinimumSize(QSize(380, 40))
        self.frame_sombraBuscar.setMaximumSize(QSize(380, 60))
        self.frame_sombraBuscar.setStyleSheet(u"\n"
"QFrame\n"
"{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:hover\n"
"{\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"\n"
"QFrame:cursor\n"
"{\n"
"	background-color: rgb(30,30,30);\n"
"}")
        self.frame_sombraBuscar.setFrameShape(QFrame.StyledPanel)
        self.frame_sombraBuscar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_sombraBuscar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.led_buscar = QLineEdit(self.frame_sombraBuscar)
        self.led_buscar.setObjectName(u"led_buscar")
        self.led_buscar.setMinimumSize(QSize(300, 25))
        self.led_buscar.setMaximumSize(QSize(300, 25))
        self.led_buscar.setStyleSheet(u"QLineEdit{\n"
"	font: 10pt \"Segoe Print\";\n"
"	background-color:  rgb(10,10, 10);\n"
"	color: #ffffff;\n"
"	border:none;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"	background-color: rgb(43, 43, 43);\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"\n"
"{\n"
"	\n"
"	background-color: rgb(160, 37, 78, 0.5);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.led_buscar)

        self.btn_buscar = QPushButton(self.frame_sombraBuscar)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setMaximumSize(QSize(40, 38))
        self.btn_buscar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_buscar.setStyleSheet(u"QPushButton\n"
"{\n"
"    border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   \n"
"	\n"
"	background-color: rgb(31, 30, 46);\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/center/Imagenes/unnamed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar.setIcon(icon13)
        self.btn_buscar.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.btn_buscar)


        self.horizontalLayout_4.addWidget(self.frame_sombraBuscar)


        self.verticalLayout_13.addWidget(self.frame_buscar)

        self.frame_CRUDS = QFrame(self.frame_Header)
        self.frame_CRUDS.setObjectName(u"frame_CRUDS")
        self.frame_CRUDS.setMinimumSize(QSize(80, 40))
        self.frame_CRUDS.setMaximumSize(QSize(16777215, 60))
        self.frame_CRUDS.setStyleSheet(u"background-color: rgb(160, 37, 78);")
        self.frame_CRUDS.setFrameShape(QFrame.StyledPanel)
        self.frame_CRUDS.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_CRUDS)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 4, 0)
        self.btn_guardar = QPushButton(self.frame_CRUDS)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setMinimumSize(QSize(140, 40))
        self.btn_guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_guardar.setStyleSheet(u"QPushButton{\n"
"font: 75 10pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgb(160, 37, 78);\n"
"border-rigth: 1px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-bottom: 2px solid rgb(183, 193, 255);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_guardar)

        self.btn_actualizar = QPushButton(self.frame_CRUDS)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setMinimumSize(QSize(140, 40))
        self.btn_actualizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_actualizar.setStyleSheet(u"QPushButton{\n"
"font: 75 10pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgb(160, 37, 78);\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-bottom: 2px solid rgb(183, 193, 255);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_actualizar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.btn_agregarFila = QPushButton(self.frame_CRUDS)
        self.btn_agregarFila.setObjectName(u"btn_agregarFila")
        self.btn_agregarFila.setMinimumSize(QSize(140, 40))
        self.btn_agregarFila.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregarFila.setStyleSheet(u"QPushButton{\n"
"font: 75 10pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgb(160, 37, 78);\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-bottom: 2px solid rgb(183, 193, 255);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_agregarFila)

        self.btn_agregarColumna = QPushButton(self.frame_CRUDS)
        self.btn_agregarColumna.setObjectName(u"btn_agregarColumna")
        self.btn_agregarColumna.setMinimumSize(QSize(140, 40))
        self.btn_agregarColumna.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregarColumna.setStyleSheet(u"QPushButton{\n"
"font: 75 10pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgb(160, 37, 78);\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-bottom: 2px solid rgb(183, 193, 255);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_agregarColumna)

        self.btn_eliminarFila = QPushButton(self.frame_CRUDS)
        self.btn_eliminarFila.setObjectName(u"btn_eliminarFila")
        self.btn_eliminarFila.setMinimumSize(QSize(140, 40))
        self.btn_eliminarFila.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminarFila.setStyleSheet(u"QPushButton{\n"
"font: 75 10pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgb(160, 37, 78);\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-bottom: 2px solid rgb(183, 193, 255);\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_eliminarFila)

        self.btn_eliminarColumna = QPushButton(self.frame_CRUDS)
        self.btn_eliminarColumna.setObjectName(u"btn_eliminarColumna")
        self.btn_eliminarColumna.setMinimumSize(QSize(140, 40))
        self.btn_eliminarColumna.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminarColumna.setStyleSheet(u"QPushButton{\n"
"font: 75 10pt \"Segoe Print\";\n"
"color: rgba(255,255,255, 1);\n"
"background-color: rgb(160, 37, 78);\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(40, 42, 63, 0.3);\n"
"	border-bottom: 2px solid rgb(183, 193, 255);\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_eliminarColumna)


        self.verticalLayout_13.addWidget(self.frame_CRUDS)


        self.verticalLayout_4.addWidget(self.frame_Header)

        self.stackedWidget = QStackedWidget(self.frame_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.pg_Dive = QWidget()
        self.pg_Dive.setObjectName(u"pg_Dive")
        self.pg_Dive.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.pg_Dive)
        self.pg_clientes = QWidget()
        self.pg_clientes.setObjectName(u"pg_clientes")
        self.pg_clientes.setMinimumSize(QSize(400, 100))
        self.pg_clientes.setStyleSheet(u"background-color: rgb(50, 48, 72);\n"
"border:none;")
        self.verticalLayout_5 = QVBoxLayout(self.pg_clientes)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Frame_tb_clientes = QFrame(self.pg_clientes)
        self.Frame_tb_clientes.setObjectName(u"Frame_tb_clientes")
        self.Frame_tb_clientes.setMinimumSize(QSize(800, 100))
        self.Frame_tb_clientes.setFrameShape(QFrame.StyledPanel)
        self.Frame_tb_clientes.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.Frame_tb_clientes)

        self.stackedWidget.addWidget(self.pg_clientes)
        self.pg_vendedores = QWidget()
        self.pg_vendedores.setObjectName(u"pg_vendedores")
        self.pg_vendedores.setStyleSheet(u"background-color: rgb(31, 30, 46);\n"
"border:none;")
        self.verticalLayout_9 = QVBoxLayout(self.pg_vendedores)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Frame_tb_vendedores = QFrame(self.pg_vendedores)
        self.Frame_tb_vendedores.setObjectName(u"Frame_tb_vendedores")
        self.Frame_tb_vendedores.setFrameShape(QFrame.StyledPanel)
        self.Frame_tb_vendedores.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.Frame_tb_vendedores)

        self.stackedWidget.addWidget(self.pg_vendedores)
        self.pg_ventas = QWidget()
        self.pg_ventas.setObjectName(u"pg_ventas")
        self.pg_ventas.setStyleSheet(u"background-color: rgb(31, 30, 46);\n"
"border:none;")
        self.verticalLayout_10 = QVBoxLayout(self.pg_ventas)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Frame_tb_ventas = QFrame(self.pg_ventas)
        self.Frame_tb_ventas.setObjectName(u"Frame_tb_ventas")
        self.Frame_tb_ventas.setFrameShape(QFrame.StyledPanel)
        self.Frame_tb_ventas.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.Frame_tb_ventas)

        self.stackedWidget.addWidget(self.pg_ventas)
        self.pg_contabilidad = QWidget()
        self.pg_contabilidad.setObjectName(u"pg_contabilidad")
        self.pg_contabilidad.setStyleSheet(u"background-color: rgb(31, 30, 46);\n"
"border:none;")
        self.verticalLayout_11 = QVBoxLayout(self.pg_contabilidad)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Frame_tb_contabilidad = QFrame(self.pg_contabilidad)
        self.Frame_tb_contabilidad.setObjectName(u"Frame_tb_contabilidad")
        self.Frame_tb_contabilidad.setFrameShape(QFrame.StyledPanel)
        self.Frame_tb_contabilidad.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.Frame_tb_contabilidad)

        self.stackedWidget.addWidget(self.pg_contabilidad)
        self.pg_estadisticas = QWidget()
        self.pg_estadisticas.setObjectName(u"pg_estadisticas")
        self.pg_estadisticas.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.pg_estadisticas)
        self.pg_insumos = QWidget()
        self.pg_insumos.setObjectName(u"pg_insumos")
        self.pg_insumos.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border:none;")
        self.verticalLayout_12 = QVBoxLayout(self.pg_insumos)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Frame_tb_insumos = QFrame(self.pg_insumos)
        self.Frame_tb_insumos.setObjectName(u"Frame_tb_insumos")
        self.Frame_tb_insumos.setFrameShape(QFrame.StyledPanel)
        self.Frame_tb_insumos.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.Frame_tb_insumos)

        self.stackedWidget.addWidget(self.pg_insumos)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_body)


        self.verticalLayout.addWidget(self.frame_center)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMaximumSize(QSize(16777215, 50))
        self.frame_bottom.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.0959545, x2:0.279, y2:0.118136, stop:0.144279 rgba(160, 37, 78, 246), stop:0.880597 rgba(0, 0, 0, 255));")
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_CERRAR.clicked.connect(MainWindow.close)
        self.btn_MINIMIZAR.clicked.connect(MainWindow.showMinimized)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u" Men\u00fa", None))
        self.btn_MINIMIZAR.setText("")
        self.btn_MAXIMIZAR.setText("")
        self.btn_CERRAR.setText("")
        self.btn_dive.setText(QCoreApplication.translate("MainWindow", u"  Dive          ", None))
        self.label.setText("")
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"   Clientes        ", None))
        self.btn_vendedores.setText(QCoreApplication.translate("MainWindow", u"   Vendedores   ", None))
        self.label_2.setText("")
        self.btn_ventas.setText(QCoreApplication.translate("MainWindow", u"   Ventas         ", None))
        self.btn_contabilidad.setText(QCoreApplication.translate("MainWindow", u"   Contabilidad  ", None))
        self.btn_estadisticas.setText(QCoreApplication.translate("MainWindow", u"  Estadisticas   ", None))
        self.label_5.setText("")
        self.btn_insumos.setText(QCoreApplication.translate("MainWindow", u"   Insumos       ", None))
        self.btn_before.setText("")
        self.btn_next.setText("")
        self.led_buscar.setPlaceholderText("")
        self.btn_buscar.setText("")
        self.btn_guardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btn_actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btn_agregarFila.setText(QCoreApplication.translate("MainWindow", u"Agregar fila", None))
        self.btn_agregarColumna.setText(QCoreApplication.translate("MainWindow", u"Agregar columna", None))
        self.btn_eliminarFila.setText(QCoreApplication.translate("MainWindow", u"Eliminar fila", None))
        self.btn_eliminarColumna.setText(QCoreApplication.translate("MainWindow", u"Eliminar columna", None))
    # retranslateUi

