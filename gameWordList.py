def makeGameWordList():
    wordList = open("words_alpha.csv", 'r').read().split('\n')
    for word in wordList:
        if len(word) > 2 and len(word) < 9:
            gameWordList = wordList.append(word)
    return gameWordList

def main():
    gameWordList = makeGameWordList()

if __name__ == "__main__":
    main()