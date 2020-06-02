from PyQt5 import uic, QtWidgets

def listar_dados():
    print("Listar")
def deletar():
    print("deletar")

app = QtWidgets.QApplication([])
lista = uic.loadUi("Prática-ListWidget.ui")
lista.pushButton.clicked.connect(listar_dados)
lista.pushButton_2.clicked.connect(deletar)

lista.show()
app.exec()

