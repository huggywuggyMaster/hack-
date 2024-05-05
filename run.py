import tkinter as tk

runV = True

def runIt():
    # Erstelle ein neues Tkinter-Fenster jrertzuiurewertzudebegzgezgzgegegezrgezrgzrzrewzrgzrgwzrgzrgzrgzrgrrgrgwzrgezererzvugrrugrghtghrgrzrgrrgwwzrg
    root = tk.Tk()

    # Setze den Fenstertitel
    root.title("Mein Fenster")

    # Setze die Größe des Fensters
    root.geometry("300x200")

    # Erstelle ein Label im Fenster
    label = tk.Label(root, text="Hallo Welt!")
    label.pack(pady=20)

    # Funktion, um das Fenster zu schließen
    def close_window():
        root.destroy()

    # Erstelle einen Button, um das Fenster zu schließen
    button = tk.Button(root, text="Schließen", command=close_window)
    button.pack()

    # Loop, um das Fenster offen zu halten
    root.mainloop()
