"""
Ukol 1: Prvni GUI - zakladni widgety
=========================================================
Vytvorte jednoduche okno a postupne ho rozsirte o ruzne widgety
z knihovny ttk. Widgety umistete pomoci pack().
"""

from tkinter import Tk, Listbox
from tkinter import ttk

# TODO 1: vytvorte hlavni okno (Tk), nastavte titulek a velikost okna
window = Tk()
window.title("Ukol_1")
window.geometry("400x300")

# TODO 2: vytvorte Label s textem "Hello world!"
label = ttk.Label(window, text="Hello world!")
label.pack()


# TODO 3: vytvorte Entry o sirce 25 znaku
entry = ttk.Entry(window, width=20)
entry.pack()
# TODO 4: vytvorte Combobox se 3 polozkami podle vlastniho vyberu
combobox=ttk.Combobox(window,width=20, values=("Ukol 1", "Ukol 2","Ukol 3"))
combobox.pack()
# TODO 5: vytvorte Checkbutton s textem "Zaskrtni me"
button = ttk.Button(window, text="Zaskrtni me")
button.pack()

# TODO 6: vytvorte Radiobutton s textem "Vyber me"
radiobutton=ttk.Radiobutton(window,text="Vyber mě!")
radiobutton.pack()

# TODO 7: vytvorte Listbox (pozor, v ttk neexistuje - pouzijte verzi
#  z tkinter) a vlozte do nej 3 polozky pomoci .insert()
listbox=Listbox(window, height=5, width=50)
listbox.insert(0, "Ukol 1")
listbox.insert(1, "Ukol 2")
listbox.insert(2, "Ukol 3")
listbox.pack()
# TODO 8: vytvorte funkci close_window(), ktera zavre okno
#  a tlacitko s textem "Zavřít", ktery ji zavola
def close_window():
    window.destroy()
button_close=ttk.Button(window, text="Close window", command=close_window)
button_close.pack()

# spusteni GUI
window.mainloop()
