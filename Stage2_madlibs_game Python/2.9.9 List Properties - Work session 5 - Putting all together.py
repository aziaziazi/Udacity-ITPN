# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input.

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """Straight outta PLACE, crazy NOUN named PERSON,
from the gang called PLURALNOUN Wit Attitude"""

# def word_in_pos(word, parts_of_speech):
#     for pos in parts_of_speech:
#     	w = word.find(pos)
#     	word_len = len(pos)
#     	if w != -1:
#     		return word[:w] + "corgi" + word[w+word_len:]
#     return word


# def play_game(ml_string, parts_of_speech):
#     ml_string = ml_string.split()
#     replaced = []

#     for i in ml_string:
#     	replaced.append(word_in_pos(i, parts_of_speech))

#     replaced = " ".join(replaced)
#     return replaced

#Search a word (pos/part of speach) in a string (word) and if inside, return it
def word_in_pos(word,parts_of_speech):
	#loop for every possible words
	for pos in parts_of_speech:
		#if the word is find inside string to compare
		if pos in word:
			#return it !
			return pos
	#if nothing found, return "None"
	return None

#Take a string(ml_string), divide it by words and send each word with
#the parts_of_speach list to word_in_pos to check if inside or not.
#If inside, replace
def play_game(ml_string,parts_of_speech):
	#split ml_string word by words
	ml_string = ml_string.split()
	#create the empty final list
	replaced = []
	#loop in every words of the ml_string list
	for word in ml_string:
		#run word_in_pos with the word and list of words to search
		replacement = word_in_pos(word,parts_of_speech)
		#if the word is return
		if replacement != None:
			#ask user to type in a word, in the type of the one returned
			#Doesn't work in sublime text, use terminal
			#user_input = raw_input("Type in a " + str(replacement))
			#OR Predefined remplacement word
			user_input = "corgy"
			#take the initial word and remplace it with the user imput
			#.replace allow to keep syntax around (,.!")
			word = word.replace(replacement, user_input )
			#add item at the end of the final list
			replaced.append(word)
		#if "none" as result, add item at the end of the final list
		else:
			replaced.append(word)
	#join every work in the list in one sentance.
	replaced = " ".join(replaced)
	return replaced

print play_game(test_string, parts_of_speech)