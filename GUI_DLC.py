import tkinter as tk
from tkinter import colorchooser

def on_button_click():
    # Hier kannst du die Logik einfügen, die beim Klick auf den Button ausgeführt werden soll
    pass

def change_bg_color():
    color_code = colorchooser.askcolor(title="Hintergrundfarbe auswählen")[1]
    if color_code:
        root.configure(bg=color_code)
        update_color_label(color_code)

def change_text_color():
    color_code = colorchooser.askcolor(title="Textfarbe auswählen")[1]
    if color_code:
        label.config(fg=color_code)

def change_bg_color_palette():
    color_code = colorchooser.askcolor(title="Hintergrundfarbe auswählen", color=("#FF0000", "#00FF00", "#0000FF"))[1]
    if color_code:
        root.configure(bg=color_code)
        update_color_label(color_code)

def update_color_label(color_code):
    color_label.config(text=f"Ausgewählte Farbe: {color_code}")

def save_color():
    with open("selected_color.txt", "w") as file:
        file.write(color_label.cget("text").split(": ")[1])

def create_gui():
    global root, color_label, label
    root = tk.Tk()

    # Variablen für das Fenster und den Hintergrund
    window_width = 400
    window_height = 300
    window_bg_color = "lightgray"
    window_shadow_color = "gray"
    window_shadow_offset = 8

    # Variablen für die Farben der Widgets
    button_bg_color = "lightblue"
    button_text_color = "black"
    button_highlight_color = "yellow"

    # Fenstergröße festlegen
    root.geometry(f"{window_width}x{window_height}")

    # Fenster-Hintergrundfarbe setzen
    root.configure(bg=window_bg_color)

    # Fensterschatten (durch Frame mit grauer Hintergrundfarbe und entsprechender Position)
    shadow_frame = tk.Frame(root, bg=window_shadow_color)
    shadow_frame.place(x=window_shadow_offset, y=window_shadow_offset, relwidth=1, relheight=1)

    root.title("Farbauswahl-Anwendung")

    # Farblayout-Label
    color_label = tk.Label(root, text="Ausgewählte Farbe: ", font=("Arial", 14))
    color_label.pack(pady=5)

    # Erstelle die Widgets
    label = tk.Label(root, text="Hallo, willkommen zur GUI!", font=("Arial", 16), fg=button_text_color)
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    button = tk.Button(root, text="Klick mich!", command=on_button_click, bg=button_bg_color, fg=button_text_color, activebackground=button_highlight_color)
    button.pack(pady=15)

    # Farbe ändern-Button
    change_color_button = tk.Button(root, text="Farbe ändern", command=change_bg_color, bg=button_bg_color, fg=button_text_color, activebackground=button_highlight_color)
    change_color_button.pack(pady=5)

    # Textfarbe ändern-Button
    change_text_color_button = tk.Button(root, text="Textfarbe ändern", command=change_text_color, bg=button_bg_color, fg=button_text_color, activebackground=button_highlight_color)
    change_text_color_button.pack(pady=5)

    # Farbpalette für Hintergrundfarbe-Button
    change_bg_color_palette_button = tk.Button(root, text="Farbe aus Palette ändern", command=change_bg_color_palette, bg=button_bg_color, fg=button_text_color, activebackground=button_highlight_color)
    change_bg_color_palette_button.pack(pady=5)

    # Farbe speichern-Button
    save_color_button = tk.Button(root, text="Farbe speichern", command=save_color, bg=button_bg_color, fg=button_text_color, activebackground=button_highlight_color)
    save_color_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
