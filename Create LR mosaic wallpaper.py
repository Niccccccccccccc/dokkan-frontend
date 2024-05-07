from PIL import Image
import os
from dokkanfunctions import *
import math
directory="data/"
cards=storedatabase(directory,"cards.csv")
createLRWallpapers(cards,directory)
print("Creating LR mosaic")
acquiredlist2 = os.listdir(r'./assets/final_assets')
acquiredlist=[]
for card in cards:
    if qualifyAsLR(card):
        acquiredlist.append("final_"+card[0]+".png")
amount=len(acquiredlist)
screenx=1280
screeny=720
size=screenx+screeny
fitx=0
fity=0
while (fitx*fity)<amount:
    size-=1
    fitx=math.floor(screenx/size)
    fity=math.floor(screeny/size)
print("Each unit will be",size,"x",size)

(width,height)=(screenx,screeny)
cfinal=Image.new("RGBA",(width,height))

print("ordering cards",end=" ")
temp=[]
for x in range(0,len(acquiredlist)):
    temp.append(acquiredlist[x][6:13])
LRcard=[]    
for unit2 in temp:
    for card in cards:
        if card[0]==unit2:
            LRcard+=[card]
LRcard=sortultralist(LRcard,0,True)
LRcard=sortultralist(LRcard,12,True)
LRcard=sortultralist(LRcard,53,False)
acquiredlist=[]
for unit in LRcard:
    temp=("final_")
    temp+=unit[0]
    temp+=(".png")
    acquiredlist.append(temp)
print("completed")


unitnumber=0
for y in range(0,fity):
    for x in range(0,fitx):
        if unitnumber<amount:
            uniturl=("assets/LR wallpapers/")
            uniturl+=(acquiredlist[unitnumber])
            cunit = Image.open(uniturl).convert("RGBA")
            cunit=cunit.resize((size,size))
            xloc=x*size
            yloc=y*size
            cfinal.paste(cunit, (xloc,yloc),cunit)
            unitnumber+=1
cfinal.save("assets/Mosaic wallpapers/LR wallpaper.png")
print("Completed")