letters = input("Write your letters\n")
words_puzzle = {}
words_puzzle[0] = input("Write your words\n")
words_puzzle[1] = input("Write your words\n")
words_puzzle[2] = input("Write your words\n")

for i in words_puzzle:
    words = []
    words = words_puzzle[i].split(" ")
    print(words)

