import re

def change(word, sequence, ints_as_strings):
    for int_string in ints_as_strings:
        if word == int_string:
            sequence = sequence.replace(word, str(ints_as_strings.index(int_string)+1))
    return sequence

def main():
    nums = []
    numbers_as_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open("aoc1input.txt", "r") as file:
        for line in file:
            numbers = (''.join(re.findall(r"(?=(\d+|one|two|three|four|five|six|seven|eight|nine))", line)))

            for number in numbers_as_string:
                numbers = change(number,numbers, numbers_as_string)

            concated_numbers = [letter for letter in numbers]

            num = int(f"{concated_numbers[0]}{concated_numbers[-1]}")
            nums.append(num)

    return sum(nums)

if __name__ == "__main__":
    print(main())


