from turtle import Turtle
user_score=0
class Score(Turtle):
    
    def __init__(self) :
        super().__init__()
        self.points=user_score          
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.color("white")
        self.write(f"Score: {self.points}",False,"center",('Arial', 20, 'normal'))
        

    def score(self):
        self.clear()
        self.points+=1  
        self.color("white")
        self.write(f"Score: {self.points}",False,"center",('Arial', 20, 'normal'))

    def game_over(self):
        self.penup
        self.home()
        self.hideturtle()
        self.color("white")
        self.write(f"GAME OVER",False,"center",('Arial', 15, 'normal'))
        
        