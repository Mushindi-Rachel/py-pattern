def patern(n):
    #first pattern
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end="  ")
        print("")

    #second pattern
    for i in range((n-1)+1, 0, -1):
        for j in range(0, i-1):
            print("*", end="  ")
            
        print("")   +

    
n =5
patern(n) 