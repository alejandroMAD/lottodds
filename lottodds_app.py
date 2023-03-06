import tkinter as tk
from tkinter import ttk, END
from PIL import Image, ImageTk

from odds_facts import odds_facts
from labels_locale import labels


class LotteryGame:
    def __init__(self, numbers_drawn, total_numbers, bonus_numbers_drawn=0, total_bonus_numbers=0):
        self.numbers_drawn = numbers_drawn
        self.total_numbers = total_numbers
        self.bonus_numbers_drawn = bonus_numbers_drawn
        self.total_bonus_numbers = total_bonus_numbers

    def calculate_odds(self):
        """Calculates the odds of winning the lottery game for this LotteryGame configuration"""
        possible_combinations = 1
        for i in range(self.numbers_drawn):
            possible_combinations *= (self.total_numbers - i) / (i + 1)
        if self.bonus_numbers_drawn > 0 and self.total_bonus_numbers > 0:
            bonus_combinations = 1
            for i in range(self.bonus_numbers_drawn):
                bonus_combinations *= (self.total_bonus_numbers - i) / (i + 1)
            possible_combinations *= bonus_combinations
        odds = 1 / possible_combinations
        return odds

    def format_odds(self):
        """Formats the odds of winning the lottery game as a string in the format 'The odds are 1 in x'."""
        result = self.calculate_odds()
        if result >= 1:
            return labels['wrong_config_lbl']['SPA']
        else:
            return labels['formatted_odds_lbl']['SPA'].format(int(round(1/result)))


class NumbersDrum(tk.Frame):
    def __init__(self, master, label_text, image_path, is_bonus_drum=False):
        super().__init__(master)

        # Load image and create image label
        self.image = ImageTk.PhotoImage(Image.open(image_path).resize((80, 80)))
        self.image_label = ttk.Label(self, image=self.image, background="#203354")

        # Create labels and spinners
        drum_text = labels['bonus_drum_lbl']['SPA'] if is_bonus_drum else labels['regular_drum_lbl']['SPA']
        self.drum_label = ttk.Label(self, text=drum_text, font=("Helvetica", 11),
                                    foreground="#c0c0c0", background="#203354")
        self.numbers_drawn_label = ttk.Label(self, text=labels['draws_lbl']['SPA'],
                                             foreground="#c0c0c0", background="#203354")
        self.numbers_drawn_spinner = ttk.Spinbox(self, from_=0, to=100, width=8)
        self.max_number_label = ttk.Label(self, text=labels['max_num_lbl']['SPA'],
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
            self.checkbox = ttk.Checkbutton(self, text=labels['bonus_disable_cbox']['SPA'],
                                            variable=self.disable_spinner, style="My.TCheckbutton", width=30)
            self.checkbox.grid(row=3, column=1, columnspan=2, padx=5, pady=10, sticky="w")
            self.disable_spinner.trace_add('write', self.toggle_spinboxes)
        else:
            self.main_drum_label = ttk.Label(self, text=labels['main_drum_lbl']['SPA'], foreground="#c0c0c0",
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
            return (
                int(self.numbers_drawn_spinner.get()),
                int(self.max_number_spinner.get())
            )


class LottOddsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Spinner App")
        self.configure(bg="#152238")

        self.logo_image = ImageTk.PhotoImage(Image.open("lottodss_logo.png").resize((180, 40)))
        self.image_label = ttk.Label(self, image=self.logo_image, background="#152238")
        self.image_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.subtitle_label = ttk.Label(self,
                                        text=labels['subtitle_lbl']['SPA'], font=("Helvetica", 12),
                                        foreground="#c0c0c0", background="#152238")
        self.subtitle_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Create and place number spinners
        self.drum1 = NumbersDrum(self, "Drum 1", "drum1.png")
        self.drum2 = NumbersDrum(self, "Drum 2", "drum2.png", True)
        self.drum1.configure(bg="#203354")
        self.drum2.configure(bg="#203354")
        self.drum1.grid(row=2, column=0, padx=10, pady=10)
        self.drum2.grid(row=2, column=1, padx=10, pady=10)

        # Create calculate button and result labels
        self.calculate_button = ttk.Button(self, text=labels['calculate_btn']['SPA'],
                                           command=self.set_odds_result, style="My.TButton")
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Create result labels 
        self.result1_label = ttk.Label(self, text=labels['result1_lbl']['SPA'], font=("Helvetica", 16),
                                       foreground="#c0c0c0", background="#152238")
        self.result1_label.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="w")
        self.result2_label = ttk.Label(self, text="", font=("Helvetica", 12), foreground="#c0c0c0",
                                       background="#152238")
        self.result2_label.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="w")

        # Create custom styles for the button and checkbutton
        style = ttk.Style()
        style.configure("My.TButton", font=('Arial', 12), background="#CCCCCA", foreground="#435524")
        style.configure("My.TCheckbutton", background="#203354", foreground="#c0c0c0")

    def set_odds_result(self):
        # Get values from drums spinners
        drum1_values = self.drum1.get_values()
        drum2_values = (0, 0) if self.drum2.disable_spinner.get() else self.drum2.get_values()

        # Instantiate LotteryGame with the selected values' configuration,
        # apply the odds calculation algorithm and retrieve a formatted result string
        try:
            lottery_game = LotteryGame(drum1_values[0], drum1_values[1], drum2_values[0], drum2_values[1])
            odds = lottery_game.format_odds()
            result1 = odds
            result2 = "Comparison of chances."
            odds_range = int(round(1/lottery_game.calculate_odds()))
            for range_, odds_fact in odds_facts.items():
                if range_[0] <= odds_range <= range_[1]:
                    result2 = odds_fact['SPA']
                    break

            # Update result labels
            self.result1_label.config(text="{}".format(result1))
            self.result2_label.config(text="{}".format(result2))
        except ZeroDivisionError as err:
            print("Incorrect lottery configuration input")
            print(err)
            self.result1_label.config(text=labels['wrong_config_lbl']['SPA'])


if __name__ == "__main__":
    app = LottOddsApp()

    # set the window dimensions
    width = 880
    height = 400

    # get the screen dimensions
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # calculate the coordinates for the center of the screen
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    # set the window geometry to center it on the screen
    app.geometry("%dx%d+%d+%d" % (width, height, x, y))

    app.mainloop()
