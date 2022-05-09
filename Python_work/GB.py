
ghosties = [14.5,228.7,116.8]
print(f"Oh no there are floating points about that need to be rounded up..{ghosties}..trouble is they're only interested in facts about the Ghostbusters movie, answer the following: what date whas the movie released? (DD)")

def spooky():
    global ghosties
    try:
        answer1 = input()            
        if int(answer1) == 15 and 14.5 in ghosties:
            ghosties[0] = int(15)
            print("correct it was released on the 15th of July")
            spooky2()
        elif int(answer1) != 15:
            print ("wrong try again")
            spooky()
    except:
        answer1 
        print("That's not a number")
        spooky()

def spooky2():
    print ("how much money, world wide, did it make? (000)")
    global ghosties
    try:
        answer2 = input()
        if int(answer2) == 229 and 228.7 in ghosties:
            ghosties[1] = int(229)
            print("correct it made £229 million")
            spooky3()        
        elif int(answer2) != 229:            
            print ("wrong try again")
            spooky2()
    except:
        answer2
        print("That's not a number")
        spooky2()    

def spooky3():
    print("How many minutes long was it?(000)")
    global ghosties
    try:
        answer3 = input()
        if int(answer3) == 117 and 116.8 in ghosties:
            ghosties[2] = int(117)
            print("Correct it was 117 minutes long, you rounded up all the floating points!")
            print(f"Ghosties caught{ghosties}")
        elif int(answer3) != 117:
            print ("wrong try again")
            spooky3()    
    except:
        answer3
        print("That's not a number")
        spooky3()        
spooky()


