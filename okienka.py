import tkinter as tk
from tkinter import font
n = 23
class Aplikacja:
    def __init__(self, root):
        custom_font = font.Font(family="Times New Roman", size=24, weight="bold")
        custom_font2 = font.Font(family="Times New Roman", size=18, weight="normal")
        
        self.tekst = tk.StringVar()
        self.tekst.set("imie")
        
        self.label1 = tk.Label(root, textvariable=self.tekst, background="green",font=custom_font )
        self.label1.grid(row=n, column=n)
        
        self.b1 = tk.Button(root, text="Przycisk nr 1", command=self.zmien_tekst, background="brown", font=custom_font2)
        self.b1.grid(row=n, column=n+1)
        
        self.label2 = tk.Label(root, text="nazwisko", background="#00BFFF", font=custom_font)
        self.label2.grid(row=1, column=0)
        
        self.b2 = tk.Button(root, text="Przycisk nr 2",font=custom_font2, background="#ffff00" ,command=lambda: self.zmien_tekst_w(self.label2))
        self.b2.grid(row=1, column=1) 

    def zmien_tekst(self):
        self.tekst.set("Jakub")
        
    def zmien_tekst_w(self, label):
        label.config(text="Zelechowski")

root = tk.Tk()
root.title("ZSEIT")
root.geometry(f"{n*10}x{n*10}")
# root.iconbitmap('./ikonka.png')

app = Aplikacja(root)

# Uruchamiamy pętlę główną
root.mainloop()
