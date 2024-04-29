#____________________________Importaciones___________________________________#
import sqlite3 as sql
import pandas as pd
#_________________________________Clase_____________________________________#
class GestorBd():
    def __init__(self):
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
                            'TAMAÑO' TEXT NOT NULL,
                            'LOTE' TEXT NOT NULL,
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
        

        self.con     = sql.connect("Dive.db")
        self.cursor  = self.con.cursor()

        self.CRUD("create")
        






                  
#*-*-*-*-*-*-*-*-*-*-*-*-*CRUD*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
    def getPos(self, tabla, nameTabla):

        
        self.buffer.append([
                            tabla,
                            nameTabla,
                            tabla.currentColumn(),
                            tabla.currentRow()
                          ])


        print(self.buffer)
        

        self.updateFlagChange()


    def messageboxUtil(self, messBox, sms, crud=None):
        messBox.setWindowTitle("¡Advertencia!")
        messBox.setText(sms)
        messBox.setIcon(messBox.Warning)
        messBox.setStandardButtons(messBox.Yes| messBox.No)      

        btn_Clickeado = messBox.exec_()

        if btn_Clickeado == messBox.Yes:

            try:
                self.CRUD(crud)
                #marcaba error porque no habia nada en las tablas de la BDD

            except:
                self.messageboxUtil(messBox, "Existen valores nulos")  
        else:
                del self.buffer[::]
                self.updateFlagChange()      

    def getID(self, item , nameTabla):
        df = pd.read_sql_query(f"SELECT * FROM {nameTabla}", self.con)
        return df.iloc[item , 0]
        #print(df.columns.tolist()) #obtener header de las tablas de la base de datos 

    def getHeader(self, nameTabla):

        query = f"SELECT * FROM {nameTabla} WHERE 1=0;" 
        self.cursor.execute(query)
        return [k[0] for k in self.cursor.description]

        
    def updateFlagChange(self):
        
        if len(self.buffer) <= 0:
            self.updateFlag = True

        else:
            self.updateFlag = False

    def crear(self):

        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tabla[0][0]} ({self.tabla[0][1][0]}) ")
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tabla[1][0]} ({self.tabla[1][1][0]}) ")
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tabla[2][0]} ({self.tabla[2][1][0]}) ")
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tabla[3][0]} ({self.tabla[3][1][0]}) ")
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tabla[4][0]} ({self.tabla[4][1][0]}) ")

        #insertar colunda insumos 

        
        
    def leer(self, num):

        self.cursor.execute(f"SELECT * FROM {self.tabla[num][0]}")
        return self.cursor.fetchall()

    def actualizar(self, tabla, header, new_item, ID):

        try:
            query = (f"UPDATE {tabla} SET {header} = '{new_item}' WHERE ID = {ID}")
            self.cursor.execute(query)
            self.con.commit()
            del self.buffer[::]
            self.updateFlagChange()

        except:
            
            pass

    #def insertar(self, num, *datos):
    #    self.cursor.execute(f"INSERT INTO {self.tabla[num][0]} VALUES ({(len(datos)-1)*'?,'+'?'})", datos)


    def aggFilas(self, nameTabla, num = 0):

        if nameTabla != None and num == 0:
            numFilas = nameTabla.rowCount() #Extrae el numero total de filas
            nameTabla.setRowCount(numFilas+1)


        elif nameTabla != None and num != 0:
            nameTabla.setRowCount(num)

        else:
            pass
            #QmessageBox "No se pueden agg filas en esta tabla"


    def delete(self):

        if self.updateFlag == False:
            
            for i in self.buffer[::-1]:
                indice = i[0].currentIndex().row()
                i[0].removeRow(indice)
                ID = self.getID(i[3], i[1])
                self.cursor.execute(f"DELETE FROM {i[1]} WHERE ID = {ID}")
                self.con.commit()
                self.buffer.pop(-1)


        else:
            #qmessagebox
            print("debe seleccionar un elemento")
            


    def insertar(self, nameTabla):
        df = pd.read_sql_query(f"SELECT * from {nameTabla}", self.con)
        num = len(df.index)
        self.aggFilas(nameTabla, num)
        for i in range(num):
            pass
        #self.ui.tb_ventas.setItem(0,0, QTableWidgetItem("holamundo")) # forma de insertar valores.

    def search(self):
        pass


    def warningUpdate(self,messBox):
       
        if self.updateFlag == False:
            
            self.messageboxUtil(messBox, "¿Desea guardar los cambios?", "update")
            

        else:
            pass

  
    def CRUD(self, flag, nameTabla = None ,  num=0):

        if flag == "create":
            self.crear() #Listo

        elif flag == "read":
            self.leer(num)

        elif flag == "update":   #Listo
                                    
            for i in self.buffer:  

                k        = self.getHeader(i[1])
                new_item = i[0].item(i[3], i[2])
                ID       = self.getID(i[3],i[1])
                self.actualizar(i[1], k[i[2]+1], new_item.text(), ID )

        elif flag == "aggFilas":

            self.aggFilas(nameTabla)


        elif flag == "insert":
            pass
        
        elif flag == "delete":
            self.delete() #Listo

        elif flag == "search":
            self.search()

        else:
            #aqui va un messageBox
            print (flag, " no es un metodo de crud")
        

