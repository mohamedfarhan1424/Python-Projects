from tkinter import *
import random

global window
window = Tk()
window.geometry('470x500')
window.resizable(0, 0)
window.title('Teams and Players Entry')
window.configure(bg="cyan")
Label(window, text="GIVE TEAM NAMES", font="rockwell 15 bold").place(x=0, y=0)
Label(window, text="TEAM1", font="rockwell 15 bold").place(x=5, y=30)
Label(window, text="TEAM2", font="rockwell 15 bold").place(x=300, y=30)
team1 = StringVar()
team2 = StringVar()
tosswon = ""
team1_enter = Entry(window, textvariable=team1).place(x=5, y=60)
team2_enter = Entry(window, textvariable=team2).place(x=300, y=60)
Label(window, text="VS", font="roman 20 bold").place(x=190, y=240)
Label(window, text="PLAYERS", font="rockwell 10 bold").place(x=5, y=90)
Label(window, text="PLAYERS", font="rockwell 10 bold").place(x=300, y=90)
teamplayers1 = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                StringVar(), StringVar(), StringVar()]
teamplayers2 = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                StringVar(), StringVar(), StringVar()]
j = 90
for i in range(11):
    teamplayers1_entry = Entry(window, textvariable=teamplayers1[i]).place(x=5, y=j + 30)
    j += 30
j = 90
for i in range(11):
    teamplayers2_entry = Entry(window, textvariable=teamplayers2[i]).place(x=300, y=j + 30)
    j += 30
global k
k = 0
global frombat, frombowl, fromplay
frombat = 0
frombowl = 0
fromplay = 0


def checkEmpty():
    flag1 = 0
    flag2 = 0
    flag = 0
    label = Label(window, text="Some Input(s) is/are missing", font="rockwell 10", fg="red")
    for i in range(11):
        if teamplayers1[i].get():
            flag1 = 1
        else:
            flag1 = 0
            break
        if teamplayers2[i].get():
            flag2 = 1
        else:
            flag2 = 0
            break
    if team1.get() and team2.get():
        flag = 1
    else:
        flag = 0
    if flag1 == 1 and flag2 == 1 and flag == 1:
        toss()
    else:
        label.place(x=130, y=430)


global window2
global playdone, flg

playdone = 0
flg = 0
global overs


def toss():
    global team1, team2, tosswon, window2, window, flg, overs
    if flg == 0:
        window.destroy()
        flg = 1
    window2 = Tk()
    window2.geometry('400x200')
    window2.title('Toss winner')
    window2.resizable(0, 0)
    window2.configure(bg="cyan")
    Label(window2, text="SWITCHED THE TOSS", font="rockwell 15 bold").place(x=0, y=0)
    tosses = [team1.get(), team2.get()]
    tosswon = random.choice(tosses)
    Label(window2, text=tosswon + " won the toss", font="rockwell 15 bold").place(x=5, y=30)
    overs = IntVar()
    Label(window2, text="Select the total Overs", font="rockwell 15").place(x=5, y=60)
    overs_entry = Entry(window2, textvariable=overs).place(x=5, y=90)
    Button(window2, text="BATTING", font="rockwell 15 bold", command=checkbat).place(x=5, y=120)
    Button(window2, text="FIELDING", font="rockwell 15 bold", command=checkbowl).place(x=200, y=120)
    window2.mainloop()


totalruns = IntVar()
Over = IntVar()
balls = IntVar()
wickets = IntVar()
extras = IntVar()
scoreone = IntVar()
scoretwo = IntVar()
ballsone = IntVar()
ballstwo = IntVar()
bowlerballs = IntVar()
bowlerover = IntVar()


def checkbowl():
    global overs
    if overs.get():
        selectbowl()
    else:
        Label(window2, text="Give the Overs", font="rockwell 10", fg="red").place(x=150, y=180)


def checkbat():
    global overs
    if overs.get():
        batting()
    else:
        Label(window2, text="Give the Overs", font="rockwell 10", fg="red").place(x=150, y=160)


global label1, Striker, Non_Striker
global window3, flg2, tossingbat, tossingbowl, window4, flg4, onfieldbatting1, onfieldbatting2, window5, fromstrikerone, fromstrikertwo
flg2 = 0
tossingbat = 0
tossingbowl = 0
flg4 = 0


def batting():
    global tosswon, teamplayers1, teamplayers2, team1, team2, window4, onfieldbatting1, onfieldbatting2, window2, label1, window3, flg4, flg2, tossingbat, tossingbowl
    global fromplay, window5, fromstrikerone, fromstrikertwo, Striker, Non_Striker
    tossingbat = 1
    if fromplay == 1:
        pass
    else:
        if tossingbowl == 1:
            if flg4 == 0:
                window4.destroy()
                flg4 = 1
        else:
            if flg2 == 0:
                window2.destroy()
                flg2 = 1
    if fromplay == 1:
        window3 = Toplevel(window5)
        window3.geometry('500x500')
        window3.title('Batting Selection')
        window3.configure(bg="cyan")
    else:
        window3 = Tk()
        window3.geometry('500x500')
        window3.title('Batting Selection')
        window3.resizable(0, 0)
        window3.configure(bg="cyan")
    Label(window3, text="Select the Players to Bat", font="rockwell 15 bold").place(x=0, y=0)
    label1 = Label(window3, text="")
    if tosswon == team1.get():
        j = 30
        selectedplayers1 = []
        l1 = []

        for i in range(11):
            l1.append(IntVar())
            if tossingbowl == 0:
                selectedplayers1.append(
                    Checkbutton(window3, text=teamplayers1[i].get(), font="rockwell 15", variable=l1[i]))
                selectedplayers1[i].place(x=5, y=j + 30)
                j += 30
            elif playdone == 1:
                selectedplayers1.append(
                    Checkbutton(window3, text=teamplayers2[i].get(), font="rockwell 15", variable=l1[i]))
                selectedplayers1[i].place(x=5, y=j + 30)
                j += 30
            else:
                selectedplayers1.append(
                    Checkbutton(window3, text=teamplayers1[i].get(), font="rockwell 15", variable=l1[i]))
                selectedplayers1[i].place(x=5, y=j + 30)
                j += 30

        def show():
            global label1, onfieldbatting1, frombat, fromplay, Striker, Non_Striker, window3, window5, fromstrikerone, fromstrikertwo
            onfieldbatting1 = []
            count = 0
            j = 0
            label1.destroy()
            label1 = Label(window3, text="")
            for i in l1:
                if i.get() == 1:
                    if tossingbowl == 0:
                        onfieldbatting1.append(teamplayers1[j].get())
                        count += 1
                    elif playdone == 1:
                        onfieldbatting1.append(teamplayers2[j].get())
                        count += 1
                    else:
                        onfieldbatting1.append(teamplayers1[j].get())
                        count += 1
                j += 1
            if fromplay == 1:
                if count == 1:
                    if fromstrikerone == 1:
                        Striker.destroy()
                        Striker = Label(window5, text=onfieldbatting1[0], font="rockwell 15")
                        Striker.place(x=20, y=60)
                        fromplay = 0
                        window3.destroy()
                    elif fromstrikertwo == 1:
                        Non_Striker.destroy()
                        Non_Striker = Label(window5, text=onfieldbatting1[0], font="rockwell 15")
                        Non_Striker.place(x=20, y=90)
                        fromplay = 0
                        fromout = 0
                        window3.destroy()
                else:
                    label1.config(text="Select only one player", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)
            else:
                if count == 2:
                    print(onfieldbatting1)
                    if tossingbowl == 0:
                        selectbowl()
                    else:
                        frombat = 1

                elif count < 2:
                    label1.config(text="Two Players need to be selected", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)
                else:
                    label1.config(text="Select only two players", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)

        Button(window3, text="PLAY", font="rockwell 15 bold", command=show).place(x=50, y=400)
    elif tosswon == team2.get():
        j = 30
        selectedplayers2 = []
        l2 = []

        for i in range(11):
            l2.append(IntVar())
            if tossingbowl == 0:
                selectedplayers2.append(
                    Checkbutton(window3, text=teamplayers2[i].get(), font="rockwell 15", variable=l2[i]))
                selectedplayers2[i].place(x=5, y=j + 30)
                j += 30
            elif playdone == 1:
                selectedplayers2.append(
                    Checkbutton(window3, text=teamplayers1[i].get(), font="rockwell 15", variable=l2[i]))
                selectedplayers2[i].place(x=5, y=j + 30)
                j += 30
            else:
                selectedplayers2.append(
                    Checkbutton(window3, text=teamplayers2[i].get(), font="rockwell 15", variable=l2[i]))
                selectedplayers2[i].place(x=5, y=j + 30)
                j += 30

        def show():
            global label1, onfieldbatting1, frombat, fromplay, fromstrikerone, fromstrikertwo, Striker, Non_Striker, window5, window3
            onfieldbatting1 = []
            count = 0
            label1.destroy()
            label1 = Label(window3, text="")
            j = 0
            for i in l2:
                if i.get() == 1:
                    if tossingbowl == 0:
                        onfieldbatting1.append(teamplayers2[j].get())
                        count += 1
                    elif playdone == 1:
                        onfieldbatting1.append(teamplayers1[j].get())
                        count += 1
                    else:
                        onfieldbatting1.append(teamplayers2[j].get())
                        count += 1
                j += 1
            if fromplay == 1:
                if count == 1:
                    if fromstrikerone == 1:
                        Striker.destroy()
                        Striker = Label(window5, text=onfieldbatting1[0], font="rockwell 15")
                        Striker.place(x=20, y=60)
                        fromplay = 0
                        window3.destroy()
                    elif fromstrikertwo == 1:
                        Non_Striker.destroy()
                        Non_Striker = Label(window5, text=onfieldbatting1[0], font="rockwell 15")
                        Non_Striker.place(x=20, y=90)
                        fromplay = 0
                        window3.destroy()
                else:
                    label1.config(text="Select only one player", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)
            else:
                if count == 2:
                    print(onfieldbatting1)
                    if tossingbowl == 0:
                        selectbowl()
                    else:
                        frombat = 1
                        play()
                elif count < 2:
                    label1.config(text="Two Players need to be selected", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)
                else:
                    label1.config(text="Select only two players", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)

        Button(window3, text="PLAY", font="rockwell 15 bold", command=show).place(x=50, y=460)
    window3.mainloop()


global flg3, onfieldbowling1, bowler
flg3 = 0


def selectbowl():
    global team1, team2, teamplayers1, teamplayers2, playdone, onfieldbowling1, onfieldbowling2, label1, window3, flg3, flg2, tossingbat, tossingbowl, window4
    global window5, fromplay, bowler
    tossingbowl = 1
    if fromplay == 1:
        pass
    else:
        if tossingbat == 1:
            if flg3 == 0:
                window3.destroy()
                flg3 = 1
        else:
            if flg2 == 0:
                window2.destroy()
                flg2 = 1
    if fromplay == 1:
        window4 = Toplevel(window5)
        window4.geometry('500x500')
        window4.resizable(0, 0)
        window4.title('Over Bowling Selection')
        window4.configure(bg="cyan")
    else:
        window4 = Tk()
        window4.geometry('500x500')
        window4.resizable(0, 0)
        window4.title('Over Bowling Selection')
        window4.configure(bg="cyan")
    Label(window4, text="Select the Bowler to bowl the over", font="rockwell 15 bold").place(x=0, y=0)
    label1 = Label(window4, text="")
    if tosswon == team1.get():
        j = 30
        selectedplayers1 = []
        l1 = []

        for i in range(11):
            l1.append(IntVar())
            if tossingbat == 0:
                selectedplayers1.append(
                    Checkbutton(window4, text=teamplayers1[i].get(), font="rockwell 15", variable=l1[i]))
                selectedplayers1[i].place(x=5, y=j + 30)
                j += 30
            elif playdone == 0:
                selectedplayers1.append(
                    Checkbutton(window4, text=teamplayers2[i].get(), font="rockwell 15", variable=l1[i]))
                selectedplayers1[i].place(x=5, y=j + 30)
                j += 30
            else:
                selectedplayers1.append(
                    Checkbutton(window4, text=teamplayers1[i].get(), font="rockwell 15", variable=l1[i]))
                selectedplayers1[i].place(x=5, y=j + 30)
                j += 30

        def show():
            global label1, onfieldbowling1, frombowl, bowler, fromplay
            onfieldbowling1 = []
            count = 0
            j = 0
            for i in l1:
                if i.get() == 1:
                    if tossingbat == 0:
                        onfieldbowling1.append(teamplayers1[j].get())
                        count += 1
                    elif playdone == 0:
                        onfieldbowling1.append(teamplayers2[j].get())
                        count += 1
                    else:
                        onfieldbowling1.append(teamplayers1[j].get())
                        count += 1
                j += 1
            if fromplay == 1:
                if count == 1:
                    bowler.destroy()
                    bowler = Label(window5, text=onfieldbowling1[0], font="rockwell 15")
                    bowler.place(x=250, y=60)
                    fromplay = 0
                    window4.destroy()
                elif count < 1:
                    label1.destroy()
                    label1 = Label(window4, text="")
                    label1.config(text="One Player need to be selected", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)
                else:
                    label1.destroy()
                    label1 = Label(window4, text="")
                    label1.config(text="Select only one player", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)
            else:
                if count == 1:
                    print(onfieldbowling1)
                    if tossingbat == 0:
                        batting()
                    else:
                        frombowl = 1
                        play()
                elif count < 1:
                    label1.destroy()
                    label1 = Label(window4, text="")
                    label1.config(text="One Player need to be selected", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)
                else:
                    label1.destroy()
                    label1 = Label(window4, text="")
                    label1.config(text="Select only one player", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)

        Button(window4, text="PLAY", font="rockwell 15 bold", command=show).place(x=50, y=400)
    elif tosswon == team2.get():
        j = 30
        selectedplayers2 = []
        l2 = []

        for i in range(11):
            l2.append(IntVar())
            if tossingbat == 0:
                selectedplayers2.append(
                    Checkbutton(window4, text=teamplayers2[i].get(), font="rockwell 15", variable=l2[i]))
                selectedplayers2[i].place(x=5, y=j + 30)
                j += 30
            elif playdone == 0:
                selectedplayers2.append(
                    Checkbutton(window4, text=teamplayers1[i].get(), font="rockwell 15", variable=l2[i]))
                selectedplayers2[i].place(x=5, y=j + 30)
                j += 30
            else:
                selectedplayers2.append(
                    Checkbutton(window4, text=teamplayers2[i].get(), font="rockwell 15", variable=l2[i]))
                selectedplayers2[i].place(x=5, y=j + 30)
                j += 30

        def show():
            global label1, onfieldbowling1, frombowl, fromplay, bowler
            onfieldbowling1 = []
            count = 0
            j = 0
            for i in l2:
                if i.get() == 1:
                    if tossingbat == 0:
                        onfieldbowling1.append(teamplayers2[j].get())
                        count += 1
                    elif playdone == 0:
                        onfieldbowling1.append(teamplayers1[j].get())
                        count += 1
                    else:
                        onfieldbowling1.append(teamplayers2[j].get())
                        count += 1
                j += 1
            if fromplay == 1:
                if count == 1:
                    bowler.destroy()
                    bowler = Label(window5, text=onfieldbowling1[0], font="rockwell 15")
                    bowler.place(x=250, y=60)
                    fromplay = 0
                    window4.destroy()
                elif count < 1:
                    label1.destroy()
                    label1 = Label(window4, text="")
                    label1.config(text="One Player need to be selected", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)
                else:
                    label1.destroy()
                    label1 = Label(window4, text="")
                    label1.config(text="Select only one player", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)
            else:
                if count == 1:
                    print(onfieldbowling1)
                    if tossingbat == 0:
                        batting()
                    else:
                        frombowl = 1
                        play()
                elif count < 1:
                    label1.destroy()
                    label1 = Label(window4, text="")
                    label1.config(text="One Player need to be selected", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)
                else:
                    label1.destroy()
                    label1 = Label(window4, text="")
                    label1.config(text="Select only one player", font="rockwell 15", fg="red")
                    label1.place(x=150, y=430)

        Button(window4, text="PLAY", font="rockwell 15 bold", command=show).place(x=50, y=460)

    window4.mainloop()


def play():
    global overs, team1, team2, onfieldbatting1, onfieldbatting2, onfieldbowling1, onfieldbowling2, frombat, frombowl, Striker, Non_Striker, bowler
    global totalruns, over, balls, extras, scoreone, scoretwo, ballsone, ballstwo, window5, window3, window4, fromplay, fromstrikerone, fromstrikertwo
    if frombat == 1:
        window3.destroy()
    elif frombowl == 1:
        window4.destroy()
    fromstrikerone = 0
    fromstrikertwo = 0
    window5 = Tk()
    window5.geometry('500x550')
    window5.resizable(0, 0)
    window5.configure(bg="cyan")
    window5.title('ScoreCard')
    Label(window5, text="Total score:", font="rockwell 15 bold").place(x=20, y=30)
    Label(window5, text="Wickets:", font="rockwell 15 bold").place(x=250, y=30)
    playerscores2 = {}
    teambat2 = 0
    teambat1 = 0
    playerscores1 = {}
    if tosswon == team1.get():
        if frombat == 1:
            teambat2 = 1
            for i in range(11):
                playerscores2[teamplayers2[i].get()] = [0, 0]
        elif frombowl == 1:
            teambat1 = 1
            for i in range(11):
                playerscores1[teamplayers1[i].get()] = [0, 0]
    elif tosswon == team2.get():
        if frombowl == 1:
            teambat2 = 1
            for i in range(11):
                playerscores2[teamplayers2[i].get()] = [0, 0]
        if frombat == 1:
            teambat1 = 1
            for i in range(11):
                playerscores1[teamplayers1[i].get()] = [0, 0]
    print(playerscores1)
    print(playerscores2)
    labelTotal = Label(window5, text=totalruns.get(), font="rockwell 15")
    labelTotal.place(x=150, y=30)
    labelover = Label(window5, text=str(Over.get()) + "." + str(balls.get()), font="rockwell 15")
    labelover.place(x=150, y=150)
    labelwickets = Label(window5, text=wickets.get(), font="rockwell 15")
    labelwickets.place(x=380, y=30)
    labelbowlerballs = Label(window5, text=str(bowlerover.get()) + "." + str(bowlerballs.get()), font="rockwell 15")
    labelbowlerballs.place(x=380, y=60)
    labelextras = Label(window5, text=extras.get(), font="rockwell 15")
    labelextras.place(x=150, y=120)
    labelscoreone = Label(window5, text=str(scoreone.get()) + "(" + str(ballsone.get()) + ")", font="rockwell 15")
    labelscoreone.place(x=150, y=60)
    labelscoretwo = Label(window5, text=str(scoretwo.get()) + "(" + str(ballstwo.get()) + ")", font="rockwell 15")
    labelscoretwo.place(x=150, y=90)
    labelstrike = Label(window5, text="*", font="rockwell 15")
    labelstrike.place(x=230, y=60)
    global strikerone, strikertwo, batsmen1, batsmen2,fromnoball
    fromnoball=0
    strikerone = 1
    strikertwo = 0
    batsmen1 = onfieldbatting1[0]
    batsmen2 = onfieldbatting1[1]
    Striker = Label(window5, text=batsmen1, font="rockwell 15", fg="white", bg="blue")
    Striker.place(x=20, y=60)
    bowler = Label(window5, text=onfieldbowling1[0], font="rockwell 15")
    bowler.place(x=250, y=60)
    Non_Striker = Label(window5, text=batsmen2, font="rockwell 15", fg="white", bg="blue")
    Non_Striker.place(x=20, y=90)
    Label(window5, text="Extras:", font="rockwell 15 bold").place(x=20, y=120)
    Label(window5, text="Overs:", font="rockwell 15 bold").place(x=20, y=150)

    def ballscheck():
        global fromplay
        if balls.get() < 5:
            balls.set(balls.get() + 1)
            labelover.config(text=str(Over.get()) + "." + str(balls.get()))
            bowlerballs.set(bowlerballs.get() + 1)
            labelbowlerballs.config(text=str(bowlerover.get()) + "." + str(bowlerballs.get()))
        else:
            balls.set(0)
            Over.set(Over.get() + 1)
            labelover.config(text=str(Over.get()) + "." + str(balls.get()))
            strikeRotate()
            bowlerover.set(0)
            bowlerballs.set(0)
            labelbowlerballs.config(text=str(bowlerover.get()) + "." + str(bowlerballs.get()))
            fromplay = 1
            selectbowl()

    def single(n):
        global fromplay, bowler,fromnoball
        if strikerone == 1:
            if fromnoball == 0:
                ballsone.set(ballsone.get() + 1)
            scoreone.set(scoreone.get() + n)
            labelscoreone.config(text=str(scoreone.get()) + "(" + str(ballsone.get()) + ")")
            if n == 1 or n == 3:
                strikeRotate()
            totalruns.set(totalruns.get() + n)
            labelTotal.config(text=totalruns.get())
        elif strikertwo == 1:
            if fromnoball == 0:
                ballstwo.set(ballstwo.get() + 1)
            scoretwo.set(scoretwo.get() + n)
            labelscoretwo.config(text=str(scoretwo.get()) + "(" + str(ballstwo.get()) + ")")
            if n == 1 or n == 3:
                strikeRotate()
            totalruns.set(totalruns.get() + n)
            labelTotal.config(text=totalruns.get())
        if fromnoball==1:
            fromnoball=0
        else:
            ballscheck()

    def wide():
        extras.set(extras.get() + 1)
        labelextras.config(text=extras.get())
        totalruns.set(totalruns.get() + 1)
        labelTotal.config(text=totalruns.get())

    def noBall():
        global fromnoball
        extras.set(extras.get()+1)
        labelextras.config(text=extras.get())
        totalruns.set(totalruns.get() + 1)
        labelTotal.config(text=totalruns.get())
        fromnoball=1

    def out():
        global fromplay,fromnoball, fromstrikerone, fromout, fromstrikertwo, batsmen1, batsmen2, ballsone, ballstwo, balls, bowlerballs, bowlerover, Over
        if fromnoball==0:
            fromplay = 1
            wickets.set(wickets.get() + 1)
            labelwickets.config(text=wickets.get())
            if balls.get() < 5:
                balls.set(balls.get() + 1)
                labelover.config(text=str(Over.get()) + "." + str(balls.get()))
                bowlerballs.set(bowlerballs.get() + 1)
                labelbowlerballs.config(text=str(bowlerover.get()) + "." + str(bowlerballs.get()))
            if strikerone == 1:
                ballsone.set(ballsone.get() + 1)
                '''
                labelout1 = Label(window5, text=batsmen1 + str(scoreone.get()) + "(" + str(ballsone.get()) + ")",
                                  font="rockwell 15")
                labelout1.place(x=30, y=450)
                '''
                if teambat1 == 1:
                    playerscores1[batsmen1] = [ballsone.get(), scoreone.get()]
                elif teambat2 == 1:
                    playerscores2[batsmen1] = [ballsone.get(), scoreone.get()]
                ballsone.set(0)
                scoreone.set(0)
                labelscoreone.config(text=str(scoreone.get()) + "(" + str(ballsone.get()) + ")")
                fromstrikerone = 1
                # Striker.destroy()
                batting()
                batsmen1 = onfieldbatting1[0]
            if strikertwo == 1:
                ballstwo.set(ballstwo.get() + 1)
                '''
                labelout2 = Label(window5,
                                  text=batsmen2 + str(scoretwo.get()) + "(" + str(ballstwo.get()) + ")",
                                  font="rockwell 15")
                labelout2.place(x=30, y=450)
                '''
                if teambat1 == 1:
                    playerscores1[batsmen2] = [ballstwo.get(), scoretwo.get()]
                elif teambat2 == 1:
                    playerscores2[batsmen2] = [ballstwo.get(), scoretwo.get()]
                ballstwo.set(0)
                scoretwo.set(0)
                labelscoretwo.config(text=str(scoretwo.get()) + "(" + str(ballstwo.get()) + ")")
                fromstrikertwo = 1
                # Non_Striker.destroy()
                batting()
                batsmen2 = onfieldbatting1[0]
        else:
            if strikerone==1:
                ballsone.set(ballsone.get()+1)
                labelscoreone.config(text=str(scoreone.get()) + "(" + str(ballsone.get()) + ")")
            elif strikertwo==1:
                ballstwo.set(ballstwo.get()+1)
                labelscoretwo.config(text=str(scoretwo.get()) + "(" + str(ballstwo.get()) + ")")

    def strikeRotate():
        global strikerone, strikertwo
        if strikerone == 1:
            labelstrike.place(x=230, y=90)
            strikerone = 0
            strikertwo = 1
        elif strikertwo == 1:
            labelstrike.place(x=230, y=60)
            strikerone = 1
            strikertwo = 0
        print(playerscores1)
        print(playerscores2)

    Button(window5, text="0", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue",
           command=lambda: single(0)).place(
        x=150, y=200)
    Button(window5, text="1", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue",
           command=lambda: single(1)).place(
        x=150, y=250)
    Button(window5, text="2", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue",
           command=lambda: single(2)).place(
        x=150, y=300)
    Button(window5, text="3", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue",
           command=lambda: single(3)).place(
        x=150, y=350)
    Button(window5, text="4", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue",
           command=lambda: single(4)).place(
        x=150, y=400)
    Button(window5, text="6", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue",
           command=lambda: single(6)).place(
        x=230, y=200)
    Button(window5, text="WD", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue", command=wide).place(
        x=230, y=250)
    Button(window5, text="NB", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue", command=noBall).place(
        x=230, y=300)
    Button(window5, text="OUT", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue", command=out).place(
        x=230, y=350)
    Button(window5, text="SR", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue",
           command=strikeRotate).place(x=230, y=400)
    Button(window5, text="B+", font="rockwell 20", height=1, width=5, bg="blue", fg="lightblue",
           command=ballscheck).place(x=230, y=450)


Button(window, text="TOSS", font="rockwell 15 bold", command=toss, borderwidth=0).place(x=200, y=450)
window.mainloop()
