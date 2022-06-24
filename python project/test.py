from cgi import test
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
        update.usd = soup.find( class_ = "style23" )
        print('1 $ cost in DZD: '+str(update.usd)[133:141])
        update.euro = soup.find( class_ = "style23" )
        print('1 € cost in DZD: '+str(update.euro)[160:167])
    
    # usd1 = update()
    # print(str(usd1)[133:141])

    update()
    data_exchange.test = update.usd
    data_exchange.test1 = str(data_exchange.test)

    fps = 15
    app = QtCore.QCoreApplication(sys.argv)
    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.setInterval(90000 // fps)
    timer.start()
    app.exec()

data_exchange(test)

print(data_exchange.test)

