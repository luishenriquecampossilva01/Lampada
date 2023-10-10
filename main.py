from tkinter import *
from PIL import Image,ImageTk

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

img_3 = Image.open('2.png')
img_3 = img_3.resize((40,40))
img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open('2.png')
img_4 = img_4.resize((40,40))
img_4 = ImageTk.PhotoImage(img_4)

img_5 = Image.open('2.png')
img_5 = img_5.resize((40,40))
img_5 = ImageTk.PhotoImage(img_5)

l_img = Label(frame_baixo,image=img_2,background=co4)
l_img.place(x=30,y=10)

l_estado = Label(frame_baixo,text='Estou com medo',anchor=NW,font=('Ivy 13'),background=co4,fg=co1)
l_estado.place(x=80,y=20)

img_lampada_on = Image.open('1.png')
img_lampada_on = img_lampada_on.resize((110,110))
img_lampada_on = ImageTk.PhotoImage(img_lampada_on)

img_lampada_off = Image.open('0.png')
img_lampada_off = img_lampada_off.resize((110,110))
img_lampada_off = ImageTk.PhotoImage(img_lampada_off)

l_img = Label(frame_baixo,image=img_lampada_off,background=co4)
l_img.place(x=5,y=70)
l_img = Label(frame_baixo,image=img_lampada_off,background=co4)
l_img.place(x=105,y=70)
l_img = Label(frame_baixo,image=img_lampada_off,background=co4)
l_img.place(x=205,y=70)


b_interruptor_1 = Button(frame_baixo,width=13,text='Kitchen switch',relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 7 bold'),background=co4,fg=co1)
b_interruptor_1.place(x=300,y=50)
b_interruptor_2 = Button(frame_baixo,width=13,text='Room switch   ',relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 7 bold'),background=co4,fg=co1)
b_interruptor_2.place(x=300,y=80)
b_interruptor_1 = Button(frame_baixo,width=13,text='bathroom switch',relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 7 bold'),background=co4,fg=co1)
b_interruptor_1.place(x=300,y=110)
b_interruptor_1 = Button(frame_baixo,width=13,text='Balcony switch',relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 7 bold'),background=co4,fg=co1)
b_interruptor_1.place(x=300,y=140)
b_interruptor_1 = Button(frame_baixo,width=13,text='Kitchen switch',relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 7 bold'),background=co4,fg=co1)
b_interruptor_1.place(x=300,y=170)

janela.mainloop()