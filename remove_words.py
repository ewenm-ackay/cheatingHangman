f = open("words_alpha.csv", "r")

words = f.read().split("\n")

vowels = ["a", "e", "i", "o", "u"]
allowed = []


for word in words:
    count = 0
    for v in vowels:
        if v in word:
            count += 1
    if count != 0:
        if len(word) > 2 and len(word) < 8:
            allowed.append(word)
    

with open("words_vowels.csv", "a") as f:
    for word in allowed:
        f.write(word + "\n")
