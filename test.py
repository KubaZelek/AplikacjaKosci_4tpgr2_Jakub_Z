import tkinter as tk
from tkinter import StringVar
from PIL import Image, ImageTk

class Aplikacja:
    def __init__(self, root):
        self.label1 = tk.Label(root, text="Ankieta zadowolenia klienta", font=('Times New Roman', 18, 'bold'), fg='blue')
        self.label1.grid(row=0, column=0, columnspan=3, pady=10)

        self.textvar1 = StringVar()
        self.textvar2 = StringVar()
        self.textvar1.set("Imię i nazwisko")
        self.entrylabel = tk.Label(root, text="Imię i nazwisko: ")
        self.entry1 = tk.Entry(root, textvariable=self.textvar1)
        self.entrylabel.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry1.grid(row=1, column=1, padx=10, pady=5)

        self.entrylabel2 = tk.Label(root, text="Adres email: ")
        self.entry2 = tk.Entry(root, textvariable=self.textvar2)
        self.entrylabel2.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry2.grid(row=2, column=1, padx=10, pady=5)

        self.radioVar = StringVar()
        self.r1 = tk.Radiobutton(root, text="Mężczyzna", variable=self.radioVar, value="mezczyzna")
        self.r2 = tk.Radiobutton(root, text="Kobieta", variable=self.radioVar, value="kobieta")
        self.r3 = tk.Radiobutton(root, text="Inne", variable=self.radioVar, value="inne")
        self.radioVar.set("mezczyzna")
        self.r1.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.r2.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.r3.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        self.labelWyksztalenie = tk.Label(root, text="Jakie masz wykształcenie?")
        self.opcje = ["podstawowe", "zawodowe", "średnie", "wyższe"]
        self.selected_option = tk.StringVar()
        self.selected_option.set(self.opcje[0])
        self.dropdown = tk.OptionMenu(root, self.selected_option, *self.opcje)
        self.labelWyksztalenie.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.dropdown.grid(row=4, column=1, padx=10, pady=5)


        self.labelOcena = tk.Label(root, text="Jak oceniasz usługi? 1-6")
        self.spinbox = tk.Spinbox(root, from_=1, to=6)
        self.labelOcena.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.spinbox.grid(row=5, column=1, padx=10, pady=5)

      
        self.saveBtn = tk.Button(root, text="Zapisz", background='red', 
                                 command=lambda: self.pokaz_dane(self.textvar1.get(), self.radioVar.get(), self.selected_option.get(), self.spinbox.get()))
        self.saveBtn.grid(row=6, column=0, columnspan=3, pady=20)

     
        self.labelKoncowy = tk.Label(root)
        self.labelKoncowy.grid(row=7, column=0, columnspan=3, pady=10)

        
        self.load_image(root)

    def load_image(self, root):
        image_path = "klient.jpg"  
        img = Image.open(image_path) 
        img = img.resize((200, 200))  
        img_tk = ImageTk.PhotoImage(img)

      
        self.image_label = tk.Label(root, image=img_tk)
        self.image_label.image = img_tk 
        self.image_label.grid(row=8, column=0, columnspan=3, pady=10)

    def pokaz_dane(self, imie, plec, wyksztalcenie, ocena):
        self.labelKoncowy.config(text=f"Imię: {imie}, Płeć: {plec}, Wykształcenie: {wyksztalcenie}, Ocena: {ocena}")

root = tk.Tk()
root.geometry("500x600")
root.config(bg='#D4D9DB')
root.title("Zapisz Ankietę")

app = Aplikacja(root)

root.mainloop()
