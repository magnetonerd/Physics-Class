#Program: Stage 1 Project
#Christopher K. Rodgers
#PHYS 310
#Jan 26, 2015
#
#This code is intended to show a ball bouncing up and
#down on a surface. It does so by starting the ball out
#at an initial hight and the proceeds to move the ball
#according to the kinimetic equations of motion.
#Specifically: v = v0 + a*t & r = r0 + v0*t + (1/2)*a*t^2

from visual import*

#Background
floor = box(length = 4, hight = 1, width = 0, color=color.red)

#initial Condisions of the ball
bx = 0 #x-component
by = 5 #y-component
bz = 0 #z-component

#The ball and its velocity
ball = sphere(pos = vector(bx,by,bz), radius = 0.5, color = color.blue)
ball.velocity = vector(0,-1,0)

#This ball is ment to keep the camera angle constant
ball2 = sphere(pos = vector(2,3,-2), radius = 0.5, color = color.green) 

g = 9.8 #acceleration due to gravity
dt = 0.01 #time step

while 1:
    #refresh rate
    rate(100)
    
    #Each of the three following components obain the
    #kinematic equation r = r0 + v0*t + (1/2)*a*t^2
    
    #How the x component of the ball's position beahaves
    #ball.x = ball.x + ball.velocity.x*dt #- 0.5*g*dt**2
    #How the y component of the ball's position beahaves
    ball.y = ball.y + ball.velocity.y*dt #- 0.5*g*dt**2
    #How the z component of the ball's position beahaves
    #ball.z = ball.z + ball.velocity.z*dt #- 0.5*g*dt**2
    #This gets the ball to move up and down
    if(ball.y < 1):
        #send the ball back in the positive direction
        ball.velocity.y = -ball.velocity.y #*exp(-dt)
    else:
        #brings ball back down according to the
        #kinematic equation v = v0 + a*t
        ball.velocity.y = ball.velocity.y - g*dt

#Note1
#I tried multiple variations on the ball.velocity.y variable
#In the first few attempts I tried to stick with the kinematic
#equation v = v0 + a*t, but this lead to the ball slowly getting
#higher in the animation. So, I had to get rid of the acceleration
#term.
#Note2
#I tried to include an exponential damping term in to see what
#Would happen. This lead to the ball slowly losing altitude.
#However, the ball did not stay only in the y direction. It also
#started moving in the negative x direction.
#Note3
#If I use the kinematic equation for position on the ball, then
#the acceleration term will begin to add values to the
#x and z components causing the ball to move in all 3 dimensions.
#Note4
#The acceleration term in the x compnent calculations will dampen
#the ball hight, but after so many iterations the ball will begin
#to just slowly drift down past the background.
