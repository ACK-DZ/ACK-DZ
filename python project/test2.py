import sys
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtWidgets import QLineEdit, QLineEdit, QApplication
import sys
from PyQt6.QtGui import QPixmap
from bs4 import BeautifulSoup
import requests


def data_exchange():
    def update():


        URL = 'https://www.bank-of-algeria.dz/'
        # class list set
        class_list = set()
        # Page content from Website URL
        page = requests.get( URL )
        # parse html content
        soup = BeautifulSoup( page.content , 'html.parser')
        usd = soup.find( class_ = "style23" )
        print('1 $ cost in DZD: '+str(usd)[133:141])
        euro = soup.find( class_ = "style23" )
        print('1 € cost in DZD: '+str(euro)[160:167])
        return(usd,euro)
    
    fps = 15
    ussd=update()
    eeuro=update()
    app = QtCore.QCoreApplication(sys.argv)
    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.setInterval(90000 // fps)
    timer.start()
    app.exec()
    return(ussd,eeuro)


class page(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Currency change')
        self.resize(300,400)
        #w.move()
        self.setStyleSheet('background-color:#17202b;')
        self.setWindowIcon(QtGui.QIcon("exchange.png"))
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        # BUTON CONFIRME AND EXIT

        self.btn1 = QtWidgets.QPushButton(" Exit ",self)
        self.btn1.resize(80,30)
        self.btn1.setStyleSheet('background-color:white; border: 2px solid black; border-radius:8px;font-weight: bold')
        self.btn1.move(112,350)
        self.btn1.setToolTip('if you want to leave this programme click exit')
        self.btn1.clicked.connect(exit)
        self.btn1.setIcon(QtGui.QIcon(".\exit-button-icon-14.jpg"))

        # Label text currency DZD

        self.lbl1= QtWidgets.QLabel('<b> 1 $ : '+ str(data_exchange)[133:140] +" DZD"+'</b>',self)
        self.lbl1.setStyleSheet('color: white; font-size:12px; font-family:tajwal;')
        self.lbl1.move(110,250)

        self.lbl2= QtWidgets.QLabel('<b> 1 € : '+ str(data_exchange)[160:167] +" DZD"+'</b>',self)
        self.lbl2.setStyleSheet('color: white; font-size:12px; font-family:tajwal;')
        self.lbl2.move(110,270)

        self.lbl3= QtWidgets.QLabel(' Choose Currency',self)
        self.lbl3.setStyleSheet('color: black; font-size:12px; font-family:tajwal; background-color:white; border: 2px solid black; border-radius:4px;font-weight: bold')
        self.lbl3.resize(120 , 20)
        self.lbl3.move(80,180)

            #  List select
        self.box1 = QtWidgets.QRadioButton(' USD ',self)
        self.box1.move(80,300)
        self.box1.setStyleSheet("color: white; font-size:14px; font-family:tajwal;font-weight: bold")

        self.box2 = QtWidgets.QRadioButton(' EURO ',self)
        self.box2.move(160,300)
        self.box2.setStyleSheet("color: white; font-size:14px; font-family:tajwal;font-weight: bold")

        usd1= str(data_exchange)[133:140]
        euro1= str(data_exchange)[160:167]

        def usd_calc():
            try: 
                Text = self.fieldEdit.text()
                self.lbl3.setNum(eval(Text)*float(usd1))
            except:
                print('error')

        def euro_calc():
            try: 
                Text = self.fieldEdit.text()
                self.lbl3.setNum(eval(Text)*float(euro1))
            except:
                print('error')

        def dzd_calc():
            try: 
                Text = self.fieldEdit.text()
                self.lbl3.setNum(eval(Text)//int(euro1))
            except:
                print('error')

        self.fieldEdit = QLineEdit("  Enter your value",self)
        self.fieldEdit.move(80,210)
        self.fieldEdit.resize(120 , 20)
        self.fieldEdit.setStyleSheet('color: black; font-size:12px; font-family:tajwal; background-color:white; border: 2px solid black; border-radius:4px;font-weight: bold')


        self.fieldEdit2 = QLineEdit("€ / $",self)
        self.fieldEdit2.move(200,210)
        self.fieldEdit2.resize(35 , 20)
        self.fieldEdit2.setStyleSheet('color: black; font-size:12px; font-family:tajwal; background-color:white; border: 2px solid black; border-radius:4px;font-weight: bold')
        
        eur = ("   €")
        dollar = ("   $")
        
        # self.fieldEdit2 = QLineEdit(dollar,self)
        # self.fieldEdit2.move(240,210)
        # self.fieldEdit2.resize(35 , 20)
        # self.fieldEdit2.setStyleSheet('color: black; font-size:12px; font-family:tajwal; background-color:white; border: 2px solid black; border-radius:4px;font-weight: bold')

        # fieldEdit.setText('Enter your value')

        self.lbl4= QtWidgets.QLabel('DZD',self)
        self.lbl4.setStyleSheet('color: black; font-size:12px; font-family:tajwal; background-color:white; border: 2px solid black; border-radius:4px;font-weight: bold')
        self.lbl4.resize(35 , 20)
        self.lbl4.move(200,180)
        
        def check():
                if self.box2.isChecked():
                
                    self.fieldEdit2.setText(eur)
                    self.fieldEdit.setText('')
                    euroo = self.fieldEdit.textChanged.connect(euro_calc)
                    self.lbl3.setText('')
                else:
                    if self.box1.isChecked:
                        self.fieldEdit2.setText(dollar)
                        self.fieldEdit.setText('')
                        self.fieldEdit.textChanged.connect(usd_calc)
                        self.lbl3.setText('')
        
        self.box1.clicked.connect(check)
        self.box2.clicked.connect(check)

        self.banner = QtWidgets.QLabel(self)
        self.p = QPixmap('.\money.png')
        self.banner.setPixmap(self.p)
        self.banner.move(85,15)

        self.change = QtWidgets.QLabel(self)
        self.c = QPixmap('.\exchanged.png')
        self.change.setPixmap(self.c)
        self.change.move(35,182)
        
        self.euro_ico = QtWidgets.QLabel(self)
        self.ep = QPixmap('.\euro.png')
        self.euro_ico.setPixmap(self.ep)
        self.euro_ico.move(1,340)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()


    def mouseMoveEvent(self, event):
      self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
      self.dragPos = event.globalPosition().toPoint()
      event.accept()

app = QtWidgets.QApplication(sys.argv)
page = page()
page.show()
sys.exit(app.exec())   
