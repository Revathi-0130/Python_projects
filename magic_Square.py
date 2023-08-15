n = int(input("What is the size of the maguc Square? "))
magicSquare = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(0)
    magicSquare.append(l)

if (n % 2 == 0):
    print("Magic Square is not possible")

else:
    i = n // 2
    j = n - 1
    count = 1
    num = n * n
    
    while(count <= num):
        
        if (i < 0 and j == n):
            i = 0
            j = n - 2
            
        elif(i < 0):
            i = n - 1
            
        elif(j == n):
            j = 0
        
        else:
            
            if(magicSquare[i][j] != 0):
                i = i + 1
                j = j - 2
                continue
            
            else:
                magicSquare[i][j] = count
                i = i - 1
                j = j + 1
                count = count + 1

for i in range(n):
    for j in range(n):
        print(magicSquare[i][j],end = " ")
    print("")
        


        
        
            
        
        
        
        


    

