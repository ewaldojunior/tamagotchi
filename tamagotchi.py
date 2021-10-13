from tkinter import *
import time

class Tamagotchi:
    energia_max = 50
    saciedade_max = 50
    limpeza_max = 50
    diamantes = 0
    idade = 0

    #construtor
    def __init__(self, energia, saciedade, limpeza):
        self.energia = energia
        self.saciedade = saciedade
        self.limpeza = limpeza

    #setters and getters
    @property
    def energia(self):
        return self._energia
    @energia.setter
    def energia(self, energia):
        self._energia= energia

    @property
    def saciedade(self):
        return self._saciedade
    @saciedade.setter
    def saciedade(self, saciedade):
        self._saciedade= saciedade

    @property
    def limpeza(self):
        return self._limpeza
    @limpeza.setter
    def limpeza(self, limpeza):
        self._limpeza= limpeza


    def jogar(self):
        #decorador
        def contador(func):
            def envoltoria(*arg):
                envoltoria.contador += 1
                return func(*arg)
            envoltoria.contador = 0
            return envoltoria

        @contador
        def resp_perguntas():
            print(lb.get(ACTIVE))
            resposta = input("Resposta: ")
            resposta.lower()
            
            for item in perguntas:
                if resposta == item[1]:
                    print("Resposta correta. +1 diamante")
                    self.diamantes += 1
                    break
            else:
                print("Você errou.")
            
            if(resp_perguntas.contador != 0 and resp_perguntas.contador % 5 == 0):
                self.idade += 1
                print(f"O pet aumentou +1 de idade, ficou com: {self.idade}")
            
            lb.delete(ANCHOR)

        def parar():
            janela.destroy()
            return

        # Interface gráfica - Tkinter
        janela = Tk()
        janela.geometry('500x450+500+200')
        janela.title('Tamagotchi')
        janela.config(bg='#223441')
        janela.resizable(width=False, height=False)

        frame = Frame(janela)
        frame.pack(pady=10)

        texto = Label(frame,
        text="Primeiro clique na pergunta nesta lista abaixo e depois no botão Responder",
        font=('Times', 12))
        texto.pack(side=TOP, fill=BOTH)

        lb = Listbox(
            frame,
            width=50,
            height=8,
            font=('Times', 12),
            bd=0,
            fg='#464646',
            highlightthickness=0,
            selectbackground='#a6a6a6',
            activestyle="none", 
        )
        lb.pack(side=LEFT, fill=BOTH)

        perguntas = [
            ['Quanto é 1 + 1?', '2'],
            ['Quanto é 2 x 3?', '6'],
            ['Qual animal é simbolizado no Python?', 'cobra'],
            ['Em qual ano foi criado o Python?', '1991'],
            ['Qual linguagem desenvolveu este Tamagotchi?', 'python'],
            ['Qual biblioteca usada para interface gráfica no Python?','tkinter'],
            ]

        for item in perguntas:
            lb.insert(END, item[0])

        sb = Scrollbar(frame)
        sb.pack(side=RIGHT, fill=BOTH)

        lb.config(yscrollcommand=sb.set)
        sb.config(command=lb.yview)

        button_frame = Frame(janela)
        button_frame.pack(pady=20)

        responder = Button(
            button_frame,
            text='Responder',
            font=('times 14'),
            bg='#78c091',
            padx=20,
            pady=10,
            command=resp_perguntas
        )
        responder.pack(fill=BOTH, expand=True, side=LEFT)
        
        sair = Button(
            button_frame,
            text='Parar',
            font=('times 14'),
            bg='#e85f5c',
            padx=20,
            pady=10,
            command=parar
        )
        sair.pack(fill=BOTH, expand=True, side=LEFT)

        janela.mainloop()
    
        self.energia -= 1
        self.limpeza -= 1
        self.saciedade -= 1
    
    def comer(self):
        self.saciedade += 5
        self.limpeza -= 1
        if self.saciedade > self.saciedade_max:
            self.saciedade = self.saciedade_max
        return self.saciedade
    
    def tomar_banho(self):
        self.limpeza += 5
        self.energia -= 1
        if self.limpeza > self.limpeza_max:
            self.limpeza = self.limpeza_max
        return self.limpeza

    def dormir(self):
        self.energia += 5
        self.saciedade -= 2
        if self.energia > self.energia_max:
            self.energia = self.energia_max
        return self.energia

#Main
pet = Tamagotchi(6, 5, 6)

while ((pet.energia > 0) and (pet.saciedade > 0) and (pet.limpeza > 0)):
    resposta = input("Olá, eu sou seu Tamagotchi :) \nO que você deseja fazer comigo agora? \n1- Jogar (-1 saciedade / -1 energia / -1 limpeza) \n2- Comer (+5 saciedade / -1 limpeza) \n3- Tomar banho (+5 limpeza / -1 energia) \n4- Dormir (+5 energia / -2 saciedade) \n5- Visualizar meu status\n-> Escolha uma opção: ")

    if resposta == '1':
        pet.jogar()
    elif resposta == '2':
        pet.comer()
        print("Amo comer, obrigado por me alimentar! ^^")
        time.sleep(2)
    elif resposta == '3':
        pet.tomar_banho()
        print("Ok, vou tomar banho... espero que a água não esteja gelada \o/")
        time.sleep(2)
    elif resposta == '4':
        pet.dormir()
        print("ZzZzZzZ soninho bom! Espera eu acordar")
        time.sleep(5)
    elif resposta == '5':
        print(f"---------------\nEnergia: {pet.energia} \nSaciedade: {pet.saciedade} \nLimpeza: {pet.limpeza} \nDiamantes: {pet.diamantes} \nIdade: {pet.idade} \n---------------")
    else:
        print("Escolha um número válido!")

else:
    print("O seu pet morreu :( \nEle vai ser resetado e você poderá jogar quantas vezes quiser depois!")