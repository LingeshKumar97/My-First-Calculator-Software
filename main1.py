
'''
program Name: Design 1
detail:
developer:
date:
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.uic import loadUi

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self,parent = None):
        super(MainWindow,self).__init__()

        #load view
        loadUi('view/test1.ui',self)
        self.addition_radioButton.setChecked(True)

        #register callbasks
        self.calculate_pushbutton.clicked.connect(self.compute)
        self.clear_pushButton_2.clicked.connect(self.clear)
        #

    def compute(self):
        a=self.InputA_lineEdit.text()
        b=self.InputB_lineEdit.text()



        if a.isnumeric() and b.isnumeric():

            

            if self.addition_radioButton.isChecked():
                c = int(a) + int(b)
            elif self.substraction_radioButton.isChecked():
                c = int(a) - int(b)
            elif self.multiplication_radioButton.isChecked():
                c = int(a) * int(b)
            elif self.division_radioButton.isChecked():
                c = int(a) / int(b)
            else:
                c = "Invalid Operation"
            

            print("Compute was clicked",c)
            self.lcdNumber.display(str(c))
        else:
            self.answer_label_5.setText("Invalid")
        

    def clear(self):
        self.InputA_lineEdit.clear()
        self.InputB_lineEdit.clear()
        self.answer_label_5.setText("")
        self.lcdNumber.display("0")
        print("Clear was clicked")
       


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)

    myapp = MainWindow()
    myapp.show()


    try:
        
        sys.exit(app.exec_())
    except:
        print("Closing App")
