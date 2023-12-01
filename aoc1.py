import re

def change(word, sequence, numbers_as_string):
    for number in numbers_as_string:
        if word == number:
            sequence = sequence.replace(word, str(numbers_as_string.index(number)+1))
    return sequence

def main():
    nums = []
    numbers_as_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open("aoc1input.txt", "r") as file:
        for line in file:
            numbers = (''.join(re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)))

            for number in numbers_as_string:
                numbers = change(number,numbers, numbers_as_string)

            concated_numbers = [letter for letter in numbers]

            num = int(f"{concated_numbers[0]}{concated_numbers[-1]}")
            nums.append(num)

    return sum(nums)

if __name__ == "__main__":
    print(main())


