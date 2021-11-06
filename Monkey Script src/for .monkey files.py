from sys import *

def Lang(Syntax):
    State = 0
    Token = ""
    String = ""
    for Char in Syntax:
        Token += Char
        if Token == " ":
            if State == 0:
                Token = ""
 
        elif Token == "\n":
            Token = ""

            # Print Command
 
        elif Token == "monkey say":
            Token = ""
 
        elif Token == "\"":
            if State == 0:
                State = 1
                Token = ""

            elif State == 1:
                State = 0
 
        elif State == 1:
            String += Token
            Token = ""
 
    print(String)

    # Reads the test.monkey file

Content = open("test.monkey", "r").readlines()
for Line in Content:
    Lang(Line)
 
 
