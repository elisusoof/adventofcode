import re

def change(word, sequence):
    if word == "one":
        sequence = sequence.replace(word, "1")
    if word == "two":
        sequence = sequence.replace(word, "2")
    if word == "three":
        sequence = sequence.replace(word, "3")
    if word == "four":
        sequence = sequence.replace(word, "4")
    if word == "five":
        sequence = sequence.replace(word, "5")
    if word == "six":
        sequence = sequence.replace(word, "6")
    if word == "seven":
        sequence = sequence.replace(word, "7")
    if word == "eight":
        sequence = sequence.replace(word, "8")
    if word == "nine":
        sequence = sequence.replace(word, "9")
    return sequence

def main():
    nums = []
    numbers_as_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open("aoc1input.txt", "r") as file:
        for line in file:
            print(line)
            numbers = (''.join(re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)))
            print(numbers)

            for number in numbers_as_string:
                numbers = change(number,numbers)
            print(numbers)

            concated_numbers = [letter for letter in numbers]

            num = int(f"{concated_numbers[0]}{concated_numbers[-1]}")
            nums.append(num)

    return sum(nums)

if __name__ == "__main__":
    print(main())


