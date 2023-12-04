# ADVENT OF CODE 2023

# --- Day 4: Scratchcards ---
# --- PART 1 ---
with open('input.txt', 'r') as f:

    points = 0

    for line in f:
        s = line.split('|')
        win_cards = s[0].split(':')[1].split()
        hand_cards = s[1].split()
        matches = [1 for card in hand_cards if card in win_cards]
        count = sum(matches)
        if count > 0:
            points = points + 2**(count - 1)

print(f'Total points: {points}')






