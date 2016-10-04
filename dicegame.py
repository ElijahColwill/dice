from random import randrange
import input
import time

def score(score):
    a = randrange(1, 7)
    b = randrange(1, 7)
    print "Rolled %d and %d.\n" % (a, b)
    if a == 1 or b == 1:
        if a == 1 and b == 1:
            score = 0
            print "Rolled two ones. Turn over, score reset.\n"
        else:
            print "Rolled a 1. Turn over.\n"
    else:
        if a == b:
            print "Rolled doubles. Must roll next turn.\n"
            score = (score + a + b) * -1
        else:
            score = score + a + b
    return score


def turn(total, turn):
    print "Start turn!"
    hold = 0
    while hold == 0:
        change = total
        total = score(total)
        if change == total or total == 0:
            hold = 1
        elif total < 0:
            total = total * -1
            hold = 0
        else:
            if turn == False:
                print "Hold? Yes or No:"
                hold = input.scan()
                if hold == "Yes" or hold == "yes" or hold == "y" or hold == "Y":
            	       hold = 1
                else: hold = 0
            else:
                print "Deciding wether to hold...\n"
                hold = randrange(0, 3)
                if hold == 2:
                    print "Choice: Hold."
                else:
                    hold = 0
                    print "Choice: Don't hold."

    return total


def game():
    print "Welcome to Pig (two dice version)!\n"
    player_score = 0
    computer_score = 0

    while player_score < 100 and computer_score < 100:
        print "Press enter when ready to start player turn."
        input.scan()
        player_score = turn(player_score, False)
        print "\nPlayer score: %d" % player_score
        print "\nPress enter when ready to start computer turn."
        input.scan()
        computer_score = turn(computer_score, True)
        print "\nComputer score: %d" % computer_score

    if player_score >= 100:
        print "\nPlayer wins!"
    else: print "\nComputer wins!"

    print "\nHere are the scores:"
    print "Player score: %d" % player_score
    print "Computer score: %d" % computer_score


game()
