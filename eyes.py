#!/usr/bin/python
#!/usr/bin/env python
from mido import Message, MidiFile, MidiTrack,bpm2tempo
#import testimage
import cv2
import present
import time
import os

# the oringinal testimage
def convert(string):  # 把不足三位数的rgb值添上0
    if len(string)== 1:
        string ='00'+string
    elif len(string) == 2 :
        string = '0'+string
    return string
def fuckoff():
    

    request = input('PROVIDE IMAGE:')
    R,G,B=imageToMusic(request)
    if input('press 1 if you want me to print it out') == '1':
        print('R is')
        showR=""
        for i in range (len(R)):
            if i%3==2:
                showR+=R[i]
                showR+=","
            else:
                showR+=R[i]
        print(showR)
                
        print('G is')
        showG=""
        for i in range (len(G)-1):
            if i%3==2:
                showG+=G[i]
                showG+=","
            else:
                showG+=G[i]
        print (showG)
                
        print('B is')
        
        showB=""
        for i in range (len(B)-1):
            if i%3==2:
                showB+=B[i]
                showB+=","
            else:
                showB+=B[i]
        print (showB)


def imageToMusic(address):
    img = cv2.imread(address)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    count=0
    Rwhole=[]
    Gwhole=[]
    Bwhole=[]
    R=''
    G=''
    B=''
    for i in range(img.shape[0]):
        for y in range(img.shape[1]):
            Rwhole.append(img[i,y][0])
            Gwhole.append(img[i,y][1])
            Bwhole.append(img[i,y][2])
            
            
            R+=convert(str(img[i,y][0]))
            G+=convert(str(img[i,y][1]))
            B+=convert(str(img[i,y][2]))
            count+=1
      
    print('there are ',count,'pixels loaded')
    return R,G,B,Rwhole,Gwhole,Bwhole # 一次性全返回
 







    
mid = MidiFile()
#创建音轨
trackR = MidiTrack()
trackG = MidiTrack()
trackB = MidiTrack()
#apply音轨 R G B
mid.tracks.append(trackR)
mid.tracks.append(trackG)
mid.tracks.append(trackB)

tra = [trackR,trackG,trackB]

def Num(yin):                    
    if yin == "0":           
        return 0
    if yin == "1":          
        return 60
    if yin == "2":           
        return 62
    if yin == "3":          
        return 64
    if yin == "4":          
        return 65
    if yin == "5":             
        return 67
    if yin == "6":          
        return 69
    if yin == "7":          
        return 71
    if yin == "8":          
        return 72
    if yin == "9":          
        return 74
def guNum(yin):                    
    if yin == "0":          
        return 0
    if yin == "1":      
        return 37
    if yin == "2":          
        return 24
    if yin == "3":           
        return 21
    if yin == "4":              
        return 22
    if yin == "5":          
        return 14
    if yin == "6":          
        return 18
    if yin == "7":          
        return 46
    if yin == "8":             
        return 38
    if yin == "9":          
        return 23
def yin(yin,pai,qian=0,qi=2,unit=trackR,tong=0,liang=100):
    if type(yin)== str:
        yin = Num(yin) #整体调音
    #unit.append(Message('program_change',channel=0,program=qi,time=0))  # 默认钢琴（2）
    unit.append(Message('note_on', note=yin, velocity=liang, time=qian,channel=tong))  #音开始
    unit.append(Message('note_off', note=yin, velocity=liang, time=pai,channel=tong))
def guYin(yin,pai,qian=0,qi=2,unit=trackR,tong=0,liang=100):
    if type(yin)== str:
        yin = guNum(yin) + 10 #整体改鼓 
    #unit.append(Message('program_change',channel=0,program=qi,time=0))  # 默认钢琴（2）
    unit.append(Message('note_on', note=yin, velocity=liang, time=qian,channel=tong))  #音开始
    unit.append(Message('note_off', note=yin, velocity=liang, time=pai,channel=tong))

def compose(puzi,pai,track,instrument=2,velocity=64,type = 'keyboard'):
    if type == 'keyboard':
        for item in puzi:
            yin(item,pai,unit=track,liang=velocity,qi=instrument)
    else:
        for item in puzi:
            guYin(item,pai,unit=track,liang=velocity,qi=instrument)

if __name__=="__main__":

    os.system("""osascript -e 'tell app "GarageBand" to open'""")
    
    #正文        
    R,G,B,RH,GH,BH = imageToMusic(input('PROVIDE IMAGE:'))

    #倒计时
    sum = 10         # 设置倒计时时间
    timeflush = 0.25  # 设置屏幕刷新的间隔时间
    for i in range(0, int(sum/timeflush)):
        list = ["\\", "|", "/", "—"]
        index = i % 4
        print("\r{}".format(list[index]), end="")
        time.sleep(timeflush)
            
    print(RH)
    print(GH)
    print(BH)
    #fuckoff()
    trackR.append(Message('program_change',channel=4,program=0,time=0))#定义R的乐器
    compose(R,400,trackR,instrument = 2)#作曲R
    trackG.append(Message('program_change',channel=0,program=1,time=0))#定义G的乐器
    compose(G,400,trackG,velocity=30,instrument = 4)#作曲G
    trackB.append(Message('program_change',channel=7,program=2,time=0))#定义B的乐器
    compose(B,400,trackB,velocity=40,instrument = 6,type='drum')#作曲B

    #导出文件为 midi
    mid.save('p3p3.mid')
    print('.jpg has become .midi, go check it out!')





    if input("press 1 to start") == "1":
        present.chessboardnew(50,RH,GH,BH)
        present.highlight(0.3,50,RH,GH,BH)
     

