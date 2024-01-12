# import time and random 
from time import *
import random as r

#main function
def main():
    # word for typing test in 3 sententes
    test=["Hunt and peck (two-fingered typing), also known as Eagle Finger, is a common form of typing in which the typist presses each key individually. Instead of relying on the memorized position of keys, the typist must find each key by sight. Use of this method may also prevent the typist from being able to see what has been typed without glancing away from the keys. Although good accuracy may be achieved.",
    "When we talk about motivating others, the justification is the end result (either we want to avoid the pain or go towards pleasure) or what we want to get the person to do. How we achieve the end result, are our alternatives. As a manager, we need to understand the other person's justification and then come up with alternatives. We may then choose the right alternative. However, in general.",
    "Web designers are expected to have an awareness of usability and if their role involves creating mark up then they are also expected to be up to date with web accessibility guidelines. The different areas of web design include web graphic design; interface design; authoring, including standardised code and proprietary software; user experience design; and search engine optimization."]

    #take a random sentence from the test array
    test1=r.choice(test)
    
    #input for enter username and extra print statement for line gap
    username=input("Enter UserName: ")
    print()
    print()

    #options for user
    print("1. Start Typing Test")
    print("2. Show Leader Board")
    print("3. Exit")
    choose=input("1/2/3: ")

main()