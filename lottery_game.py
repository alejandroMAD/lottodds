
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
            return labels['wrong_config_lbl']['ENG']
        else:
            return labels['formatted_odds_lbl']['ENG'].format(int(round(1/result)))
