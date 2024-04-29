#_-_-_-_-_-_-_-_-_-_-_-_-_-_-IMPORTACIONES_-_-_-_-_-_-_-_-_-_-_-_-_-_-#

import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import *
from gestorBD1 import *
from ui_Dive1 import Ui_MainWindow


class MyApp(QMainWindow,GestorBd):
    def __init__(self):
        QMainWindow.__init__(self)
        GestorBd.__init__(self)

        self.estado = 0
        self.Tabla = []
        self.ui     = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mainLayout = QtWidgets.QGridLayout()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.btn_MAXIMIZAR.clicked.connect(lambda: self.maximizar())

        #crear tablas
        self.tb_clientes =      QTableWidget(self.ui.Frame_tb_clientes)
        self.tb_vendedores =    QTableWidget(self.ui.Frame_tb_vendedores)
        self.tb_ventas =        QTableWidget(self.ui.Frame_tb_ventas)
        self.tb_contabilidad =  QTableWidget(self.ui.Frame_tb_contabilidad)
        self.tb_insumos =       QTableWidget(self.ui.Frame_tb_insumos)

        self.listaTable = [
                            self.tb_clientes,
                            self.tb_vendedores,
                            self.tb_ventas,
                            self.tb_contabilidad,
                            self.tb_insumos
                          ]

    
        for i in range(len(self.listaTable)):
            df = self.getDataFrame()
            headers = list(df[i].keys())
            self.listaTable[i].setColumnCount(self.columnCount(i))
            self.listaTable[i].setRowCount(self.rowCount(i))


            self.listaTable[i].setHorizontalHeaderLabels(headers)
            self.listaTable[i].setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.listaTable[i].resizeColumnsToContents()
            self.insertDataTable(i, self.listaTable[i])
            
            for j in range(len(headers)):
                ancho = len(headers[j])*12+20
                self.listaTable[i].setColumnWidth(j, ancho)

        #Celda unica
        #self.ui.tb_clientes.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        #SideBar
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_Dive)
        self.ui.btn_dive.clicked.connect(lambda: self.dive())
        self.ui.btn_clientes.clicked.connect(lambda: self.clientes())
        self.ui.btn_vendedores.clicked.connect(lambda: self.vendedores())
        self.ui.btn_ventas.clicked.connect(lambda: self.ventas())
        self.ui.btn_contabilidad.clicked.connect(lambda: self.contabilidad())
        self.ui.btn_estadisticas.clicked.connect(lambda: self.estadisticas())
        self.ui.btn_insumos.clicked.connect(lambda: self.insumos())

        self.ui.btn_agregarFila.clicked.connect(lambda: self.aggFilas_Columnas(self.Tabla, "AggFila" ))
        self.ui.btn_agregarColumna.clicked.connect(lambda : self.aggFilas_Columnas(self.Tabla , "AggColumna"))
        self.ui.btn_eliminarFila.clicked.connect(lambda: self.deleteFilas_Columnas(self.Tabla , "EliminarFila"))
        self.ui.btn_eliminarColumna.clicked.connect(lambda: self.deleteFilas_Columnas(self.Tabla , "EliminarColumna"))
        

#*-*-*-*--*-*-*-*-*-*-*-*-EVENTOS MOVER, MAXIMIZAR, RESTAURAR-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*
    def maximizar(self):

        if self.estado == 0:
            self.estado = 1
            self.ui.btn_MAXIMIZAR.setIcon(QtGui.QIcon(u":/top/Imagenes/Restaurar.png"))
            self.showMaximized()

        else:
            self.estado = 0         
            self.ui.btn_MAXIMIZAR.setIcon(QtGui.QIcon(u":/top/Imagenes/Maximizar.png"))
            self.showNormal()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            try:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
            except:
                pass

#°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°Acción botones°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°-°
    def dive(self):
        self.Tabla = []
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_Dive)

    def clientes(self):
        self.Tabla = [self.tb_clientes, 0]
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_clientes)
        #self.ui.tb_clientes.itemSelectionChanged.connect(lambda : self.getPos(self.ui.tb_clientes, "tb_clientes"))

    def vendedores(self):
        self.Tabla = [self.tb_vendedores, 1]
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_vendedores)


    def ventas(self):
        self.Tabla = [self.tb_ventas, 2] 
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_ventas)

    def contabilidad(self):
        self.Tabla = [self.tb_contabilidad, 3]
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_contabilidad)

    def estadisticas(self):
        self.Tabla = []
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_estadisticas)

    def insumos(self):
        self.Tabla = [self.tb_insumos, 4]
        self.ui.stackedWidget.setCurrentWidget(self.ui.pg_insumos)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



