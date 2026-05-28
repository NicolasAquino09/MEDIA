import PyQt6.QtWidgets
import PyQt6.uic


app = PyQt6.QtWidgets.QApplication([])
tela = PyQt6.uic.loadUi("mediacorreta.ui")
def calcular_media():
    try:
        nota1 = float(tela.txt_nota1.text())
        nota2 = float(tela.txt_nota2.text())
        nota3 = float(tela.txt_nota3.text())

        media = (nota1 + nota2 + nota3) / 3

        media = round(media,2)

      
        if media >= 7:
          status = ("Situação: Aprovado")

        elif media < 7:
             status = ("Situação: Reprovado:")
        
        elif media < 4:
             status = ("Situação: Recuperação")


        tela.lbl_resultado.setText(f"Média: {media} Situação: {status}")
       

        
    except ValueError:
        tela.lbl_resultado.setText("Erro: digite apenas números")

tela.btn_calcular.clicked.connect(calcular_media)

def limpar():
    tela.txt_nome.setText("")
    tela.txt_nota1.setText("")
    tela.txt_nota2.setText("")
    tela.txt_nota3.setText("")

tela.btn_limpar.clicked.connect(limpar)





tela.show()
app.exec()