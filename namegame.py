name = input("What is your name?") 

while name != "":
#Print their name 100 times 
    for x in range (100):
        print(name, end = " ")
    print("======End======")
    name = input ("Type another name, or just hit [ENTER] to quit: ")
print("Thanks for playing!")
