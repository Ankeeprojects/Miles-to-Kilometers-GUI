from tkinter import *

FONTE = ("Courier", 18, "bold")
CONSTANTE = 1.609344

window = Tk()
window.title("Miles to kilometers converter")
window.minsize(300,200)
window.config(padx=30, pady=30)

label1 = Label(text="Miles", font=FONTE)
label1.grid(column=2, row=0)
label1.config(padx=30)

label2 = Label(text="equals", font=FONTE)
label2.grid(column=0, row=1)
label2.config(padx=30)

label3 = Label(text="Km", font=FONTE)
label3.grid(column=2, row=1)
label3.config(padx=30)

label4 = Label(text="0", font=FONTE)
label4.grid(column=1, row=1)

entry = Entry()
entry.grid(column=1, row=0)

def calcular():
    texto = entry.get()
    label4["text"] = round(int(texto) * CONSTANTE, 2)

botao = Button(text="Calculate", font=FONTE, command=calcular)
botao.grid(column=1, row=2)

window.mainloop()
