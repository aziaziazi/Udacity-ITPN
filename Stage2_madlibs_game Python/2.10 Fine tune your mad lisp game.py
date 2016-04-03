#!/usr/bin/env python
# -*- coding: utf-8 -*-

parts_of_speech  = [["_1_","ronronnement"], ["_2_","chaton"]]

test_string = """
Le _1_ apparaît dès l’âge de deux jours lors de la tétée,
où chatte et le _2_ communiquent par _1_ ; ce phénomène apparaît aussi lors
de la toilette du _2_ par la mère. Le _1_ se manifeste le plus souvent lorsque
l’animal éprouve du plaisir mais aussi de la souffrance : stressé, blessé et même en mourant,
le chat peut ronronner ; il s’agit donc de l’expression d’un sentiment fort. Enfin, le _1_
sert aussi à communiquer, puisque la rencontre de deux chats déclenche des ronronnements.
Le chat ronronne le plus souvent pour exprimer la dépendance affective : le _2_ dépend de sa mère
et de son lait, de l’homme lorsqu’il réclame des soins ou des caresses.
"""

def try_to_find(number,solution):
	user_input = raw_input("What should stand for " + str(number) + " ? >>> ")
	while user_input != solution:
		user_input = raw_input("NO ! Try again :) >>> ")
	print "YEAH !!!"
	return True


def play_game(ml_string,parts_of_speech):
	print "*** Try to find the missing words :"
	print ml_string
	for enigm in parts_of_speech:
		if try_to_find(enigm[0],enigm[1]):
			ml_string = ml_string.replace(enigm[0],enigm[1])
	print "YOU DID IT !"
	return ml_string


print play_game(test_string, parts_of_speech)