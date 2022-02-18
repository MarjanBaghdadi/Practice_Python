#credit: Tech with Tim youtube channel

name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Where would you like to go? ").lower()

if answer == "left":
    
    answer = input("You come to a riverr. You can walk around it or swim in it. Which one would you do (swim or walk?: ").lower()
    if answer == "swim":
        print("blah b;ah blah...")
    elif answer == "walk":
        print("blah blah blah...")
    else: 
        print("Not a valid choice. You lost")
        
elif answer == "right":
    print("blah blah blah...")
    
else:
    print("Not a valid option. You lose. ")
    