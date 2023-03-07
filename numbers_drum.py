import tkinter as tk
from tkinter import ttk, END, messagebox
from PIL import Image, ImageTk

from labels_locale import labels


class NumbersDrum(tk.Frame):
    def __init__(self, master, label_text, image_path, is_bonus_drum=False):
        super().__init__(master)

        # Load image and create image label
        self.image = ImageTk.PhotoImage(Image.open(image_path).resize((80, 80)))
        self.image_label = ttk.Label(self, image=self.image, background="#203354")

        # Create labels and spinners
        drum_text = labels['bonus_drum_lbl']['ENG'] if is_bonus_drum else labels['regular_drum_lbl']['ENG']
        self.drum_label = ttk.Label(self, text=drum_text, font=("Helvetica", 11),
                                    foreground="#c0c0c0", background="#203354")
        self.numbers_drawn_label = ttk.Label(self, text=labels['draws_lbl']['ENG'],
                                             foreground="#c0c0c0", background="#203354")
        self.numbers_drawn_spinner = ttk.Spinbox(self, from_=0, to=100, width=8)
        self.max_number_label = ttk.Label(self, text=labels['max_num_lbl']['ENG'],
                                          foreground="#c0c0c0", background="#203354")
        self.max_number_spinner = ttk.Spinbox(self, from_=0, to=10000, width=8)

        self.image_label.grid(row=0, column=0, columnspan=1, rowspan=4, padx=10, pady=10)
        self.drum_label.grid(row=0, column=1, columnspan=1, sticky="w", padx=10, pady=5)
        self.numbers_drawn_label.grid(row=1, column=1, sticky="e", padx=5, pady=5)
        self.numbers_drawn_spinner.grid(row=1, column=2, sticky="w", padx=5, pady=5)
        self.max_number_label.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        self.max_number_spinner.grid(row=2, column=2, sticky="w", padx=5, pady=5)

        self.disable_spinner = tk.BooleanVar()

        # Create checkbox to enable/disable spinners if it is a bonus drum
        if is_bonus_drum:
            self.disable_spinner.set(False)
            self.checkbox = ttk.Checkbutton(self, text=labels['bonus_disable_cbox']['ENG'],
                                            variable=self.disable_spinner, style="My.TCheckbutton", width=30)
            self.checkbox.grid(row=3, column=1, columnspan=2, padx=5, pady=10, sticky="w")
            self.disable_spinner.trace_add('write', self.toggle_spinboxes)
        else:
            self.main_drum_label = ttk.Label(self, text=labels['main_drum_lbl']['ENG'], foreground="#c0c0c0",
                                             background="#203354", width=30)
            self.main_drum_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="w")

    def toggle_spinboxes(self, *args):
        if self.disable_spinner.get():
            self.max_number_spinner.configure(state="disabled")
            self.numbers_drawn_spinner.configure(state="disabled")
        else:
            self.max_number_spinner.configure(state="normal")
            self.numbers_drawn_spinner.configure(state="normal")

    def get_values(self):
        if self.max_number_spinner.get() == "":
            self.max_number_spinner.delete(0, END)
            self.max_number_spinner.insert(0, "0")
        if self.numbers_drawn_spinner.get() == "":
            self.numbers_drawn_spinner.delete(0, END)
            self.numbers_drawn_spinner.insert(0, "0")

        if self.disable_spinner.get():
            return 0, 0
        else:
            try:
                numbers_drawn = int(self.numbers_drawn_spinner.get())
                max_number = int(self.max_number_spinner.get())
                return numbers_drawn, max_number
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers.")
                return 0, 0
