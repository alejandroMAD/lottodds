def calculate_lottery_odds(numbers_drawn, total_numbers, bonus_numbers_drawn=0, total_bonus_numbers=0):
    """Calculates the odds of winning a lottery game with the specified parameters."""
    possible_combinations = 1
    for i in range(numbers_drawn):
        possible_combinations *= (total_numbers - i) / (i + 1)
    if bonus_numbers_drawn > 0 and total_bonus_numbers > 0:
        bonus_combinations = 1
        for i in range(bonus_numbers_drawn):
            bonus_combinations *= (total_bonus_numbers - i) / (i + 1)
        possible_combinations *= bonus_combinations
    odds = 1 / possible_combinations
    return odds


def format_lottery_odds(result):
    """Formats the odds of winning a lottery game as a string in the format 'The odds are 1 in x'."""
    if result >= 1:
        return "The odds of winning the specified lottery game are 1 in {:,}".format(int(round(1/result)))
    else:
        return "The odds of winning the specified lottery game are 1 in {:,}".format(int(round(1/result)))


# Test with the EuroMillions transnational lottery game configuration
result = calculate_lottery_odds(5, 50, 2, 12)
formatted_result = format_lottery_odds(result)
print(formatted_result)
