from turtle import Turtle,Screen
up=90
down=270
left=180
right=0
names=['s1','s2','s3']
position=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.list=[]
        for i in position:
            a=Turtle()
            a.penup()
            a.color("white")
            a.shape("square")
            a.goto(i)
            self.list.append(a)
        self.head=self.list[0]    

    def Smove(self):    
        for i in range(len(self.list)-1,0,-1):
            pos=self.list[i-1].pos()
            self.list[i].goto(pos)
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=down:
            self.head.seth(up)
    
    def down(self):
        if self.head.heading()!=up:
            self.head.seth(down)

    def left(self):
        if self.head.heading()!=right:
            self.head.seth(left)

    def right(self):
        if self.head.heading()!=left:       
            self.head.seth(right) 

    def extend(self):       
        self.increase_size(self.list[-1].position())

    def increase_size(self,posi):
            a=Turtle()
            a.penup()
            a.color("white")
            a.shape("square")
            a.goto(posi)
            self.list.append(a)
            

    
                                

