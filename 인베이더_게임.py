#인베이더게임

#import
import turtle
import random
import winsound
#화면
ts = turtle.Screen()
ts.bgcolor("black")
ts.title("우주 인베이더")
ts.screensize(20,20)
ts.bgpic("우주.gif")

#플레이어
playerspeed = 12
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.pu()
player.speed(0)
player.setpos(0,-300)
player.setheading(90)
turtle.register_shape("ship.gif")
player.shape("ship.gif")

#플레이어 이동
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -242:
        x = -242
    player.setx(x)
    if not fired:
        bullet.setx(x)
def move_right():
    x = player.xcor()
    x +=playerspeed
    if x > 242:
        x = +242
    player.setx(x)
    if not fired:
        bullet.setx(x)
turtle.onkeypress(move_left,"a")
turtle.onkeypress(move_right,"d")
turtle.listen()
#플레이어공격
fired=False
def fire():
    global fired
    if not fired:
        play_sound("shoot")
        fired = True

    
bulletspeed = 20
bullet = turtle.Turtle()
bullet.color("white")
bullet.pu()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.setpos(0,-290)
turtle.onkey(fire,"space")

#적들
tspeed = 4
step = 30
startx= -242
A=[]

for i  in range(10):
    t=turtle.Turtle()
    t.shapesize(1,1)
    t.color("red")
    t.shape("circle")
    t.pu()
    t.speed(0)
    A.append(t)
    

for i ,t in enumerate(A):
    tstep = startx+step*i
    t.setpos(tstep,300)
def bullet_fire():
     global fired
     if fired:
         y = bullet.ycor()
         y +=bulletspeed
         bullet.sety(y)
         if y > 340:
             fired = False
             bullet.setpos(player.xcor(),-290)
#적공격
enemybullets = []
ebulletspeed = 13


def efire():
    global enemybullets
    ts=random.sample(A,3)
    for i in range(3):
        t=ts[i]
        X=t.xcor()
        ebullet = turtle.Turtle()
        ebullet.ht()
        ebullet.color("yellow")
        ebullet.pu()
        ebullet.setheading(270)
        ebullet.setpos(X,300)
        ebullet.showturtle()
        enemybullets.append(ebullet)
    
#게임오버
gameover_title = turtle.Turtle()
gameover_title.hideturtle()
gameover_title.speed(0)
gameover_title.color("white")
gameover_title.setpos(0,0)
gameover_title.pu()

#sound
def play_sound(sound_name):
    winsound.PlaySound("{}.wav".format(sound_name),winsound.SND_FILENAME)


def enemyattack(enemybullets,p):
    다시공격 =0
    global bullet
   
    for ebullet in enemybullets:
         
         y = ebullet.ycor()
         y -=ebulletspeed
         ebullet.sety(y)
         if 충돌(ebullet,p):
             play_sound("shipexplosion")
             p.ht()
             gameover_title.write("Game over",False,align='center',font=('Arial',34,"normal"))
             gameover_title.showturtle()
             bullet.ht() 
             ebullet.ht()
             enemybullets.remove(ebullet)
             del(ebullet)
             다시공격 += 1
             #continue
         if y <-340:
             ebullet.ht()
             enemybullets.remove(ebullet)
             다시공격 += 1
 
    if 다시공격 == 2:
        
        efire()
             
def 충돌(x,y):
    아무거나 = x.distance(y)
    if 아무거나  <= 20:
        y.ht()

        return True
    return False
        
#점수
score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.pu()
score_pen.setpos(-250,-300)
scorestr = "Score:%s" %score
score_pen.write(scorestr,False,align='left',font=('Arial',14,"normal"))
#점수획득
def 점수획득(score):
    scorestr = "Score:%s" %score
    score_pen.clear()
    score_pen.write(scorestr,False,align='left',font=('Arial',14,"normal"))
    

        
#적들 이동
efire()
while True:
    bullet_fire()
    efire
    enemyattack(enemybullets,player)
    
    
    for t in A:
        if 충돌(bullet,t):
            play_sound("enemykilled")
            A.remove(t)
            del(t)
            score=score+10
            점수획득(score)
            continue
        x = t.xcor()
        x +=tspeed
        t.setx(x)
        if t.xcor() > 242:
            tspeed *= -1
        if t.xcor() < -242:
            tspeed *= -1

            


turtle.done()
