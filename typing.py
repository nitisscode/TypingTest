# import time and random from libraries

from time import *
import random as r
import json              #calling json file


file=False
finaldata=None

#function for calling json file data
def ReadData():
    global finaldata
    try:
        file=open("data.json","r")
        x=file.read()
        finaldata=json.loads(x)
    except:
        print("Something is Wrong!")
ReadData()


#input for enter username and extra print statement for line gap
username=input("Enter UserName: ")
print()
print()

# array and dictionary for upload data in json file
arr=[]
dic={"user":None,
    "WPM":0
    }

test1=False
word=1

# word for typing test in 3 sententes
test=["Hunt and peck (two-fingered typing), also known as Eagle Finger, is a common form of typing in which the typist presses each key individually. Instead of relying on the memorized position of keys, the typist must find each key by sight. Use of this method may also prevent the typist from being able to see what has been typed without glancing away from the keys. Although good accuracy may be achieved.",
"When we talk about motivating others, the justification is the end result (either we want to avoid the pain or go towards pleasure) or what we want to get the person to do. How we achieve the end result, are our alternatives. As a manager, we need to understand the other person's justification and then come up with alternatives. We may then choose the right alternative. However, in general.",
"Web designers are expected to have an awareness of usability and if their role involves creating mark up then they are also expected to be up to date with web accessibility guidelines. The different areas of web design include web graphic design; interface design; authoring, including standardised code and proprietary software; user experience design; and search engine optimization."]


test1=r.choice(test) #take a random sentence from the test array

#function for catch typing mistake
def mistake(para,usertest):
    error=0
    global word
    for i in range(len(para)):
        try:
            if(para[i]!=usertest[i]):
                error+=1
            if(usertest[i]==" "):
                word+=1    
        except:
            error+=1   
    return error  

#function for measure time of typing in word per minute
def speedtime(time_s,time_e,userinput):
    global word

    tytest=round(time_e-time_s)/60
    print("Word Typed:",word)
    print("Time Taken:",round(tytest,2),"min")
    
    speed=round(word/tytest)
    return speed

#Function for store json data in array (List)
def userdata(dic,finaldata):
    res=False
    
    if(finaldata!=None): 
        for a in finaldata:
            if(username==a["user"]):
                res=True
            
            arr.append(a)

    if(res==False):
        arr.append(dic)
    else:
        for i in finaldata:
            if(username==i["user"]):
                i["WPM"]=dic["WPM"]


# function for user typing input and time capture
def get_user_input():
    global word, test1
    
    print()
    print(test1)
    print()

    time1=time()
    testinput=input("Type here: ")
    time2=time()

    errors=mistake(test1,testinput)
    TypingSpeed=speedtime(time1,time2,testinput)
    
    print("Errors: ",errors)
    print("speed: ",TypingSpeed,"WPM")

    dic["user"]=username
    dic["WPM"]=TypingSpeed
    userdata(dic,finaldata)
    print(arr)

    word=1






#main function to choose options for user
def main():
    print("1. Start Typing Test")
    print("2. Show Leader Board")
    print("3. Exit")
    choose=input("1/2/3: ")
    if(choose=="1"):
        get_user_input()   
main()          








