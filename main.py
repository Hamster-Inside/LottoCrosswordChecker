letters = []
letters = input("Write your letters\n").split(" ")
words_puzzle = {}
words_puzzle[0] = input("Write your words\n")
words_puzzle[1] = input("Write your words\n")
words_puzzle[2] = input("Write your words\n")
hits_in_crossword = {}
word_hit = 0
for i in words_puzzle:
    hits_in_crossword[i] = 0
    words = []
    words = words_puzzle[i].split(" ")
    for word in words:
        length_of_word = len(word)
        for letter in word:
            if letter in letters:
                word_hit += 1
        if length_of_word == word_hit:
            hits_in_crossword[i] += 1
        word_hit = 0
print(hits_in_crossword)



