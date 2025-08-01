import functions as f

# Grab dicts
counter_dict, position_dict, words_dict = f.establish_dicts()

for guess_num in range(7):

    # Prompt the user for guess and results
    print(list(words_dict.keys())[:20])
    guess = input("What was your guess? (Type \"quit\" to quit)\n").lower()
    if guess == "quit":
        break
    results = input("What was the result of the guess?\nUse \"x\" for grey, \"y\" for yellow and \"g\" for green!\n").lower()

    # Handle results
    words_dict = f.handle_results(guess, results, words_dict)

    # Rescore
    words_dict = f.rescore(words_dict)