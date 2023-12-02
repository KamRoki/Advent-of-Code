# ADVENT OF CODE 2023

# --- Day 2: Cube Conundrum ---
# --- PART 1 ---
with open("input.txt") as f:
    sum_1 = 0
    for line in f:
        play_game = True
        game, cubes = line.split(': ')
        _, day = game.split()
        for sample in cubes.split('; '):
            for cube in sample.split(', '):
                number, color = cube.split()
                number = int(number)
                if 'red' in color and number > 12:
                    play_game = False
                if 'green' in color and number > 13:
                    play_game = False
                if 'blue' in color and number > 14:
                    play_game = False
        if play_game:
            sum_1 += int(day)

print(f'The answer to part 1 is: {sum_1}')

# --- PART 2 ---
with open('input.txt') as f:
    sum_2 = 0
    for line in f:
        play_game = True
        game, cubes = line.split(': ')
        _, game = game.split()
        red_max, green_max, blue_max = 1, 1, 1
        for sample in cubes.split('; '):
            for cube in sample.split(', '):
                number, color = cube.split()
                number = int(number)
                if 'red' in color and number > red_max:
                    red_max = number
                if 'green' in color and number > green_max:
                    green_max = number
                if 'blue' in color and number > blue_max:
                    blue_max = number
        sum_2 += (red_max * green_max * blue_max)

print(f'The answer to part 2 is: {sum_2}')




