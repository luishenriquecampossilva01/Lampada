from tkinter import *

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
janela.mainloop()