"""
Ukol 3: Styly a pristupnost
=========================================================
Vytvorte GUI se 3 stavovymi "kontrolkami" (OK / Pozor / Chyba), ktere
pouzivaji barevne odliseni pomoci ttk.Style(). Podle zasad navrhu UI
pro barvoslepe uzivatele (viz prednaska) KAZDE barevne znaceni doplnte
i textem nebo symbolem - nespolehejte se pouze na barvu!
"""

from tkinter import Tk
from tkinter import ttk


window = Tk()
window.title("Stavove kontrolky")
window.geometry("300x180")

# TODO 1: vytvorte objekt stylu - style = ttk.Style()
style = ttk.Style()

# TODO 2: nadefinujte 3 styly pro Label pomoci style.configure():
#  - "OK.TLabel"      -> zelene pozadi ("green"), bily text
#  - "Warning.TLabel" -> oranzove pozadi ("orange"), cerny text
#  - "Error.TLabel"   -> cervene pozadi ("red"), bily text
#  u vsech nastavte i font a padding podle vlastniho vyberu
style.configure("G.Label", background="green", foreground="white")
style.configure("O.Label", background="orange", foreground="black")
style.configure("R.Label", background="red", foreground="white")

# TODO 3: vytvorte 3 Label s prislusnym stylema textem, ktery
#  KROME barvy obsahuje i popis stavu, napr.: "OK (vse v poradku)",
#  "POZOR (zkontrolujte)", "CHYBA (nefunguje)", umistete je pomoci pack()
label_ok =ttk.Label(window, text="OK (vse v poradku)", style="G.Label")
label_ok.place(x=10, y=30)
label_warning =ttk.Label(window, text="POZOR (zkontrolujte)", style="O.Label")
label_warning.place(x=10, y=60)
label_error = ttk.Label(window, text="CHYBA (nefunguje)", style="R.Label")
label_error.place(x=10, y=90)

window.mainloop()
