import random

def gamerules(my_move, comp_move):
    global compscore
    global myscore
    global scorecard

    if my_move == "r":       
        if comp_move == "p":
            uploss = int(eval("0"))
            upwin = int(eval("1"))
            compscore = compscore + upwin
            myscore = myscore + uploss
            scorecard.update({str(myscore):str(compscore)})
            a = scorecard.items()
            a1 = list(a)
            a2 = a1[len(a1)-1]
            a3 = list(a2)
            print(f"Computer wins and the score is {a3[0]}:{a3[1]}")
            return scorecard
        elif comp_move == "s":
            uploss = int(eval("0"))
            upwin = int(eval("1"))
            compscore = compscore + uploss
            myscore = myscore + upwin
            scorecard.update({str(myscore):str(compscore)})
            a = scorecard.items()
            a1 = list(a)
            a2 = a1[len(a1)-1]
            a3 = list(a2)
            print(f"You win and the score is {a3[0]}:{a3[1]}")
            return scorecard
        elif comp_move == "r":
            uploss = int(eval("0"))
            upwin = int(eval("1"))
            compscore = compscore + uploss
            myscore = myscore + uploss
            scorecard.update({str(myscore):str(compscore)})
            a = scorecard.items()
            a1 = list(a)
            a2 = a1[len(a1)-1]
            a3 = list(a2)
            print(f"Draw and the score is {a3[0]}:{a3[1]}")
            return scorecard

        else:
            pass

    if my_move == "p":
        if comp_move == "s":
            uploss = int(eval("0"))
            upwin = int(eval("1"))
            compscore = compscore + upwin
            myscore = myscore + uploss
            scorecard.update({str(myscore):str(compscore)})
            a = scorecard.items()
            a1 = list(a)
            a2 = a1[len(a1)-1]
            a3 = list(a2)
            print(f"Computer wins and the score is {a3[0]}:{a3[1]}")
            return scorecard
        elif comp_move == "r":
            uploss = int(eval("0"))
            upwin = int(eval("1"))
            compscore = compscore + uploss
            myscore = myscore + upwin
            scorecard.update({str(myscore):str(compscore)})
            a = scorecard.items()
            a1 = list(a)
            a2 = a1[len(a1)-1]
            a3 = list(a2)
            print(f"You win and the score is {a3[0]}:{a3[1]}")
            return scorecard
        elif comp_move == "p":
            uploss = int(eval("0"))
            upwin = int(eval("1"))
            compscore = compscore + uploss
            myscore = myscore + uploss
            scorecard.update({str(myscore):str(compscore)})
            a = scorecard.items()
            a1 = list(a)
            a2 = a1[len(a1)-1]
            a3 = list(a2)
            print(f"Draw and the score is {a3[0]}:{a3[1]}")
            return scorecard

        else:
            pass

    if my_move == "s":
        if comp_move == "r":
            uploss = int(eval("0"))
            upwin = int(eval("1"))
            compscore = compscore + upwin
            myscore = myscore + uploss
            scorecard.update({str(myscore):str(compscore)})
            a = scorecard.items()
            a1 = list(a)
            a2 = a1[len(a1)-1]
            a3 = list(a2)
            print(f"Computer wins and the score is {a3[0]}:{a3[1]}")
            return scorecard
        elif comp_move == "p":
            uploss = int(eval("0"))
            upwin = int(eval("1"))
            compscore = compscore + uploss
            myscore = myscore + upwin
            scorecard.update({str(myscore):str(compscore)})
            a = scorecard.items()
            a1 = list(a)
            a2 = a1[len(a1)-1]
            a3 = list(a2)
            print(f"You win and the score is {a3[0]}:{a3[1]}")
            return scorecard
        elif comp_move == "s":
            uploss = int(eval("0"))
            upwin = int(eval("1"))
            compscore = compscore + uploss
            myscore = myscore + uploss
            scorecard.update({str(myscore):str(compscore)})
            a = scorecard.items()
            a1 = list(a)
            a2 = a1[len(a1)-1]
            a3 = list(a2)
            print(f"Draw and the score is {a3[0]}:{a3[1]}")
            return scorecard

        else:
            pass


choice1 = ["r", "p", "s"]
scorecard = {"-1":"-1"}
compscore = 0
myscore = 0

for key, val in list(scorecard.items()):
    while ('3','0') not in list(scorecard.items()) and  ('3','1') not in list(scorecard.items()) and ('3','2') not in list(scorecard.items()) and ('0','3') not in list(scorecard.items()) and ('1','3') not in list(scorecard.items()) and ('2','3') not in list(scorecard.items()):
        comp_move = random.choice(choice1).lower()
        my_move = input("Play your move \n r for rock \t p for paper \t s for scissors \n").lower()
        gamerules(my_move, comp_move)

    a = scorecard.items()
    a1 = list(a)
    a2 = a1[len(a1)-1]
    a3 = list(a2)
    break

if int(a3[0]) < int(a3[1]):
    print(f"GAME OVER! Computer wins and the final score is {a3[0]}:{a3[1]}")

else:
    print(f"GAME OVER! You win and the final score is {a3[0]}:{a3[1]}")
