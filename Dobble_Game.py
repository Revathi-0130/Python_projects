import string
import random
choice = 0
score = 0
size = int(input("What is the size of the card? "))
while(choice == 0):
    symbols = list(string.ascii_letters)
    sameSymbol = random.choice(symbols)
    print(size)
    card1 = [0] * size
    card2 = [0] * size
    pos1 = random.randint(0, size-1)
    pos2 = random.randint(0, size-1)
    choice = 0

    if(pos1 == pos2):
        card1[pos1] = sameSymbol
        card2[pos2] = sameSymbol
    else:
        card1[pos1] = sameSymbol
        card2[pos2] = sameSymbol
        symbols.remove(sameSymbol)
        card1[pos2] = random.choice(symbols)
        symbols.remove(card1[pos2])
        card2[pos1] = random.choice(symbols)
        symbols.remove(card2[pos1])
    i = 0
    while(i < size):
        if(i != pos1 and i != pos2):
            card1[i] = random.choice(symbols)
            symbols.remove(card1[i])
            card2[i] = random.choice(symbols)
            symbols.remove(card2[i])
        i = i + 1
    print("Card_1: ", card1)
    print("Card_2: ", card2)
        
    n = input("What is the common letter in both the cards? ")
    if (n == sameSymbol):
        print("Correct")
        score = score + 1
        choice = 0
    
    else:
        print("Wrong")
        choice = 1

print("Your final Score is: ", score)
        
    
        

