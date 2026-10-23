"""Program 29: Check for an Armstrong number."""


def is_armstrong(number):
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == number


if __name__ == "__main__":
    number = int(input("Enter a non-negative integer: "))

    if is_armstrong(number):
        print("Armstrong number")
    else:
        print("Not an Armstrong number")