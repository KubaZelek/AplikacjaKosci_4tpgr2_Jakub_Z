import tkinter as tk
n = 23

class Aplikacja:
    def __init__(self, root):
        self.tekst1 = tk.StringVar()
        self.tekst2 = tk.StringVar()
        
        
        self.label1 = tk.Label(root, text="Podaj imię i nazwisko")
        self.label1.grid(row=n, column=n)
        
         
        self.entry1 = tk.Entry(root, textvariable=self.tekst1, font=('none', 9, 'italic'))
        self.entry1.grid(row=n, column=n+1)
        
        
        self.label2 = tk.Label(root, text="Podaj nazwę klasy")
        self.label2.grid(row=n+1, column=n)
        
        self.entry2 = tk.Entry(root, textvariable=self.tekst2, show="*")
        self.entry2.grid(row=n+1, column=n+1)

        self.btn1 = tk.Button(root, text="Podaj dane",font=('Times new Roman', 10, 'italic'), background="gray" ,command=lambda: self.zmien_tekst1(self.label1, self.tekst1))
        self.btn1.grid(row=n, column=n+2)
        
        self.btn2 = tk.Button(root,text="Podaj klasę", font=('Times new Roman', 10, 'italic'), background="orange" ,command=lambda: self.zmien_tekst2(self.label2, self.tekst2))
        self.btn2.grid(row=n+1, column=n+2)

    def zmien_tekst1(self, label, textvar):
        label.config(text=("Cześć "+ str(textvar.get())))
    def zmien_tekst2(self, label, textvar):
        label.config(text=("Jesteś z klasy "+ str(textvar.get())))



root = tk.Tk()
root.title("ZSEIT")
root.configure(bg='lightblue')
root.geometry(f"{n*30}x{n*30}")
app = Aplikacja(root)
root.mainloop()