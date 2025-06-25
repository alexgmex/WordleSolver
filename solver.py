import copy
import string

counter_dict = {letter: 0 for letter in string.ascii_lowercase}
position_dict = {pos: copy.deepcopy(counter_dict) for pos in range(5)}
words_dict = {}

with open("words.txt", "r") as file:
    for word in file:
        word = word.strip()
        words_dict[word] = 0
        for pos, letter in enumerate(word):
            counter_dict[letter] += 1
            position_dict[pos][letter] += 1

total_letters = sum(counter_dict.values())

for letter in counter_dict:
    counter_dict[letter] = round(((counter_dict[letter]/total_letters))*100, 2)
for pos in position_dict:
    for letter in position_dict[pos]:
        position_dict[pos][letter] = round((position_dict[pos][letter]/(total_letters/5))*100, 2)

# print(counter_dict)
# print(position_dict)

for word in words_dict:
    words_dict[word] = 0
    for pos, letter in enumerate(word):
        words_dict[word] += counter_dict[letter]*(position_dict[pos][letter]**2)
    words_dict[word] = round(words_dict[word], 2)

words_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))

# print(words_dict)

for guess_num in range(7):
    print(list(words_dict.keys())[:20])
    guess = input("What was your guess? (Type \"quit\" to quit)\n").lower()
    if guess == "quit":
        break
    results = input("What was the result of the guess?\nUse \"x\" for grey, \"y\" for yellow and \"g\" for green!\n").lower()

    # Check multiples
    info_dict = {}
    for pos, letter in enumerate(guess):
        if letter in info_dict:
            info_dict[letter].append((pos, results[pos]))
        else:
            info_dict[letter] = [(pos, results[pos])]
    
    # Process
    for letter in info_dict:
        # If there was only one letter in that guess
        if len(info_dict[letter]) == 1:

            # If it was a grey
            if info_dict[letter][0][1] == "x":
                for word in list(words_dict.keys()):
                    if letter in word:
                        del words_dict[word]
            
            # If it was a yellow
            elif info_dict[letter][0][1] == "y":
                for word in list(words_dict.keys()):
                    if letter not in word or word[info_dict[letter][0][0]] == letter:
                        del words_dict[word]

            # If it was a green
            elif info_dict[letter][0][1] == "g":
                for word in list(words_dict.keys()):
                    if word[info_dict[letter][0][0]] != letter:
                        del words_dict[word]

        else:
            
            grey_count = 0
            appearances = len(info_dict[letter])

            for _, result in info_dict[letter]:
                if result == "x":
                    grey_count += 1
            
            for word in list(words_dict.keys()):
                if grey_count != 0:
                    if word.count(letter) != (appearances - grey_count):
                        del words_dict[word]
                else:
                    if word.count(letter) < appearances:
                        del words_dict[word]
            
            for pos, result in info_dict[letter]:
                if result == "y":
                    for word in list(words_dict.keys()):
                        if letter not in word or word[pos] == letter:
                            del words_dict[word]
                
                if result == "g":
                    for word in list(words_dict.keys()):
                        if word[pos] != letter:
                            del words_dict[word]


            
