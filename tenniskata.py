import random as rd
from math import *
# def pointstennis(scoreplayer1,scoreplayer2):
#     pointoutcome = rd.randint(1,2)
#     print(pointoutcome)
#     if pointoutcome == 1:
#         scoreplayer1 += 1
#     else:
#         scoreplayer2 += 1
#     print(scoreplayer1,scoreplayer2)

# def scorereader(scoreplayer1,scoreplayer2):
#     goodscore =  



def jeutennis():
    scoreplayer1 = 0
    scoreplayer2 = 0
    while (scoreplayer2 + scoreplayer1 <= 4) or (-2 < scoreplayer1 - scoreplayer2 < 2) :
        pointoutcome = rd.randint(1,2)
        if pointoutcome == 1:
            scoreplayer1 += 1
        else:
            scoreplayer2 += 1
    print(scoreplayer1,scoreplayer2)
    if scoreplayer1 - scoreplayer2 < 2:
        #jeuplayer1 = jeuplayer1 + 1
        print("player1 wins the game")
    else:
        scoreplayer1 - scoreplayer2 < -2
        #jeuplayer2 = jeuplayer2 + 1
        print("player2 wins the game")
jeutennis()  