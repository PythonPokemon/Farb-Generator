import tkinter as tk
from tkinter import colorchooser

def save_palette():
    with open("custom_palette.txt", "w") as file:
        for color_code in color_list:
            file.write(color_code + "\n")

def add_color():
    color_code = colorchooser.askcolor(title="Farbe zur Palette hinzufügen")[1]
    if color_code:
        color_list.append(color_code)
        update_palette()

def update_palette():
    for widget in color_frame.winfo_children():
        widget.destroy()

    for color_code in color_list:
        relief_func = selected_effect.get()
        shadow = selected_shadow.get()
        color_box = tk.Label(color_frame, bg=color_code, width=10, height=2, relief=relief_func)
        if shadow:
            color_box.configure(borderwidth=3, highlightthickness=4, highlightbackground=shadow)
        color_box.pack(side=tk.LEFT, padx=5, pady=5)
        color_box.bind("<Button-1>", lambda event, code=color_code: apply_color_scheme(code))

def apply_color_scheme(bg_color):
    root.configure(bg=bg_color)
    label.config(fg=get_text_color(bg_color))

def get_text_color(bg_color):
    r, g, b = tuple(int(bg_color[i:i+2], 16) for i in (1, 3, 5))
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return "black" if luminance > 0.5 else "white"

def flat_effect():
    selected_effect.set("flat")
    update_palette()

def raised_effect():
    selected_effect.set("raised")
    update_palette()

def sunken_effect():
    selected_effect.set("sunken")
    update_palette()

def toggle_shadow():
    update_palette()

def create_palette_generator():
    global color_list, color_frame, root, label, selected_effect, selected_shadow

    color_list = []

    root = tk.Tk()
    root.title("Farbpaletten-Generator")
    root.geometry("400x300")

    label = tk.Label(root, text="Hallo, willkommen zur GUI!", font=("Arial", 16))
    label.pack(pady=10)

    add_color_button = tk.Button(root, text="Farbe hinzufügen", command=add_color)
    add_color_button.pack(pady=10)

    save_palette_button = tk.Button(root, text="Palette speichern", command=save_palette)
    save_palette_button.pack(pady=5)

    selected_effect = tk.StringVar(root, "flat")  # Standard-Effekt ist "flat"
    selected_shadow = tk.StringVar(root, "")  # Standard-Schatten ist deaktiviert

    effect_frame = tk.Frame(root)
    effect_frame.pack(pady=5)

    flat_radio = tk.Radiobutton(effect_frame, text="Flat", variable=selected_effect, value="flat", command=flat_effect)
    flat_radio.pack(side=tk.LEFT, padx=5)

    raised_radio = tk.Radiobutton(effect_frame, text="Raised", variable=selected_effect, value="raised", command=raised_effect)
    raised_radio.pack(side=tk.LEFT, padx=5)

    sunken_radio = tk.Radiobutton(effect_frame, text="Sunken", variable=selected_effect, value="sunken", command=sunken_effect)
    sunken_radio.pack(side=tk.LEFT, padx=5)

    shadow_checkbox = tk.Checkbutton(effect_frame, text="Schatten", variable=selected_shadow, onvalue="gray", offvalue="", command=toggle_shadow)
    shadow_checkbox.pack(side=tk.LEFT, padx=5)

    color_frame = tk.Frame(root)
    color_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # Farbe aus der Palette auswählen
    root.bind("<Key>", lambda event: apply_color_scheme(color_list[int(event.char) - 1]) if event.char.isdigit() and int(event.char) <= len(color_list) else None)

    root.mainloop()

if __name__ == "__main__":
    create_palette_generator()
