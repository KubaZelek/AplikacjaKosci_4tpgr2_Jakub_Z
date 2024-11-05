import tkinter as tk
class Aplikacja:
    def __init__(self, root):
        self.tekst1 = tk.StringVar()
        self.tekst2 = tk.StringVar()
        
        
        self.label1 = tk.Label(root, text="Podaj liczbe")
        self.label1.grid(row=0, column=0)
        
         
        self.entry1 = tk.Entry(root, textvariable=self.tekst1, font=('none', 9, 'italic'))
        self.entry1.grid(row=0, column=1)
        
        self.btn1 = tk.Button(root, text="Przekaż liczbę", command=lambda: self.zmien_tekst(self.label3, self.tekst1, "Podana liczba:"))
        self.btn1.grid(row=0, column=2)
        
        self.label2 = tk.Label(root, text="Podaj haslo")
        self.label2.grid(row=1, column=0)
        
        self.entry2 = tk.Entry(root, textvariable=self.tekst2, show="*")
        self.entry2.grid(row=1, column=1)
        
        
        self.btn2 = tk.Button(root,text="Przekaz haslo", command=lambda: self.zmien_tekst(self.label4, self.tekst2, "Haslo to: "))
        self.btn2.grid(row=1, column=2)
        
        self.label3 = tk.Label(root, text="Zmien mnie!!!")
        self.label3.grid(row=2, column=1)
        
        
        self.label4 = tk.Label(root, text="Haslo to")
        self.label4.grid(row=3, column=1)
        
        
    def zmien_tekst(self, label, textvar, text):
        label.config(text=(str(text)+ str(textvar.get())))
root = tk.Tk()
root.title("Siema")
root.geometry("300x300")
app = Aplikacja(root)
root.mainloop()