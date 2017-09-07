print('This game requires two players, if you do not have two players, please look for a friend to play with.')

print('Player1 is the player that will guess the word, and player2 is the player that will create the word that is being guessed.')

print('Player2, please input your word in all lowercase letters. DO NOT use any characters other than letters.')

def inputCheck():
  global wordInput
  wordInput = input()
  if wordInput.isalpha() == False:
    print("Please don't include characters outside of letters.\nTry again.")
    inputCheck()

inputCheck()

wordList = list(str(wordInput))

#letterCount = amount of letters in wordInput

letterCount = len(wordInput)
letterCount = letterCount + 1

d={}

i = 0

for x in range(1,letterCount):
  d["character{0}".format(x)] = wordList[i]
  i = i + 1
  
print(d)
print(d["character1"])
