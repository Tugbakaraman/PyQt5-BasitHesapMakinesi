import math
import sys
from PyQt5.QtWidgets import*
from HesapMakinesiUi import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tasarim=Ui_MainWindow()
        self.tasarim.setupUi(self)

        self.islem_text=''
        self.sonuc=0
        
        self.tasarim.pushButton_0.clicked.connect(self.yazdir)
        self.tasarim.pushButton_1.clicked.connect(self.yazdir)
        self.tasarim.pushButton_2.clicked.connect(self.yazdir)
        self.tasarim.pushButton_3.clicked.connect(self.yazdir)
        self.tasarim.pushButton_4.clicked.connect(self.yazdir)
        self.tasarim.pushButton_5.clicked.connect(self.yazdir)
        self.tasarim.pushButton_6.clicked.connect(self.yazdir)
        self.tasarim.pushButton_7.clicked.connect(self.yazdir)
        self.tasarim.pushButton_8.clicked.connect(self.yazdir)
        self.tasarim.pushButton_9.clicked.connect(self.yazdir)
        self.tasarim.pushButton_Toplma.clicked.connect(self.yazdir)
        self.tasarim.pushButton_Cikartma.clicked.connect(self.yazdir)
        self.tasarim.pushButton_Carpma.clicked.connect(self.yazdir)
        self.tasarim.pushButton_Bolme.clicked.connect(self.yazdir)
        self.tasarim.pushButton_sil.clicked.connect(self.silme)
        self.tasarim.pushButton_Esittir.clicked.connect(self.islemYapma)
        self.tasarim.pushButton_mutlak.clicked.connect(self.islemYapma)
        self.tasarim.pushButton_koklu.clicked.connect(self.islemYapma)
        self.tasarim.pushButton_prntz_A.clicked.connect(self.yazdir)
        self.tasarim.pushButton_prntz_K.clicked.connect(self.yazdir)
        self.tasarim.pushButton_mod.clicked.connect(self.yazdir)
        self.tasarim.pushButton_faktoriyel.clicked.connect(self.islemYapma)
        self.tasarim.pushButton_pozitif_negatif.clicked.connect(self.islemYapma)
        self.tasarim.pushButton_nokta.clicked.connect(self.yazdir)
        
        
   
    def islemYapma(self):
        sender_btn=self.sender()
        if sender_btn:
            if sender_btn.text().find('|x|')==0:
                self.sonuc=abs(float(self.islem_text))
            elif sender_btn.text().find('√x')==0:
                self.sonuc=math.sqrt(float(self.islem_text))
            elif sender_btn.text().find('+/-')==0:
                self.sonuc=float(self.islem_text)*-1
            elif sender_btn.text().find('x!')==0:
                self.sonuc=math.factorial(int(self.islem_text))
            else:
                self.sonuc =eval(self.islem_text)
        self.islem_text=str(self.sonuc)
        self.tasarim.label.setText(self.islem_text)
        
    def silme(self):
        self.islem_text=''
        self.tasarim.label.setText(self.islem_text)
    
    def yazdir(self):
        sender_button=self.sender()
        if sender_button:
            self.islem_text+=sender_button.text()
            self.tasarim.label.setText(self.islem_text)

    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())