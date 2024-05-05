import tkinter as tk

def open_window():
    # Erstelle ein neues Fenster loloolololololololololololol
    window = tk.Tk()
    
    # Setze den Fenstertitel
    window.title("Mein Fenster")
    
    # Setze die Fenstergröße
    window.geometry("400x300")
    
    # Erstelle ein Label im Fenster
    label = tk.Label(window, text="Hallo Welt!")
    label.pack(pady=20)
    
    # Schleife, um das Fenster offen zu halten
    window.mainloop()

if __name__ == "__main__":
    open_window()
