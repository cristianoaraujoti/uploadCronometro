from tkinter import *
import tkinter

#Configurando janela
janela = Tk()
janela.title('')
janela.geometry('300x180')
janela.configure(bg='Black')
janela.resizable(width=False, height=False)


#Cores
cor1 = '#0a0a0a' #black / preta
cor2 = '#fafcff' #white / branca
cor3 = '#21c25c' #green / verde
cor4 = '#eb463b' #rede / vermelha
cor5 = '#dedcdc' #gray / cinzenta
cor6 = '#3080f0' #blue / azul

#Definindo vaviaveis globais

global tempo
global rodar
global contador
global limitador



tempo = "00:00:00"
rodar = False
contador = -5


#função iniciar
def iniciar():
    global tempo
    global contador
    global limitador

    limitador = 59

    if rodar:
        #Antes do cronometro começar
        if contador <=-1:
            inicio = 'Começando em ' + str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'
        
        # Rodando o  cronometro 
        else:
            label_tempo['font'] = 'Times 50 bold'
            
            temporario = str(tempo)
            h,m,s = map(int, temporario.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)

            if (s>=limitador):
                contador = 0
                m+=1
            
            s = str(0)+ str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            # Atualizando os valores atuais
            temporario = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])

            label_tempo['text'] = temporario

            tempo = temporario


        label_tempo.after(1000, iniciar)
        contador +=1

#função para dar inicio
def start():
    global rodar
    rodar = True
    iniciar()

# função pausar
def pausar():
    global rodar
    rodar = False


#função reiniciar
def reiniciar():
    global contador
    global tempo

    #Reiniciando o contador
    contador = 0

    #Reiniciando tempo
    tempo = "00:00:00"
    label_tempo['text'] = tempo




#Criando Labls

label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=('Arial 50 bold'), bg=cor1, fg=cor6)
label_tempo.place(x=20, y=30)

#Criando Botões
botao_iniciar = Button(janela, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 10 bold'), relief='raised', overrelief='ridge', command=start)
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 10 bold'), relief='raised', overrelief='ridge', command=pausar)
botao_pausar.place(x=110, y=130)

botao_reiniciar = Button(janela, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 10 bold'), relief='raised', overrelief='ridge', command=reiniciar)
botao_reiniciar.place(x=200, y=130)



janela.mainloop()