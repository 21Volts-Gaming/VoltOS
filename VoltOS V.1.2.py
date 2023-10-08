#imports the stuff adn sets up other things
from ast import While
from operator import index
import turtle
from turtle import Screen, bgcolor
import random
import time
import os
from unicodedata import unidata_version
filepath = 'C:\tim stuff\OneDrive - Bayfield High School\2023\10DTI\Programming\Python\VoltOS\VoltOS V.1.2.py'
basename = os.path.basename(filepath)

#Sets starting variables.
global loading
global User
global SignIn
global Unid
global Pind
global LoopStats
screen = Screen()
loading = 0
SignIn =False
User = 0
Uind = 0
Pind = 0
LoopStats = False
screen.colormode(255)
Volt = turtle.Turtle()
global FirstStart
global UsernameDatabase
FirstStart = True
UsernameDatabase = list(())
PasswordDatabase = list(())
AccsessDatabase = list(())
screen.bgcolor("black")
Volt.hideturtle()

#Is used to set up a new user and during first-time setup.
def UserSetup():
    global SignIn
    global User
    global FirstStart
    global access
    UseTerminal()
    print ("<V.O.S> Create new user")
    print ("<V.N.A> Your username can not be the same as another user.")
    print ("<V.N.A> Your username must be between 3 and 16 charectors long.")
    print ("<V.N.A> Your password cannot be empty.")
    print ("<V.N.A> If you did not intend to create a new user, please enter 0 as new username.")
    LoopStats = True
    while LoopStats == True:
        print ("<V.O.S> New username:")
        nav = input("<V.O.S><RequestingInput> ")
        if nav == "0":
            LoopStats = False
            print ("<V.O.S> Exiting user setup")
            Menu()
        elif len(nav) < 3:
            print ("<V.O.S> Username too short")
        elif len(nav) > 16:
            print ("<V.O.S> Username too long")
        elif nav in UsernameDatabase:
            print ("<V.O.S> Existing username already in UsernameDatabase")
        else:
            if FirstStart == True:
                UsernameDatabase.insert(0, nav)
            else:
                UsernameDatabase.append(nav)
            if SignIn == False:
                User = nav
                Uind = UsernameDatabase.index(nav)
            while LoopStats == True:
                print ("<V.O.S> New password:")
                nav = input("<V.O.S><RequestingInput> ")
                if nav == "0":
                    print ("<V.O.S> Exiting user setup")
                    UsernameDatabase.pop(Uind)
                    Menu()
                elif nav == "":
                    print ("<V.O.S> Password cannot be empty.")
                else:
                    LoopStats = False
                    if FirstStart == True:
                        PasswordDatabase.insert(0, nav)
                        AccsessDatabase.insert(0, 5)
                        access = AccsessDatabase[0]
                    else:
                        PasswordDatabase.append(nav)
                        LoopStats = True
                        print ("<V.O.S> Admin, please input new user accesss level.")
                        while LoopStats == True:
                            nav = input("<V.O.S><RequestingInput> ")
                            if nav == "1" or nav == "2" or nav == "3" or nav == "4":
                                AccsessDatabase.append(int(nav))
                                LoopStats = False
                            else:
                                print ("<V.O.S> Input unacceptable")
                    if SignIn == False:
                        Pind = PasswordDatabase.index(nav)
    if SignIn == False:
        SignIn = True
        FirstStart = False
    Menu()

#Displays a message telling the user to input at terminal.
def UseTerminal():
    clr()
    Volt.goto(0, -160)
    Volt.pencolor("grey")
    Volt.write("Input required at teminal", font=("Josefin Sans", 50, 'italic', 'bold'), align=("center"))

#only accesssed when there is already a user in database. Signs a user in to the OS.
def SignOn():
    global User
    global SignIn
    global Uind
    global Pind
    global access
    UseTerminal()
    print ("<V.O.S> Sign in")
    print ("<N.V.A> If you do not wish to sign in, enter 0 in ither username or password.")
    LoopStats = True
    while LoopStats == True:
        print ("<V.O.S> Username:")
        nav = input("<V.O.S> <Awaiting input> ")
        if nav in UsernameDatabase:
            Uind = UsernameDatabase.index(nav)
            Pind = Uind
            while LoopStats == True:
                print ("<V.O.S> Password:")
                nav = input("<V.O.S> <Awaiting input> ")
                if nav == PasswordDatabase[Pind]:
                    LoopStats = False
                    User = UsernameDatabase[Uind]
                    access = AccsessDatabase[Uind]
                    print ("<V.O.S> Sucsessful sign-in to", User)
                    SignIn = True
                    Menu()
                elif nav == "0":
                    LoopStats = False
                    print ("<V.O.S> Exiting user sign in")
                    Menu()
                else:
                    print ("<V.O.S> Password incorrect")
        elif nav == "0":
            LoopStats = False
            print ("<V.O.S> Exiting user Sign in")
            Menu()
        else:
            print ("<V.O.S> Username not in database")
            
#Does the opposate of sign in.
def SignOut():
    global User
    global SignIn
    global Uind
    global Pind
    global access
    print ("<V.O.S> Signing out from", User,"...")
    User = 0
    SignIn = False
    Uind = 0
    Pind = 0
    access = 0
    print ("<V.O.S> Sign-out sucsess")
    print ("<V.O.S> Returning to menu...")

#draws the logo on the screen (not including the circle). Only used on startup or on command.
def Logo():
    Volt.penup()
    Volt.goto(-90, 150)
    Volt.setheading(-65)
    Volt.pencolor("grey")
    Volt.pensize(20)
    Volt.pendown()
    Volt.forward(200)
    Volt.penup()
    Volt.goto(80, 150)
    Volt.setheading(-115)
    Volt.pencolor(255, 0, 0)
    Volt.pendown()
    Volt.forward(160)

#a space where infomation about the software is displayed.
def info():
    Volt.penup
    title()
    Volt.pencolor("white")
    Volt.goto(-250, -300)
    Volt.write("Version: V.1.2", font=("arial", 25))
    Volt.goto(-250, -340)
    Volt.write("Auther: Timothy Birchall", font=("arial", 25))
    Volt.goto(-250, -380)
    Volt.write("Legacy name: Microsoft Startup Concept Turtle", font=("arial", 25))
    time.sleep(1)
    Volt.goto(0, -460)
    Volt.write("1 = Return to menu", font=("arial", 25), align=("center"))
    LoopStats = True
    while LoopStats == True:
        nav = input("<V.O.S> <Awaiting input> ")
        if nav == "1":
            LoopStats = False
            print ("<V.O.S> Returning to menu...")
            Menu()
        else:
            print ("<V.O.S> Input unacceptable")

#a simulated loading system with a color changing circle around the logo.
def LoadingFunc():
    LightDark = False
    global loading
    loading = 0
    circleSides = 80
    circleSize = 12
    fullLoad = 100
    LL = 127
    DL = 0
    LH = 255
    DH = 127
    Volt.penup()
    Volt.goto(-13, 235)
    Volt.setheading(0)
    Volt.pendown()
    Volt.speed(200)
    while not loading == fullLoad:
        if LightDark == True:
            Red = random.randint(LL, LH)
            Green = random.randint(LL, LH)
            Blue = random.randint(LL, LH)
            LightDark = False
        else:
            Red = random.randint(DL, DH)
            Green = random.randint(DL, DH)
            Blue = random.randint(DL, DH)
            LightDark = True
        Volt.pencolor(Red, Green, Blue)
        for i in range(circleSides):
            Volt.forward(circleSize)
            Volt.rt(360/circleSides)
            i = i+1
        if loading > 80:
            loading = fullLoad
        else:
            loading = random.randint (loading+5, loading+20)
        print ("Loading = %",loading)
    Volt.pencolor("white")
    for i in range(circleSides):
        Volt.forward(circleSize)
        Volt.rt(360/circleSides)
        i = i+1

#lists all the created users in the database.
def userList():
    i = 0
    while i < len(UsernameDatabase):
        print(i, "=", UsernameDatabase[i])
        i = i+1

#displays the title
def title():
    clr()
    Volt.goto(0, -160)
    Volt.pencolor("grey")
    Volt.write("Volt", font=("Josefin Sans", 50, 'italic', 'bold'), align=("center"))
    Volt.goto(0, -270)
    Volt.pencolor("red")
    Volt.write("OS", font=("Impact", 80), align=("center"))

#the main hub. Where the user can navigate around the OS.
def Menu():
    global access
    clr()
    Volt.penup()
    Volt.pencolor("grey")
    Volt.goto(0, -160)
    #the title under the main logo is changed depending on the sign in stats.
    if SignIn == True:
        Volt.write("Welcome", font=("Josefin Sans", 50, 'italic', 'bold'), align=("center"))
    else:
        title()
    Volt.pencolor("red")
    Volt.goto(0, -270)
    if SignIn == True:
        Volt.write(User, font=("Impact", 80), align=("center"))
        Volt.goto(0, 350)
        Volt.pencolor("white")
        if access == 5:
            Volt.write("You have level: Admin", font=("Impact", 30), align=("center"))
        else:
            Volt.write("You have level: " + str(access), font=("Impact", 30), align=("center"))
    time.sleep(1)
    Volt.penup()
    #writes the options.
    Volt.pencolor("white")
    Volt.goto(-200, -350)
    if FirstStart == True:
        Volt.write("1 = First time setup", font=("arial", 25), align=("center"))
    elif SignIn == False:
        Volt.write("1 = Sign in", font=("arial", 25), align=("center"))
    else:
        Volt.write("1 = Sign out", font=("arial", 25), align=("center"))
    if SignIn == True:
        Volt.goto(-200, -400)
        Volt.write("2 = New user", font=("arial", 25), align=("center"))
    Volt.goto(-200, -450)
    Volt.write("info = Software information", font=("arial", 25), align=("center"))
    Volt.goto(200, -350)
    Volt.write("3 = Restart", font=("arial", 25), align=("center"))
    if SignIn == True:
        Volt.goto(200, -400)
        Volt.write("4 = List users", font=("arial", 25), align=("center"))
    LoopStats = True
    while LoopStats == True:
        nav = input("<V.O.S><Requesting input> ")
        #selection detection.
        if nav == "1":
            if SignIn == False:
                if FirstStart == True:
                    LoopStats = False
                    #if the program has started for the first time, UserSetup is chosen.
                    UserSetup()
                else:
                    #if program has not started for the first time but user is not signed in, SignOn is chosen.
                    SignOn()
            else:
                #if program has not started for the first time and user is signed in, SignOut is chosen.
                SignOut()
                Menu()
        elif nav == "info":
            info()
        elif nav == "2" and SignIn == True:
            LoopStats = False
            UserSetup()
        elif nav == "3":
            print ("<V.O.S> Restarting...")
            SignOut()
            Restart()
        elif nav == "4" and SignIn == True:
            userList()
            Menu()
        else:
            print ("<V.O.S><Input unacceptable>")

#unlike Volt.clear(), this clears only the space below the logo.
def clr():
    Volt.penup()
    Volt.goto(-400, -285)
    Volt.pensize(400)
    Volt.pencolor("black")
    Volt.setheading(0)
    Volt.pendown()
    Volt.forward(800)
    Volt.penup()
    Volt.pencolor("black")
    Volt.goto(-400, 350)
    Volt.pensize(200)
    Volt.pendown()
    Volt.forward(800)
    Volt.penup()


#used to boot up the OS and restart it without clearing variables and the databases.
def Restart():
    Volt.clear()
    Volt.speed(3)
    print ("============================= Now running: ",basename,"=============================")
    Logo()
    LoadingFunc()
    Menu()

#starts the program after all functions are defined.
Restart()

#program stall detection (P.S.D) system will restart the OS if all funtions complete prematureley causing a program stall.
infin = True
while infin == True:
    print ("<P.S.D> Restart due to program stall")
    Restart()
turtle.done()