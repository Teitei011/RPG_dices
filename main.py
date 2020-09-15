import random as r
from time import time
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

'''
    Programa que vai rolar os dados de d&d como o anterior fazia,
    mas agora usando da biblioteca kivy e de PO

'''

class Dices(Screen,FloatLayout, ButtonBehavior):

    # A seed nao esta funcionando
    r.seed = time()  # Gerando a seed para o numero aleatorio

    label_wid = ObjectProperty()
    info = StringProperty()


    # Para vantagem o valor é 1, para desvantagem o valor é -1. Para o valor neutro o valor é 0

    global determinacao_de_vantagem_e_desvantagem
    determinacao_de_vantagem_e_desvantagem = 0

    global rolls
    rolls = 1

    def roll_more(self, number):
        '''
            Com isso eu consigo fazer rolar os dados o numero suficiente de vezes para a quantidade de dados.

            Estava funcionando, mas por algum motivo escuso parou de funcionar
        '''
        global rolls
        rolls = number
        print(rolls)

    def vantagem(self):
        '''
            Desta forma eu consigo falar para o computador quando há a necessidade de vantagem e de desvantagem
        '''
        print("Vantagem")
        global determinacao_de_vantagem_e_desvantagem
        determinacao_de_vantagem_e_desvantagem = 1

    def desvantagem(self):
        '''
            Desta forma ele coloca como desvantagem a determinacao
        '''
        print("Desvantagem")
        global determinacao_de_vantagem_e_desvantagem
        determinacao_de_vantagem_e_desvantagem = -1

    def neutro(self):
        '''
            Desta forma eu volto para a forma neutra, com isso posso fazer varias vezes. Isso nao vai dar certo
            Tenho que achar uma forma de colocar estes tres modulos numa coisa só, pq senao nao vou conseguir atualizar
        '''
        print("Neutro")
        global determinacao_de_vantagem_e_desvantagem
        determinacao_de_vantagem_e_desvantagem = 0

    def rolar_dados(self, numero):
        '''
            Parte responsavel para rodar os dados com vantagem/desvantagem/neutro. Assim como fazer a soma caso foi
            requisitado jogar mais de uma vez
        '''
        global rolls
        global determinacao_de_vantagem_e_desvantagem

        valores =[]

        for j in range(2): # Para vantagem e desvantagem
            self.soma = 0
            for i in range(rolls):
                self.soma += r.randint(1, numero)

            valores.append(self.soma)

        print("Os valores que foram jogados foi de:")
        print(valores)

        # Colocar a parte para vantagem, desvantagens e cenarios neutros
        #TODO: NAO ESTA PEGANDO DIREITO ISSO
        if determinacao_de_vantagem_e_desvantagem == 1:
            print("Passou por aqui")
            soma = max(valores)

        elif determinacao_de_vantagem_e_desvantagem == -1: # Com isso eu pego o menor valor do array
            soma = min(valores)

        else: # Caso nao há vantagem e nem desvantagem
            soma = valores[0]

        # Enviando para o texto
        self.label_wid.text = str(soma)


    def mostra(self):
        self.label_wid.text = "Made by Teitei"

    def quinta_serie(self):
        fart = SoundLoader.load("Fart.wav")
        fart.play()


presentation = Builder.load_file("myfirst.kv")


class MyfirstApp(App):
    def build(self):
        self.title = "dnd dice by teitei"
        return presentation

if __name__ == '__main__':
    MyfirstApp().run()