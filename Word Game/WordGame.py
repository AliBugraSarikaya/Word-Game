import sys
import string 
letters = []
words = []
def letter_control(word):
    letter_control_count = 0
    for i in word:
        if i not in string.ascii_letters:
            letter_control_count += 1
    if letter_control_count != 0:
        print(f"Argument {word} is not a word. All arguments should be word")

if len(sys.argv) != 4:
    print("Please run with 3 arguments")
elif len(sys.argv[1]) == len(sys.argv[2]) or len(sys.argv[1]) == len(sys.argv[3]) or len(sys.argv[2]) == len(sys.argv[3]):
    print("Arguments should be a different length")
elif any(not word.isalpha() for word in sys.argv[1:]):
    letter_control(sys.argv[1])
    letter_control(sys.argv[2])
    letter_control(sys.argv[3])
else:
    print("Find longest word using letters given below\n")
    for i in sys.argv[1:]:
        words.append(i)
        for j in i:      
            letters.append(j)
    letters.sort()
    print(letters)
    placement = 0
    your_guess_word = input("Guess a longest word: ")
    if your_guess_word in words:
        print("You found a word from list")
        for i in words:
            if len(your_guess_word) < len(i):
                placement += 1
        if placement == 0:
            print("You won 50 points !")
        elif placement == 1:
            print("You won 30 points !")
        else:
            print("You won 10 points !")
    else:
        print("The word you guessed is not in the list")
        print("You lost !")

    