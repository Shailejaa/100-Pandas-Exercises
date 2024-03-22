# Step 1 - Hangman Project
word_list = ["aardvark", "baboon", "camel"]
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

length = len(word_list)
# chosen_word = random.choice(word_list)
for word in word_list:
    # print(word)
    pick = random.randint(0, length - 1)
    result = word_list[pick]
    final = ''
    for i in result:
        final += '_'
print(result)

for i in range(len(result)):
    guess = input("Guess ").lower()
    for n, j in enumerate(result):
        if j == guess:
            # print(n)
            final = list(final)
            final[n] = j
            output = ''.join(final)
print(output)




