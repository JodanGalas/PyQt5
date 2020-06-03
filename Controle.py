from PyQt5 import uic, QtWidgets

def listar_dados():
    dado_lido = lista.lineEdit.text()
    lista.listWidget.addItem(dado_lido)
    lista.lineEdit.setText("")
def deletar():
    lista.listWidget.clear()

app = QtWidgets.QApplication([])
lista = uic.loadUi("Pratica.ui")
lista.pushButton.clicked.connect(listar_dados)
lista.pushButton_2.clicked.connect(deletar)

lista.show()
app.exec()

