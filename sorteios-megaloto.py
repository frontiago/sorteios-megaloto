# Sorteios Megasena e Lotofácil 

from tkinter import *
from random import randint 

# Sortear MegaSena
def sortearMegasena():
    sorteados = set()

    while len(sorteados) < 6:
        numeros = randint(1, 60)
        sorteados.add(numeros)
        outputStrMegaSena.set(sorted(sorteados))

# Sortear LotoFacil
def sortearLotoFacil():
    sorteados = set()

    while len(sorteados) < 15:
        numeros = randint(1, 25)
        sorteados.add(numeros)
        outputStrLotoFacil.set(sorted(sorteados))

# Window 
window = Tk()
window.title("Sortear Megasena")
window.geometry("670x400")

# Megasena button  
buttonMegaSena = Button(window, 
    text = "Sortear MegaSena", 
    font = "Calibri 16", 
    fg = "#FFF",
    bg = "green",
    bd = 0,
    command = sortearMegasena
)
buttonMegaSena.pack(pady=10)

# Megasena numbers
outputStrMegaSena = StringVar()
outputLabelMegaSena = Label(window, 
    text = "Output", 
    font = ("Calibri 30"), 
    fg = "green", 
    textvariable = outputStrMegaSena
)
outputLabelMegaSena.pack(pady=20)

# Lotofacil button 
buttonLotofacil = Button(window, 
    text = "Sortear LotoFácil", 
    font = "Calibri 16", 
    fg = "#FFF",
    bg = "#a6368e",
    bd = 0,
    command = sortearLotoFacil
)
buttonLotofacil.pack(pady=10)

# Lotofacil numbers 
outputStrLotoFacil = StringVar()
outputLabelLotoFacil = Label(window, 
    text = "Output", 
    font = ("Calibri 30"),
    fg = "#a6368e",
    textvariable = outputStrLotoFacil
)
outputLabelLotoFacil.pack(pady=20)

# Run App
window.mainloop()

