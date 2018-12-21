#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#  (make_join2data.py) Generate a random combination of titles and viewer counts, or channels
# this is a simple version of a congruential generator, 
#   not a great random generator but enough  
# --------------------------------------------------------------------------

chans   = ['ABC','DEF','CNO','NOX','YES','CAB','BAT','MAN','ZOO','XYZ','BOB']
sh1 =['Hot','Almost','Hourly','PostModern','Baked','Dumb','Cold','Surreal','Loud']
sh2 =['News','Show','Cooking','Sports','Games','Talking','Talking']
vwr =range(17,1053)

chvnm=sys.argv[1]  #get number argument, if its n, do numbers not channels,

lch=len(chans)
lsh1=len(sh1)
lsh2=len(sh2)
lvwr=len(vwr)
ci=1
s1=2
s2=3
vwi=4
ri=int(sys.argv[3])
for i in range(0,int(sys.argv[2])):  #arg 2 is the number of lines to output

    if chvnm=='n':  #no numuber
        print('{0}_{1},{2}'.format(sh1[s1],sh2[s2],chans[ci]))
    else:
        print('{0}_{1},{2}'.format(sh1[s1],sh2[s2],vwr[vwi])) 
    ci=(5*ci+ri) % lch   
    s1=(4*s1+ri) % lsh1
    s2=(3*s1+ri+i) % lsh2
    vwi=(2*vwi+ri+i) % lvwr
 
    if (vwi==4): vwi=5
