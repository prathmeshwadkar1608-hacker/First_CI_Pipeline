def sum_of_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


if __name__ == "__main__":
    numbers = list(map(int, input(
        "Enter numbers separated by spaces: "
    ).split()))

    print("Sum:", sum_of_list(numbers))