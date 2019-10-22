width=500  #larghezza campo
height=440
xpalla=100
ypalla=120
x2=1
y2=1
xrettangolo=((width/2)-25)
yrettangolo=(height-25)
hrettangolo=25
lrettangolo=80
lrettangolo2=80
hrettangolo2=25
xrettangolo2=((width/2)-25)
yrettangolo2=0



def setup():
    size(500,440)
    background(0,0,255)
    stroke(0,255,0)
def draw():
    global xpalla,ypalla,x2,y2,xrettangolo,yrettangolo
    background(255,255,255)
    ellipse(xpalla,ypalla,50,50)
    rect(xrettangolo,yrettangolo,lrettangolo,hrettangolo)
    rect(xrettangolo2,yrettangolo2,lrettangolo2,hrettangolo2)
    xpalla+=3*(x2)
    ypalla+=3*(y2)
    if xpalla>=width or xpalla<0:
       x2*= -1
       fill(random(255),random(255),random(255))
    if ypalla>= height or ypalla<0:
       y2*= -1
       fill(random(255),random(255),random(255))
    if lrettangolo>=width and xrettangolo>=height :
        xrettangolo+=0
        yrettangolo+=0
    if ypalla+25>height-25 and xpalla>=xrettangolo and xpalla<=yrettangolo :
        y2*= -1
   
   
    
def keyPressed():
    global xrettangolo,yrettangolo,width,height,y2,x2,x,xrettangolo2,yrettangolo2
    circonferenza=ypalla+25
    if keyCode == RIGHT and xrettangolo<width-lrettangolo:        
        xrettangolo+=15
    if keyCode == LEFT and xrettangolo>0:
        xrettangolo-=15
    if key == "a" and xrettangolo2>0:
        xrettangolo2-=15
    if key == "d" and xrettangolo2>0:
        xrettangolo2+=15
    if ypalla+25>=yrettangolo2+25 and xpalla>=xrettangolo2 and xpalla<=yrettangolo2+25 :
        y2*= -1
       
  
   
    

    
