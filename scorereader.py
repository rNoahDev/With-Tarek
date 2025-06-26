from math import *
def scorereader(score1,score2):
    newscore1 = fabs(cos(score1*0.5*pi))*15*fabs(cos(score1*0.5*pi))*score1 + fabs(ceil(log10(score1))-1)*15 + cos(score1*pi)*ceil(log10(score1))*40*remainder(score1,2)
    newscore2 = fabs(cos(score2*0.5*pi))*15*fabs(cos(score2*0.5*pi))*score2 + fabs(ceil(log10(score2))-1)*15 + cos(score2*pi)*ceil(log10(score2))*40*remainder(score2,2)
    print(trunc(newscore1),trunc(newscore2))
    

scorereader(1,4)
scorereader(2,4)
scorereader(3,5)
scorereader(4,6)
