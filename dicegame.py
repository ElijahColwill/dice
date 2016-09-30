from random import randrange
# Please read README.md

player1_total = 0
player2_total = 0

def turn(total):
    print "Start turn!"
    hold = False
    while hold == False:
        a = randrange(1, 7)
        b = randrange(1, 7)
        print "You rolled %d and %d.\n" % (a, b)
        if a == 1 or b == 1:
            if a == 1 and b == 1:
                total = 0
                print "You rolled two ones. Turn over, score reset.\n"
                hold = True
            else:
                print "You rolled a 1. Turn over.\n"
                hold = True
        else:
            if a == b:
                print "You rolled doubles. You must roll next turn.\n"
                hold = False
                total = total + a + b
            else:
                total = total + a + b
                hold = raw_input("Hold? Yes or No:\n")
                if hold == "Yes" or hold == "yes" or hold == "y" or hold == "Y":
                	hold = True
                else: hold = False
    print "Here is your new score: %d.\n" % total
    return total


print "Welcome to Pig (two dice version)!\n"

input = False
above100 = False

while input == False:

	players = raw_input("Type number of players (2+):\n")

	if players.isdigit():
		if players >= '2':
			if players < '99999':
				input = True
				playerwins = 0
				player = []
				scores = []
				for i in range(0, int(players)):
					player.append(i)
					scores.append(i)

				print player

				for i in scores:
					scores[i] = 0

				while above100 == False:
					for i in player:
						if above100 == False:
							current_player = player[i] + 1
							current_score = scores[player[i]]
							current_player = int(current_player)
							print "Press enter when ready to start player %d's turn." % current_player
							raw_input()
							current_score = turn(current_score)
							scores[player[i]] = current_score
							if current_score >= 100:
								above100 = True
							playerwins = player[i]


				print "Player %d wins!" % (playerwins + 1)
				print "Here are the scores:"
				for i in player:
					current_player = player[i]
					actual_score = scores[current_player]
					actual_player = current_player + 1
					print "Player %r has a score of %r." % (actual_player, actual_score)

			else:
				print "Not valid input!"
				input = False

		else:
			print "Not valid input!"
			input = False
	else:
		print "Not valid input!"
		input = False





# 100
