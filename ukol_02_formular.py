"""
Ukol 2: Jednoduchy formular
=========================================================
Vytvorte GUI s jednim widgetem Label, jednim Entry a jednim Button.
Po stisknuti tlacitka se v popisku zobrazi text napsany do pole ve
formatu "Napsal jsi: text_z_entry". Pokud uzivatel nic nenapise,
zobrazi se "Nic jsi nenapsal". Widgety umistete pomoci grid()
(kazdy do vlastniho radku, sloupec 0).
"""

from tkinter import Tk
from tkinter import ttk

window = Tk()
window.title("GUI")
window.geometry("300x120")

# TODO 1: vytvorte Label s textem "Tady se zobrazi tvuj napsany
#  text" a umistete ho
label = ttk.Label(window, text="Tady se zobrazí tvůj napsaný text")
label.place(x=60, y=30)

# TODO 2: vytvorte Entry o sirce 30 znaku a umistete ho
entry = ttk.Entry(window, width=30)
entry.place(x=60, y=60)

# TODO 3: napiste funkci zobraz_text(), ktera:
#  - precte text z entry
#  - pokud je prazdny, nastavi labelu text "Nic jsi nenapsal"
#  - jinak nastavi labelu text "Napsal jsi: " + precteny text
def zobraz_text():
    text = entry.get()
    if not text:
        label.configure(text="Nic jsi nenapsal")
    else:
        label.configure(text="Napsal jsi: "+text)

# TODO 4: vytvorte Button s textem "Zobraz text", ktery po
#  stisknuti zavola funkci zobraz_text, widget umistete
button = ttk.Button(window, text="Zobraz text", command=zobraz_text)
button.place(x=60, y=90)

# spusteni GUI
window.mainloop()