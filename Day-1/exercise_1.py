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