# ch 5.2.1 ui.py 
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox)    

from PyQt5.QtGui import QIcon   # icon을 추가하기 위한 라이브러리     
from PyQt5 import QtCore    # 모듈 추가 

class View(QWidget): 
    def __init__(self):
        super().__init__()  
        self.initUI()  
        
    def initUI(self):
        self.te1 = QPlainTextEdit()     # 텍스트 에디트 생성 
        self.te1.setReadOnly(True)  #텍스트 에디트 위젯을 읽기만 가능하도록 수정 
        
        self.le1 = QLineEdit('0', self)     # 라인 에디트1 추가 
        self.le1.setAlignment(QtCore.Qt.AlignRight) 
        self.le1.setFocus(True) # 포커스 설정 
        self.le1.selectAll() # 텍스트 전체 선택 
        
        self.le2 = QLineEdit('0', self)     # 라인 에디트2 추가 
        self.le2.setAlignment(QtCore.Qt.AlignRight)
        
        self.cb = QComboBox(self)
        self.cb.addItems(['+', '-', '*', '/'])     # 콤포 박스 항목
        
        hbox_formular = QHBoxLayout() # 새로 정의한 위젯을 QHBoxLayout에 배치 
        hbox_formular.addWidget(self.le1) 
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)
        
        self.btn1 = QPushButton('Calc', self)    # 버튼 이름 변경  
        self.btn2 = QPushButton('Clear', self)  # 버튼2 추가 
                   
        hbox = QHBoxLayout()    # 수평 박스 레이아웃을 추가하고 버튼1, 2 추가 
        hbox.addStretch(1)  # 공백
        hbox.addWidget(self.btn1)   # 버튼1 배치 
        hbox.addWidget(self.btn2)   # 버튼2 배치  
        
        vbox = QVBoxLayout()    # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1) # 수직 레이아웃에 텍스트 에디트 위젯 추가 
        vbox.addLayout(hbox_formular) # hbox_formular 배치 
        vbox.addLayout(hbox)    # btn1 위치에 hbox 배치 
        vbox.addStretch(1) 
        
        self.setLayout(vbox)    # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정 
        
        self.setWindowTitle('Calculator')  
        self.setWindowIcon(QIcon('icon.png'))   # 윈도 아이콘 추가 
        self.resize(256, 256)  
        self.show()          
        

    def setDisplay(self, text):   # 버튼 클릭할 때 동작하는 함수 : 메시지 박스 출력        
        self.te1.appendPlainText(text)  

    
    def clearMessage(self):  # 버튼2 핸들러 함수 정의 
        self.te1.clear()
    
       

    
