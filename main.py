from tkinter import *
from PIL import Image,ImageTk
import random

#cores

co0 = '#f0f3f5'
co1 = '#feffff'
co2 = '#3fb5a3'
co3 = '#38576b'
co4 = '#403d3d'


#criando janela
janela = Tk()
janela.title('')
janela.geometry('400x260')
janela.configure(background=co1)
janela.resizable(width=False,height=False)


#criando frames -------
frame_cima = Frame(janela,width=500,height=50,background=co2)
frame_cima.grid(row=0, column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width=500,height=210,background=co4)
frame_baixo.grid(row=1, column=0,pady=1,padx=0,sticky=NSEW)

#configurando frame_cima
l_app = Label(frame_cima,text='Acenda a Lâmpada',anchor=NE,font=('Ivy 20 '),background=co2,fg=co0)
l_app.place(x=5,y=5)

#onfigurando frame_baixo

img_2 = Image.open('2.png')
img_2 = img_2.resize((40,40))
img_2 = ImageTk.PhotoImage(img_2)

img_3 = Image.open('3.png')
img_3 = img_3.resize((40,40))
img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open('4.png')
img_4 = img_4.resize((40,40))
img_4 = ImageTk.PhotoImage(img_4)

img_5 = Image.open('5.png')
img_5 = img_5.resize((40,40))
img_5 = ImageTk.PhotoImage(img_5)

l_img = Label(frame_baixo,image=img_2,background=co4)
l_img.place(x=30,y=10)

l_estado = Label(frame_baixo,text='Estou com medo',anchor=NW,font=('Ivy 13'),background=co4,fg=co1)
l_estado.place(x=80,y=20)
global controle
global contador
controle = ['lampada_1','lampada_2','lampada_3']

def ligar_lampada(i):
    global controle
    lista = i

    #desabilitando o botão clicado
    if lista[1] == 'Kitchen switch':
        b_interruptor_1['state'] = 'disable'
    elif lista[1] == 'Room switch':
        b_interruptor_2['state'] = 'disable'
    elif lista[1] == 'bathroom switch':
        b_interruptor_3['state'] = 'disable'
    elif lista[1] == 'Balcony switch':
        b_interruptor_4['state'] = 'disable'
    elif lista[1] == 'bathroom switch-2':
        b_interruptor_5['state'] = 'disable'

    def substituir_valor(i):
        global controle
        nova_lista = []

        for string in controle:
            novo_valor = string.replace(i[0],i[1])
            nova_lista.append(novo_valor)
        controle = nova_lista
        print(nova_lista)
    valor_selecionado = random.sample(lista[0],1)[0]

    print(valor_selecionado)
    if int(valor_selecionado)==1:
        if controle[0] == 'lampada_1':
            l_img_1['image']=img_lampada_on
            l_img['image'] = img_3
            l_estado['text'] = 'Ok Obrigado'
            substituir_valor(['lampada_1',str(1)])
        else:
            if controle[1] == 'lampada_2':
                l_img_2['image']=img_lampada_on
                l_img['image'] = img_4
                l_estado['text'] = 'Por Favor, acenda  a ultima'
                substituir_valor(['lampada_2',str(2)])
            else:
                if controle[2] == 'lampada_3':
                    l_img_3['image']=img_lampada_on
                    l_img['image'] = img_5
                    l_estado['text'] = 'Muito Obrigado !!!'
                    substituir_valor(['lampada_1',str(2)])


img_lampada_on = Image.open('1.png')
img_lampada_on = img_lampada_on.resize((110,110))
img_lampada_on = ImageTk.PhotoImage(img_lampada_on)

img_lampada_off = Image.open('0.png')
img_lampada_off = img_lampada_off.resize((110,110))
img_lampada_off = ImageTk.PhotoImage(img_lampada_off)

l_img_1 = Label(frame_baixo,image=img_lampada_off,background=co4)
l_img_1.place(x=5,y=70)
l_img_2 = Label(frame_baixo,image=img_lampada_off,background=co4)
l_img_2.place(x=105,y=70)
l_img_3 = Label(frame_baixo,image=img_lampada_off,background=co4)
l_img_3.place(x=205,y=70)

lista = [1,0,1,1,0]

b_interruptor_1 = Button(frame_baixo,command=lambda i=[lista,'Kitchen switch']:ligar_lampada(i),width=13,text='Kitchen switch',relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 7 bold'),background=co4,fg=co1)
b_interruptor_1.place(x=300,y=50)
b_interruptor_2 = Button(frame_baixo,command=lambda i=[lista,'Room switch']:ligar_lampada(i),width=13,text='Room switch',relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 7 bold'),background=co4,fg=co1)
b_interruptor_2.place(x=300,y=80)
b_interruptor_3 = Button(frame_baixo,command=lambda i=[lista,'bathroom switch']:ligar_lampada(i),width=13,text='bathroom switch',relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 7 bold'),background=co4,fg=co1)
b_interruptor_3.place(x=300,y=110)
b_interruptor_4 = Button(frame_baixo,command=lambda i=[lista,'Balcony switch']:ligar_lampada(i),width=13,text='Balcony switch',relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 7 bold'),background=co4,fg=co1)
b_interruptor_4.place(x=300,y=140)
b_interruptor_5 = Button(frame_baixo,command=lambda i=[lista,'bathroom switch-2']:ligar_lampada(i),width=13,text='bathroom switch-2',relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 7 bold'),background=co4,fg=co1)
b_interruptor_5.place(x=300,y=170)

janela.mainloop()