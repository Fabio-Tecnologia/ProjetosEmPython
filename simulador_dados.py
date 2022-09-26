import random
import PySimpleGUI as sg 


class SimuladorDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar valor do dado?: '
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado')],
            [sg.Button('sim'),sg.Button('nao')]
        ]


    def Iniciar(self):
        #criação da Janela
        self.janela = sg.Window('Simulador de Dado', Layout=self.layout)
        #Leitura dos valores da tela
        self.evento, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores    
        try:
            if self.evento == 'sim' or self.evento == 's':
                self.ValorDoDado()
            elif self.evento == 'nao' or self.evento == 'n': 
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta.')

        
        
    def ValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

#Instanciar a classe
simulador = SimuladorDados()
simulador.Iniciar()




