import random

def play():
    user=input("What's your choice?\n'r' for rock, 'p' for paper, 's' for scissors: ")
    computer =random.choice(['r','p','s'])
    print(computer)

    if computer == user:
        return 'tie'

    # r>s , p>r, s>p
    if win(user, computer):
        return 'You WON!'

    return 'You LOST!'

def win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's' ) or (player == 'p' and opponent == 'r' ) or (player == 's' and opponent == 'p' ):
        return True

print(play())