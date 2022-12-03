'''
ROCK = A
PAPER = Y, 2
WIN = 6

PAPER = B
ROCK = X, 1

SCISSORS = C
SCISSORS = Z, 3
DRAW = 3
'''

score = 0

with open('input.txt', 'r') as f:
    for line in f:
        opponentChoice, myChoice = line.split(' ')
        if 'A' in opponentChoice:
            # ROCK/A CASE
            myChoice = 'X'
            if 'Y' in myChoice:
                score += 6
                # for choosing paper
                score += 2
                
            elif 'X' in myChoice:
                # for choosing rock
                score += 1
                # tie
                score += 3
            elif 'Z' in myChoice:
                # for choosing scissors
                score += 3
                
                
        elif 'B' in opponentChoice:
            # PAPER/B CASE
            myChoice = 'X'
            if 'X' in myChoice:
                # for choosing rock
                score += 1
            elif 'Y' in myChoice:
                # for choosing paper
                score += 2
                # tie
                score += 3
            elif 'Z' in myChoice:
                # for choosing scissors
                score += 3
                #win
                score += 6
                
        elif 'C' in opponentChoice:
            # SCISSORS/C CASE
            myChoice = 'X'
            if 'Z' in myChoice:
                # for tie
                score += 3
                # for choosing scissors
                score += 3
            elif 'Y' in myChoice:
                # for choosing paper
                score += 2
            elif 'X' in myChoice:
                # for choosing rock
                score += 1
                # win
                score += 6
def part_two(their_throw, your_response):
    round_points = 0
    if their_throw == 'A': # Rock
        if your_response == 'X': # Need to lose (+0)
            round_points += 3 # Scissors (+3)
        if your_response == 'Y': # Need to draw (+3)
            round_points += 4 # Rock (+1)
        if your_response == 'Z': # Need to win (+6)
            round_points += 8 # Paper (+2)
 
    elif their_throw == 'B': # Paper
        if your_response == 'X': # Need to lose (+0)
            round_points += 1 # Rock (+1)
        if your_response == 'Y': # Need to draw (+3)
            round_points += 5 # Paper (+2)
        if your_response == 'Z': # Need to win (+6)
            round_points += 9 # Scissors (+3)  
   
    elif their_throw == 'C': # Scissors
        if your_response == 'X': # Need to lose (+0)
            round_points += 2 # Paper (+2)
        if your_response == 'Y': # Need to draw (+3)
            round_points += 6 # Scissors (+3)
        if your_response == 'Z': # Need to win (+6)
            round_points += 7 # Rock (+1)
    return round_points
print('part one **')
print('--> ' + str(score))

part_two_score = 0    
 
with open('day2/input.txt') as input_data:
    input_data = [line.strip() for line in input_data.readlines()]
 
    for round in input_data:
        part_two_score += part_two(round[0], round[2])
 
print('part two **')
print('--> ' + str(part_two_score))
