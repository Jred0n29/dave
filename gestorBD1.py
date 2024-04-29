#____________________________Importaciones___________________________________#
import sqlite3 as sql
import pandas as pd
from PyQt5.QtWidgets import QMessageBox , QMainWindow
from PySide6 import QtWidgets, QtCore
from propiedades import *

#_________________________________Clase_____________________________________#
class GestorBd():
    def __init__(self):
        self.NameDB = "Dive.db3" #nombre de la bas de datos.
        self.buffer = []

        self.updateFlag = True

#*-*-*-*-*-*-*-*-*-*-*-QUERY*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        
        tb_cliente    = ["tb_cliente", 
                            ["""
                            'ID' INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT UNIQUE,
                            'NOMBRE' TEXT NOT NULL, 
                            'APELLIDOS' TEXT NOT NULL,
                            'TELEFONO' INTEGER NOT NULL,
                            'BARRIO' TEXT NOT NULL,
                               'SABOR' TEXT NOT NULL,
                         'FRUTA' TEXT NOT NULL,
                            'LOTE' TEXT NOT NULL,
                            'TAMAÑO' TEXT NOT NULL,
                            'ENTREGA' TEXT NOT NULL,
                            'PAGO' TEXT NOT NULL, 
                            'VENDEDOR' TEXT NOT NULL
                            """]
                        ]


        tb_vendedores = ["tb_vendedores", 
                            ["""
                            'ID' INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT UNIQUE,
                            'NOMBRE' TEXT NOT NULL, 
                            'APELLIDOS' TEXT NOT NULL,
                            'TELEFONO' INTEGER NOT NULL,
                            'CIUDAD' TEXT NOT NULL,
                            'SECTOR' TEXT NOT NULL,
                            'VENTAS/LOTES' TEXT NOT NULL
                            """]
                        ]


        tb_ventas     = ["tb_ventas", 
                            ["""
                            'ID' INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT UNIQUE,
                            'LOTE' TEXT NOT NULL,
                            'SABOR' TEXT NOT NULL,
                            'CANTIDAD' TEXT NOT NULL   
                            """]
                        ]


        tb_contabilidad = ["tb_contabilidad", 
                            ["""
                            'ID' INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT UNIQUE,
                            'LOTE' TEXT NOT NULL,
                            'INVERSION' INTEGER NOT NULL,
                            'RECAUDADO' INTEGER NOT NULL, 
                            'GANANCIA' INTEGER NOT NULL
                             """] 
                            ]

        tb_insumos    = ["tb_insumos", 
                            ["""
                            'ID' TEXT NOT NULL UNIQUE,
                            'VARIANTES' TEXT  NULL,
                            'LECHE' TEXT, 
                            'AZUCAR' TEXT,
                            'ENVASE' TEXT,
                            'SABORIZANTE' TEXT,
                            'COLORANTE' TEXT,
                            'FRUTA' TEXT,
                            'CULTIVO' TEXT,
                            'CONSERVANTE' TEXT
                            """]
                        ]

        self.row_Insumos   = [            
                              ("CANTIDAD"),
                              ("KUMIS"),
                              ("NATURAL"),
                              ("FRESA"),
                              ("MORA"),
                              ("UVA"),
                              ("MELOCOTON"),
                              ("COCO")
                             ]

        self.tabla  =  [

                        tb_cliente,
                        tb_vendedores,
                        tb_ventas,
                        tb_contabilidad,
                        tb_insumos

                       ]
        
#::::::::::::::::::::::::::::::::::Conxion:::::::::::::::::::::::::::::::::::::::::::::#
        self.con = sql.connect(self.NameDB)
        self.cur = self.con.cursor()
        self.dataFrame = []

        for i in range(len(self.tabla)):
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.tabla[i][0]} ({self.tabla[i][1][0]})")
            self.dataFrame.append(pd.read_sql(f"SELECT * FROM {self.tabla[i][0]}", self.con))

        

    def rowCount(self, num):       
        return self.dataFrame[num].shape[0]

    def columnCount(self, num):
        return self.dataFrame[num].shape[1]

    def getDataFrame(self):
        return self.dataFrame


    def insertDataTable(self, num, table):

        row = 0

        for indice_fila, fila in  self.dataFrame[num].iterrows():

            dataRow = list(fila)    
            column = 0
            #table.insertRow(row) #no se para que
            for data in dataRow:
                data = str(data) 
                data = QtWidgets.QTableWidgetItem(data)
                table.setItem(row, column, data)
                column += 1
            row += 1

    def aggFilas_Columnas(self, table , variante = "" ):

        if variante == "AggFila":

            table[0].insertRow(table[0].rowCount())

            #|-|-|-|-|-| INSERTAR EN SQLITE3 CON UN VALOR POR DEFEECTO |-|-|-|-|-|-|-|-|

            NameTabla = self.tabla[table[1]][0]
            df = pd.read_sql_query(f"SELECT * from {NameTabla}", self.con)
            LenValues = len(df.columns.tolist())-2
            defaultValues = "0,"*LenValues + "0"
            self.cur.execute(f"INSERT INTO {NameTabla} VALUES (NULL,{defaultValues})")
            self.con.commit()

        elif variante == "AggColumna":

            #|-|-|  INSTACIAMOS LA CLASE VENTANA PARA LLAMAR A LA VENTANA EMERGENTE Y GUARDAR LA COLUMNA EN SQLITE3 
            self.ventana = Ventana2()
            self.ventana.botones(table)

    def deleteFilas_Columnas(self, table , variante = ""):

        if variante == "EliminarFila":

            #-|-|-|-|-|-|-| ELIMINAR DE SQLITE3 Y LA TABLA |-|-|-|-|-|-|-|-|-|

            ID = table[0].item(table[0].currentRow() , 0).text()
            self.cur.execute(f"DELETE FROM {self.tabla[table[1]][0]} WHERE ID = {ID}")
            self.con.commit()
            return table[0].removeRow(table[0].currentRow())

        elif variante == "EliminarColumna":

            #FALTA TERMINAR ESTA FUNCION
            return table[0].removeColumn(table[0].currentColumn())

    def saveBBDColumn(self, titulo, TypeDato,table):

        #|-|-| GUARDAR COLUMNA EN SQLITE ESTE METODO LO LLAMA LA VENTANA EMERGENTE POR INSTANCIA |-|-|-|-|
        try:
            self.cur.execute(f""" ALTER TABLE {self.tabla[table[1]][0]} ADD {titulo} {TypeDato} DEFAULT "" """)
            self.con.commit()

            headers = list(self.dataFrame[table[1]].keys())
            headers.append(titulo)
            table[0].insertColumn(table[0].columnCount())
            table[0].setHorizontalHeaderLabels(headers)

        except:
            self.messageBoxUtil("Information", "Columna existente", "Ya existe una columna con ese nombre vuelva a intentarlo.")


    def actualizar(self):
        pass


    def buscar(self):
        pass

    def estadisticas(self):
        pass


#______________________________________________messageBox______________________________________________________#

    def messageBoxUtil(self, icono = "NoIco", titulo = "" , sms = ""):
           
        objMessage = QMessageBox()
        if icono == "Question":
            titulo      = titulo
            typeMessage = objMessage.Question
            objMessage.setStandardButtons(objMessage.Yes| objMessage.No) 

        elif icono == "Information":
            titulo      = titulo
            typeMessage = objMessage.Information
            objMessage.setStandardButtons(objMessage.Ok) 

        elif icono == "Warning":
            titulo      = titulo
            typeMessage = objMessage.Warning
            objMessage.setStandardButtons(objMessage.Close) 

        elif icono == "Critical":
            titulo      = titulo
            typeMessage = objMessage.Critical
            objMessage.setStandardButtons(objMessage.Ignore | objMessage.Abort) 

        #cuerpo 
        objMessage.setWindowTitle(titulo)
        objMessage.setText(sms)
        objMessage.setIcon(typeMessage)
             

        btn_Clickeado = objMessage.exec_()
        btn_message   = [objMessage.Ok,
                        objMessage.Ignore,
                        objMessage.No,
                        objMessage.Close,
                        objMessage.Abort
                        ]
        

        if   btn_Clickeado == objMessage.Yes:
            pass
        elif btn_Clickeado in btn_message:
            pass


class Ventana2(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow2()
        self.ventana = QtWidgets.QMainWindow()
        self.ui.setupUi2(self.ventana)
        self.ventana.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ventana.show()

    def botones(self, table):

        self.ui.btn_cerrar.clicked.connect(lambda: self.slotCloseAcept("cerrar"))
        self.ui.btn_aceptar.clicked.connect(lambda: self.slotCloseAcept("aceptar", table))

    def slotCloseAcept(self,variante = "", table = None):

        self.GestorBd = GestorBd() #INSTANCIAMOS LA CLASE PARA UTILIZAR EL QMESSABOX Y EL METODO saveBBDColumn

        if variante == "aceptar":
            self.titulo   = str(self.ui.Entry_titulo.text())
            self.TypeDato = self.ui.Combox_dato.currentText()

            if self.titulo == "":
                self.GestorBd.messageBoxUtil("Warning","Titulo sin rellenar", "La columna debe tener un titulo")
            
            else:
                self.GestorBd.saveBBDColumn(self.titulo.upper(), self.TypeDato, table )
                self.ventana.close()

        elif variante == "cerrar":
            self.ventana.close()      








