
def setup():
    size(400,400)
    global pos1
    global pos2
    pos1=0
    pos2=175
def draw():
    background(255)
    global pos1
    global pos2
    rect(pos1,pos2,50,50)
    strokeWeight(4)
    kolor = (0,255,65,84,95,182,231,15,90,11,25,194,111)
    k1=int(random(12))
    k2=int(random(12))
    k3=int(random(12))
    strokeWeight(4)
    stroke(kolor[k3],kolor[k2],kolor[k1])
    pushStyle()
    fill(204, 153, 0)
    fill(kolor[k1],kolor[k2],kolor[k3])
    if mousePressed:
        pos1+=1
        pos2-=1
    if pos1==175 and pos2==0:
        noLoop()
