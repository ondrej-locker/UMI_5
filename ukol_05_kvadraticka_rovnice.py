"""
Ukol 5: Vypocet kvadraticke rovnice
=========================================================
Vytvorte GUI pro vypocet korenu kvadraticke rovnice a*x^2 + b*x + c = 0.
Uzivatel zada koeficienty a, b, c a po stisknuti tlacitka "Spocitej"
se zobrazi vysledek zaokrouhleny na 2 desetinna mista. Pokud je
diskriminant zaporny, zobrazi se hlaska "Rovnice nema reseni".

Vsechny widgety umistete pomoci grid()
"""
import math
from tkinter import Tk
from tkinter import ttk

# TODO 1: vytvorte okno, nastavte titulek a velikost (cca 420x160)
window = Tk()
window.title("Kvadratická rovnice")
window.geometry("600x160")


# TODO 2: vytvorte objekt stylu a nadefinujte jeden styl
#  "Koeficient.TLabel" (napr. tucne pismo a vlastni barva textu),
#  ktery pak pouzijete pro vsechny 3 popisky a, b, c
style = ttk.Style()
style.configure("Koeficient_a.TLabel", foreground="red")
style.configure("Koeficient_b.TLabel", foreground="green")
style.configure("Koeficient_c.TLabel", foreground="blue")

# TODO 3: vytvorte popisky pro "a:", "b:" a "c:", vsem nastavte
#  style="Koeficient.TLabel" a umistete je
label_a = ttk.Label(window, text="a:",font=("Arial", 12, "bold"),style="Koeficient_a.TLabel")
label_a.place(x=10,y=10)
label_b = ttk.Label(window, text="b:",font=("Arial", 12, "bold"),style="Koeficient_b.TLabel")
label_b.place(x=10,y=50)
label_c = ttk.Label(window, text="c:",font=("Arial", 12, "bold"),style="Koeficient_c.TLabel")
label_c.place(x=10,y=90)

# TODO 4: vytvorte 3 Entry (pro a, b, c) o sirce 10 znaku a
#  umistete je
entry_a = ttk.Entry(window, width=10,font=("Arial", 12, "bold"))
entry_a.place(x=80,y=10)
entry_b = ttk.Entry(window, width=10,font=("Arial", 12, "bold"))
entry_b.place(x=80,y=50)
entry_c = ttk.Entry(window, width=10,font=("Arial", 12, "bold"))
entry_c.place(x=80,y=90)


# TODO 5: napiste funkci calculate(), ktera:
#  - precte a prevede na float hodnoty z entry_a, entry_b, entry_c
#  - spocita diskriminant D = b^2 - 4*a*c
#  - pokud D >= 0, spocita oba koreny (zaokrouhlene na 2 des. mista)
#  a zobrazi je v label_vysledek
#  - pokud D < 0, zobrazi v label_vysledek text "Rovnice nema reseni"
def calculate():
    a=float(entry_a.get())
    b=float(entry_b.get())
    c=float(entry_c.get())
    d = b**2 - (4 * a * c)
    if d >= 0:
        x_1=(-(b)+math.sqrt(d))/(2*a)
        x_2=(-(b)-math.sqrt(d))/(2*a)
        vysl=[x_1,x_2]
        label_vysledek.configure(text =" Výsledek je: " +str(vysl),font=("Arial", 20, "bold"))
        label_vysledek.place(x=200,y=45)
    elif d < 0:
        label_vysledek.configure(text="Rovnive nemá řešení v R",font=("Arial", 20, "bold"))
        label_vysledek.place(x=200,y=45)


# TODO 6: vytvorte tlacitko s textem "Spocitej", ktery zavola
#  calculate(), widget umistete
button_vysledek = ttk.Button(window,text="Spocitej",command =calculate)
button_vysledek.place(x=200,y=120)
button_vypnout = ttk.Button(window,text="Vypnout", command =window.destroy)
button_vypnout.place(x=350,y=120)

# TODO 7: vytvorte prazdny label_vysledek pro zobrazeni vysledku,
#  widget umistete
label_vysledek = ttk.Label(text="Zde se zobrazí výsledek", font=("Arial", 20, "bold"))
label_vysledek.place(x=200,y=45)

window.mainloop()
