import os
import sys
from threading import *


from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
from design import *


class Novo(QMainWindow, Ui_MainWindow, QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnConectarUsuario.clicked.connect(self.conectar_usuario)
        self.btnComprarDigital.clicked.connect(self.botao_compra_digital)
        self.btnComprarBinario.clicked.connect(self.botao_compra_binario)
        self.btnVenderBinario_3.clicked.connect(self.botao_venda_binaria)
        self.btnVenderDigital.clicked.connect(self.botao_venda_digital)
        self.btnDesconectarUsuario.clicked.connect(self.botao_reconectar)

        self.btnDesconectarUsuario.setDisabled(True)
        self.btnComprarBinario.setDisabled(True)
        self.btnComprarDigital.setDisabled(True)
        self.btnVenderBinario_3.setDisabled(True)
        self.btnVenderDigital.setDisabled(True)




    def conectar_usuario(self):

        if self.radioBtnTreino.isChecked():
            tipo = "PRACTICE"
        elif self.radioBtnOficial.isChecked():
            tipo = "REAL"
        else:
            print("ERRO TREINO ou OFICIAL")

        email1 = self.inputEmail_1.text()
        senha1 = self.inputSenha_1.text()

        email2 = self.inputEmail_2.text()
        senha2 = self.inputSenha_2.text()

        email3 = self.inputEmail_3.text()
        senha3 = self.inputSenha_3.text()

        email4 = self.inputEmail_4.text()
        senha4 = self.inputSenha_4.text()

        email5 = self.inputEmail_5.text()
        senha5 = self.inputSenha_5.text()

        email6 = self.inputEmail_6.text()
        senha6 = self.inputSenha_6.text()

        email7 = self.inputEmail_7.text()
        senha7 = self.inputSenha_7.text()

        email8 = self.inputEmail_8.text()
        senha8 = self.inputSenha_8.text()

        email9 = self.inputEmail_9.text()
        senha9 = self.inputSenha_9.text()

        email10 = self.inputEmail_10.text()
        senha10 = self.inputSenha_10.text()

        dinheiro_bin = self.inputDinheiroBinario.text()
        moeda_bin = self.inputMoedaBinario.currentText()
        tempo_bin = self.inputTempoBinario.text()

        dinheiro_dig = self.inputDinheiroDigital.text()
        moeda_dig = self.inputMoedaDigital.currentText()
        tempo_dig = self.inputTempoDigital.text()





        if self.radioBtnUpBinario.isChecked():
            acao_bin = "put"
        elif self.radioBtnDownBinario.isChecked():
            acao_bin = "call"
        else:
            print("ERRO UP ou DOWN Binario")


        if self.radioBtnUpDigital.isChecked():
            acao_dig = "put"
        elif self.radioBtnDownDigital.isChecked():
            acao_dig = "call"
        else:
            print("ERRO UP ou DOWN Digital")


        f = open('comprar_digital.txt', 'w')
        f.write('False')
        f.close()
        f = open('comprar_binario.txt', 'w')
        f.write('False')
        f.close()

        f = open('stop.txt', 'w')
        f.write('False')
        f.close()

        # if self.radioBtnTreino.isChecked():
        #     self.radioBtnTreino.setChecked(True)
        #     self.radioBtnTreino.setEnabled(False)
        # else:
        #     self.radioBtnOficial.setChecked(True)
        #     self.radioBtnOficial.setEnabled(False)



        class App1(Thread):
            def run(self):
                if email1 != "" and senha1 != "":
                    os.system(f'python users/usuario1.py {email1} {senha1} {dinheiro_bin} {moeda_bin} {acao_bin} {tempo_bin} {dinheiro_dig} {acao_dig} {moeda_dig} {tempo_dig} {tipo}')

        class App2(Thread):
            def run(self):
                if email2 != "" and senha2 != "":
                    os.system(f'python users/usuario2.py {email2} {senha2} {dinheiro_bin} {moeda_bin} {acao_bin} {tempo_bin} {dinheiro_dig} {acao_dig} {moeda_dig} {tempo_dig} {tipo}')

        class App3(Thread):
            def run(self):
                if email3 != "" and senha3 != "":
                    os.system(f'python users/usuario3.py {email3} {senha3} {dinheiro_bin} {moeda_bin} {acao_bin} {tempo_bin} {dinheiro_dig} {acao_dig} {moeda_dig} {tempo_dig} {tipo}')

        class App4(Thread):
            def run(self):
                if email4 != "" and senha4 != "":
                    os.system(f'python users/usuario4.py {email4} {senha4} {dinheiro_bin} {moeda_bin} {acao_bin} {tempo_bin} {dinheiro_dig} {acao_dig} {moeda_dig} {tempo_dig} {tipo}')

        class App5(Thread):
            def run(self):
                if email5 != "" and senha5 != "":
                    os.system(f'python users/usuario5.py {email5} {senha5} {dinheiro_bin} {moeda_bin} {acao_bin} {tempo_bin} {dinheiro_dig} {acao_dig} {moeda_dig} {tempo_dig} {tipo}')

        class App6(Thread):
            def run(self):
                if email6 != "" and senha6 != "":
                    os.system(
                        f'python users/usuario6.py {email6} {senha6} {dinheiro_bin} {moeda_bin} {acao_bin} {tempo_bin} {dinheiro_dig} {acao_dig} {moeda_dig} {tempo_dig} {tipo}')

        class App7(Thread):
            def run(self):
                if email7 != "" and senha7 != "":
                    os.system(
                        f'python users/usuario7.py {email7} {senha7} {dinheiro_bin} {moeda_bin} {acao_bin} {tempo_bin} {dinheiro_dig} {acao_dig} {moeda_dig} {tempo_dig} {tipo}')

        class App8(Thread):
            def run(self):
                if email8 != "" and senha8 != "":
                    os.system(
                        f'python users/usuario8.py {email8} {senha8} {dinheiro_bin} {moeda_bin} {acao_bin} {tempo_bin} {dinheiro_dig} {acao_dig} {moeda_dig} {tempo_dig} {tipo}')

        class App9(Thread):
            def run(self):
                if email9 != "" and senha9 != "":
                    os.system(
                        f'python users/usuario9.py {email9} {senha9} {dinheiro_bin} {moeda_bin} {acao_bin} {tempo_bin} {dinheiro_dig} {acao_dig} {moeda_dig} {tempo_dig} {tipo}')

        class App10(Thread):
            def run(self):
                if email10 != "" and senha10 != "":
                    os.system(
                        f'python users/usuario10.py {email10} {senha10} {dinheiro_bin} {moeda_bin} {acao_bin} {tempo_bin} {dinheiro_dig} {acao_dig} {moeda_dig} {tempo_dig} {tipo}')


        app1 = App1()
        app2 = App2()
        app3 = App3()
        app4 = App4()
        app5 = App5()
        app6 = App6()
        app7 = App7()
        app8 = App8()
        app9 = App9()
        app10 = App10()

        app1.start()
        app2.start()
        app3.start()
        app4.start()
        app5.start()
        app6.start()
        app7.start()
        app8.start()
        app9.start()
        app10.start()

        self.btnConectarUsuario.setDisabled(True)
        self.btnDesconectarUsuario.setEnabled(True)


        self.btnComprarBinario.setEnabled(True)
        self.btnComprarDigital.setEnabled(True)
        self.btnVenderBinario_3.setDisabled(True)
        self.btnVenderDigital.setDisabled(True)



    def botao_compra_digital(self):
        self.btnVenderDigital.setEnabled(True)
        self.btnComprarDigital.setDisabled(True)
        f = open('comprar_digital.txt', 'w')
        f.write('True')
        f.close()
        f = open('digital.txt', 'w')
        f.write('False')
        f.close()

    def botao_compra_binario(self):
        self.btnVenderBinario_3.setEnabled(True)
        self.btnComprarBinario.setDisabled(True)
        f = open('comprar_binario.txt', 'w')
        f.write('True')
        f.close()
        f = open('binario.txt', 'w')
        f.write('False')
        f.close()

    def botao_venda_digital(self):
        self.btnComprarDigital.setEnabled(True)
        self.btnVenderDigital.setDisabled(True)
        f = open('digital.txt', 'w')
        f.write('True')
        f.close()

    def botao_venda_binaria(self):
        self.btnComprarBinario.setEnabled(True)
        self.btnVenderBinario_3.setDisabled(True)
        f = open('binario.txt', 'w')
        f.write('True')
        f.close()

    def botao_reconectar(self):
        self.btnConectarUsuario.setEnabled(True)
        self.btnDesconectarUsuario.setDisabled(True)
        f = open('stop.txt', 'w')
        f.write('True')
        f.close()




if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
