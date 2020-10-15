# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 07:48:30 2019

@author: Ing. Industrial
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys
from generar_Nube import generar_Nube


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi("WordcloudGUI.ui",self)
        self.ui.pushButton_cargar.clicked.connect(self.cargar)
        self.ui.pushButton_generar.clicked.connect(self.generar)
        self.ui.pushButton_cerrar.clicked.connect(self.cerrar)
        
    def cargar(self):
        info_archivo=QFileDialog.getOpenFileName(self)
        self.ui.lineEdit_ruta.setText(info_archivo[0])
        archivo=open(info_archivo[0],"r")
        texto=archivo.read()
        self.ui.textEdit_doc.setText(texto)
        
    def generar(self):
        archivo=open(self.ui.lineEdit_ruta.text(),"r")
        texto=archivo.read()
        self.ui.textEdit_doc.setText(generar_Nube(texto))
        
    def cerrar(self):
        self.close()
               
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Ventana()
    ventana.show()
    sys.exit(app.exec_())
    
        
        