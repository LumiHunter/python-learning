import time
import csv
import random
import winsound

name = input('What is your name?')
print('Hi, ' + name + ', Time to play hangman game!', sep='')
print()
time.sleep(1)

print('Start loading...')
print()
time.sleep(0.5)

words = []
with open('./Level.1/resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)

random.shuffle(words)
q = random.choice(words)
answer = q[0].strip()    # 문자열에서 양쪽 공백 제거

guesses = set()

turns = 10

while turns > 0:
    failed = 0    # 추측 단어와 정답에서 틀린 글자 수
    for char in answer:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1
    if failed == 0:
        print()
        print()
        winsound.PlaySound('./Level.1/sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations! Your Guesses is correct!')
        break
    print()
    
    print(f'Hint: {q[1].strip()}')
    guess = input('Guess the answer.')
    for c in guess:
        if c not in guesses:
            guesses.add(c)
    if guess not in answer:
        turns -= 1
        print('Oops! Wrong')
        print('You have', turns, 'more guesses!')
        if turns == 0:
            winsound.PlaySound('./Level.1/sound/bad.wav', winsound.SND_FILENAME)
            print('You lose.')