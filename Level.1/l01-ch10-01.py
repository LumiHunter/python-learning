import time

name = input('What is your name?')
print('Hi, ' + name + ', Time to play hangman game!', sep='')
print()
time.sleep(1)

print('Start loading...')
print()
time.sleep(0.5)

answer = 'secret'

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
        print('Congratulations! Your Guesses is correct!')
        break
    print()
    
    guess = input('Guess the answer.')
    for c in guess:
        if c not in guesses:
            guesses.add(c)
    if guess not in answer:
        turns -= 1
        print('Oops! Wrong')
        print('You have', turns, 'more guesses!')
        if turns == 0:
            print('You lose.')