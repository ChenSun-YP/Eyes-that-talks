import turtle
import time

# x = 887
# y = 111
# turtle.screensize(canvwidth=None, canvheight=None, bg=None)
# image = Image.new("RGB",(x,y))
# f = open('ce.txt')
# for i in range(0,x):
#     for j in range(0,y):
#         l = f.readline()
#         r = l.split(", ")#注意逗号后面有个空格（文本中逗号后面有空格，所以需要分离）
#         image.putpixel((i,j),(int(r[0]),int(r[1]),int(r[2])))
# im.save('image1.jpg')
#
import time
import turtle

#sets screen characteristics
wn=turtle.Screen()
wn.bgcolor('black')
wn.title('eye')
wn.colormode(255)
#sets turtle characteristics
greg = turtle.Turtle()
greg.speed(0)
#强化一个rgb值
def colorconvert(r):
    a=1.2
    b=60

    color=r*a+b
    if color>255:
        color=255
    elif color<0:
        color=0

    return int(color)

#draws and fills one square
def square(size,r,g,b):
    wn.tracer(0) #with update below
    greg.color(r,g,b)
    greg.begin_fill()
    for i in range(4):
        greg.fd(size)
        greg.lt(90)

    greg.end_fill()
    greg.fd(size)
    wn.update()#

#draws the whole chessboard 10*10
def chessboardnew(size,R,G,B):
    #greg.home()
    greg.setx(-300)
    greg.sety(200)
    for i in range(10):
        greg.setx(-300)
        greg.sety(200+(-50)*i)
        for j in range(10):
            print(10*i+j)
            square(size,R[10*i+j],G[10*i+j],B[10*i+j])
            print(greg.pos(),R[10*i+j],G[10*i+j],B[10*i+j])
            
        #greg.setx(-300)
        #greg.sety(200+(-50)*i)
    #background
def highlight(tempo,size,R,G,B):
    print('---------------------------------------')
    print('---------------------------------------')

    tempo = float(input("Input your TEMPO and start!!:"))
    time_left = 10
    while time_left > 0:
        print(time_left)
        time.sleep(1)
        time_left = time_left - 1
    greg.up()
    greg.setx(-300)
    greg.sety(200)
    greg.down()
    for i in range(10):
        greg.setx(-300)
        greg.sety(200+(-50)*abs(i))
        greg.down()
        for j in range(10): 
            square(size,colorconvert(R[10*i+j]),
            colorconvert(G[10*i+j]),colorconvert(B[10*i+j]))
            greg.setx(greg.xcor()-50)
            time.sleep(tempo)
            square(size,R[10*i+j],G[10*i+j],B[10*i+j])
        greg.up()


        #greg.setx(-300)
        #greg.sety(200+(-50)*abs(i))
def chessboard(size,RH,GH,BH):
    greg.pu()
    greg.goto(-(size*4),size*4)
    
    
    for i in range(3):
        for j in range(3):
            if(listOfValues[i][j] == 1 ):
                square(size,92,9,3)#预设颜色1
            else:
                square(size,92,9,3)#预设颜色1
        greg.rt(90)
        greg.lt(90)
        greg.goto(-(size*(4)),(size*(4 - i - 1)))
    greg.pu()
    greg.goto(-(size*4),(size*4))
    
    #greg.goto(-(size*4),(size*4))
    for i in range(3):
        for j in range(3):
            time.sleep(0.5)
            if(listOfValues[i][j] == 1 ):
                square(size,colorconvert(92),colorconvert(17),colorconvert(0))#preset3
            else:
                square(size,colorconvert(92),colorconvert(17),colorconvert(0))#preset3
        greg.rt(90)
        greg.lt(90)
        greg.goto(-(size*(4)),(size*(4 - i - 1)))
if __name__ == "__main__":
    listOfValues=[[2,1,1],[1,2,1],[2,1,2]]
    chessboardnew(50,[100,100],[100,100],[120,120])
    #chessboard(50)
