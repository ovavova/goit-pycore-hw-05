import re


def generator_numbers(text: str):
    pattern = r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?"  # Pattern for real numbers

    for match in re.finditer(pattern, text):  # ItarationIterating via object of patterns
        yield float(match.group())


def sum_profit(text: str, func: callable):
    sum_profit = 0
    for num in generator_numbers(text):  # Calling iterator fucntion
        sum_profit += num  # Adding next real number
    return sum_profit


# Test
if __name__ == "__main__":

    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

