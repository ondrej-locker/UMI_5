"""
Ukol 6: Kontrola rodneho cisla
=========================================================
Vytvorte GUI, ktere zkontroluje spravnost rodneho cisla (bez lomitka,
10 znaku: RRMMDD/XXXX).

Pravidla:
- pole musi byt vyplnene
- RC musi mit 10 znaku
- RC se sklada pouze z cislic
- RC musi byt delitelne 11
- hodnota mesice (znaky na pozici 2-3) musi byt 01-12 nebo 51-62
- hodnota dne (znaky na pozici 4-5) musi byt 01-31
"""

from tkinter import Tk
from tkinter import ttk

window = Tk()
window.title("Kontrola rodneho cisla")
window.geometry("600x300")

style=ttk.Style()
style.configure("Waring.Label",foreground="red")

label=ttk.Label(window,text="Rodné číslo:",font=("Arial", 12, "bold"))
label.place(x=50,y=20)
label_wariing=ttk.Label(window,text="Zadej rodné číslo bez lomítka!!!",font=("Arial", 8, "bold"),style="Waring.Label")
label_wariing.place(x=50,y=80)

entry = ttk.Entry(window, width=30)
entry.place(x=50,y=50)

def overeni():
    znak=""
    rodne_cislo=list(entry.get())
    for x in rodne_cislo:

        if not (x.isdigit()):
            znak += str(x)
            label_wariing.configure(text="Neplatný znak: " + str(znak))
            label_wariing.place(x=50, y=80)

    if len(rodne_cislo) == 0:
        label_wariing.configure(text="Zadej rodne cislo")
        label_wariing.place(x=50, y=80)

    elif len(rodne_cislo) != 10:
        label_wariing.configure(text="Zkontrolujte rodne cislo špatný počet")
        label_wariing.place(x=50, y=80)

    elif int(entry.get()) % 11 != 0:
        label_wariing.configure(text="Zkontrolujte rodné číslo neni dělitelné 11")
        label_wariing.place(x=50,y=80)

    elif not int(entry.get()[2:4]) in range(1,13) and not int(entry.get()[2:4]) in range(51,63):
        label_wariing.configure(text="Nesprávné rodné číslo měsíc")
        label_wariing.place(x=50,y=80)

    elif not int(entry.get()[4:6]) in range(1,32):
            label_wariing.configure(text="Nesprávné rodné číslo den")
            label_wariing.place(x=50, y=80)
    else:
        label_wariing.configure(text="Rodné číslo je správné")
        label_wariing.place(x=50, y=80)


buuton_vypnout=ttk.Button(window, text="Vypnout",command=window.destroy)
buuton_vypnout.place(x=50,y=120)

button_overit=ttk.Button(window, text="Ověřit rodné číslo",command=overeni)
button_overit.place(x=170,y=120)

window.mainloop()