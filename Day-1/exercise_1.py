# ADVENT OF CODE 2023

# --- Day 1: Trebuchet?! ---
# --- PART 1 ---

def calibration(text_document):
    '''
    Returns sum of first and last integers from each line in text_document.
    '''
    total_sum = 0

    for line in text_document:
        for char in line:
            if char.isdigit():
                first_digit = int(char)
                break
        for char in reversed(line):
            if char.isdigit():
                last_digit = int(char)
                break
        calibration_value = int(str(first_digit) + str(last_digit))
        total_sum += calibration_value
    return total_sum

text = open('input.txt', 'r')
text = text.readlines()

print(calibration(text))

# --- PART 2 ---
total = 0
s = ""
nums = {"one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9"}

with open("input.txt") as f:
    for line in f:
        first = None
        for i, c in enumerate(line):
            if c.isdigit():
                if first == None:
                    first = c
                    s = c + c
                else:
                    s = first + c
            else:
                for n in nums:
                    if line[i:].startswith(n):
                        if first == None:
                            first = nums[n]
                            s = first + first
                        else:
                            s = first + nums[n]
        total += int(s)

print(total)