def getInput(x):
    if x == "puzzle":
        puzzle = input("Please enter the puzzle:")
        puzzle = puzzle.lower()
        checkInput(puzzle)
        return puzzle
    elif x == "words":
        words = input("Please enter the words:")
        words = words.lower()
        return words
    return 1

def printPuzzle(x):
    temp_list = x.split("-")
    for i in range(len(temp_list)):
        print(temp_list[i])

def checkInput(x):
    for i in x:
        if not ((ord(i) <= 122 and ord(i) >= 97) or (ord(i) <= 90 and ord(i) >= 65) or i == "-"):
            return False
    temp_list = x.split("-")
    length = len(temp_list[0])
    for i in range(len(temp_list)):
        if len(temp_list[i]) != length:
            return False
    if len(temp_list) < 2:
        return False
    return True

def findWords(x,y):
    temp_list = x.split("-")
    words_list = y.split(",")
    row = len(temp_list)
    col = len(temp_list[0])
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""

    for i in range(row): # for horizontal
        for j in range(col):
            str1 += temp_list[i][j]
    for i in range(col): # for vertical
        for j in range(row):
            str2 += temp_list[j][i]
    for i in range(col): # for reverse vertical
        for j in range(row-1,-1,-1):
            str3 += temp_list[j][i]
    for i in range(row): # for reverse horizontal
        for j in range(col-1,-1,-1):
            str4 += temp_list[i][j]

    print(str1,str2,str3,str4)

    for word in words_list:
        if str1.find(word) > -1:
            foundrow = str1.find(word) // col
            foundcol = str1.find(word) % col
            print("Found {} at ({},{})-({},{})".format(word,foundrow,foundcol,foundrow,foundcol+len(word)-1))
        elif str2.find(word) > -1:
            foundrow = str2.find(word) % row
            foundcol = str2.find(word) // row
            print("Found {} at ({},{})-({},{})".format(word,foundrow,foundcol,foundrow+len(word)-1,foundcol))
        elif word in str3:
            foundrow = row -(str3.find(word) % row) - 1
            foundcol = str3.find(word) // row
            print("Found {} at ({},{})-({},{})".format(word,foundrow,foundcol,foundrow-len(word)+1,foundcol))
        elif word in str4:
            foundrow = str4.find(word) // col
            foundcol = col -(str4.find(word) % col) - 1
            print("Found {} at ({},{})-({},{})".format(word,foundrow,foundcol,foundrow,foundcol-len(word)+1))
        else:
            print("{} does not exist".format(word))


puzzle = getInput("puzzle")

while not checkInput(puzzle):
  print("Wrong input format.")
  puzzle = getInput("puzzle")

words = getInput("words")
printPuzzle(puzzle)

findWords(puzzle,words)