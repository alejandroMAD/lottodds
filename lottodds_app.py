import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from labels_locale import labels
from lottery_game import LotteryGame
from numbers_drum import NumbersDrum
from odds_facts import odds_facts


class LottOddsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LottOdds")
        self.configure(bg="#152238")

        self.logo_image = ImageTk.PhotoImage(Image.open("images/lottodds_logo.png").resize((180, 40)))
        self.image_label = ttk.Label(self, image=self.logo_image, background="#152238")
        self.image_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.subtitle_label = ttk.Label(self,
                                        text=labels['subtitle_lbl']['ENG'], font=("Helvetica", 12),
                                        foreground="#c0c0c0", background="#152238")
        self.subtitle_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Create and place number spinners
        self.drum1 = NumbersDrum(self, "Drum 1", "images/drum1.png")
        self.drum2 = NumbersDrum(self, "Drum 2", "images/drum2.png", True)
        self.drum1.configure(bg="#203354")
        self.drum2.configure(bg="#203354")
        self.drum1.grid(row=2, column=0, padx=10, pady=10)
        self.drum2.grid(row=2, column=1, padx=10, pady=10)

        # Create calculate button and result labels
        self.calculate_button = ttk.Button(self, text=labels['calculate_btn']['ENG'],
                                           command=self.set_odds_result, style="My.TButton")
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Create result labels 
        self.result1_label = ttk.Label(self, text=labels['result1_lbl']['ENG'], font=("Helvetica", 16),
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
                    result2 = odds_fact['ENG']
                    break

            # Update result labels
            self.result1_label.config(text="{}".format(result1))
            self.result2_label.config(text="{}".format(result2))

            # If the input is invalid, no comparison of chances will be showed
            if odds == labels['wrong_config_lbl']['ENG']:
                self.result2_label.config(text="")
        except ZeroDivisionError as err:
            print("Incorrect lottery configuration input")
            print(err)
            self.result1_label.config(text=labels['wrong_config_lbl']['ENG'])


if __name__ == "__main__":
    app = LottOddsApp()
    app.wm_iconbitmap("images/lottodds.ico")

    # set the window dimensions
    width = 890
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
