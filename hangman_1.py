import random

HANGMAN_PICS = ['''
   +----+
	 |
	 |
	 |
	===''','''
	+---+
	0   |
		|
		|
	   ===''']


	   # define word list
words = 'apple bananna orange kiwi'.split()


def getRandomWord(wordList):
	wordIndex = random.randint(0, len(wordList) - 1)
	return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
	print (HANGMAN_PICS[len(missedLetters)])
	print ()
	print ('Missed letters:', end='')
	for letter in missedLetters:
		print(letter, end='')
	print()
	blanks = '_' * len(secretWord)
	for i in range (len(secretWord)):
		if secretWord[i] in correctLetters:
			blanks =  blanks[:i] + secretWord[i] + blanks[i+1:]
	for letter in blanks:
		print(letter, end='')
	print()

def getGuess(alreadyGuessed):
	while True:
		print('Guess a Letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('PLease enter a single letter: ')
		elif guess in alreadyGuessed:
			print('You have already guesed that letter.  Choose again: ')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a letter: ')
		else:
			return guess

def playAgain():
	print('Do you want to play again (yes or no): ')
	return input().lower().startswith('y')

print ('HANGMAN') 
missedLetters = '' #define variable to empty string
correctLetters = '' #define variable to empty string
secretWord = getRandomWord(words) #grabs random word from word list
gameIsDone = False
while True:
	displayBoard(missedLetters,correctLetters,secretWord)
	guess = getGuess(missedLetters + correctLetters)

	if guess in secretWord:
		correctLetters = correctLetters + guess
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
			if foundAllLetters:
				print('Yes! The secret word is: ' + secretWord)
				gameIsDone = True
		else:
			missedLetters = missedLetters + guess

			if len(missedLetters) == len(HANGMAN_PICS) - 1:
				displayBoard(missedLetters,correctLetters,secretWord)
				print('You have run out of guesses\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was ' + secretWord)
				gameIsDone = True

		if gameIsDone:
			if playAgain():
				missedLetters = ''
				correctLetters = ''
				gameIsDone = False
				secretWord = getRandomWord(words)
			else:
				break

