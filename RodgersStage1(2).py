#Program:.Stage_1_Project (Bouncing Ball)
#Coder:...Christopher K. Rodgers
#Class:...PHYS 310
#Date:....Jan 28, 2015
#
#This code is intended to show a ball bouncing up and
#down on a surface. It does so by starting the ball out
#at an initial hight and the proceeds to move the ball
#according to the kinimetic equations of motion.
#Specifically: v = v0 + a*t

from visual import* #Library used in order to do visual effects

#this is the boundary that is used to make the ball bounce off of.
#length defines how far to the left and right the background will extend
#hihght is how much the background extends in the up and down direction
#width is how far backward and forward the background will extend.
#color defines the color of the background. Red in this case
background = box(length = 10,hight = 1,width = 10, color = color.red)
#This is the ball that will be made to bounce up and down.
#pos initialzes the position of the ball on the screen.
#Raduis defines the radius of the ball in the units that the
#call function defines.
#The color of the ball is blue.
ball = sphere(pos = vector(0,4,0),radius = 0.5, color = color.blue)

#It is a good idea to have our system setup so that quick changes can
#be made to the intial conditions of the position of the ball
bx = 0.0 #x-component
by = 4.0 #y-component
bz = 0.0 #z-component

#This is used to set the different components of the ball. This will
#allow for quick changes made to position vector of the ball.
ball.x = bx #Positions to the left and right of center screen
ball.y = by #Positions above and below the center of the screen
ball.z = bz #Positions behind and in front of the center of the screen

vx = 0.0 #x-component of the velocity
vy = -1.0 #y-component of the velocity
vz = 0.0 #z-component of the velocity

ax = 0.0 #x-component of the acceleration
ay = -9.8 #y-component of the acceleration
az = 0.0 #z-component of the acceleration

dt = 0.01 #Step size of the time variable
t = 0.0 #Initialization of the time variable

#This loop insures that the ball will bounce until the window is closed
while t < 1:
    rate(100)#Refresh rate
    t = t + dt #The time at each iteration of the loop

## You have an odd mixture of updating ball position while not tracking
## ball.velocity, but with tracking vx, vy, vz, but not updating x, y, z.
## We want to go to only tracking x, y, z, vx, vy, vz, and then only
## using ball to update the position at the very end (ball.x = x and so on).
    
## Remove ball.x and so forth from the dynamics (see below for updating
## x, y, z).  The ONLY thing we want ball.x to do is to get updated
## from our calculated value of x.  So, at the end of the while loop,
## ball.x = x, ball.y = y, ball.z = z, and that is all.

    #The ball will not bounce unless it is told to do so.
    #The if statement defines the velocity based on the
    #position of the ball.

## Remove ball from this condition, make it if (y < 1):
    if(by < 1):
        #This will keep the ball moving in the same x direction
        #as it was when the ball first started moving.
        vx = vx
        #This sends the ball back up when it reaches the boundary
        #of the background.
        vy = -vy
        #This will keep the ball moving in the same z direction
        #as it was when the ball first started moving.
        vz = vz
        
    else:
        #If the acceleration term is not added into this statement
        #the ball will reach the background and then it will start
        #over at the beginning. So, the acceleration in the y
        #direction term insures that the ball will actually move
        #up and down. Giving the ball the apperance of bouncing.
        vx = vx + ax*dt #x-component of the velocity
        vy = vy + ay*dt #y-component of the velocity
        vz = vz + az*dt #z-component of the velocity
        #The x and z components of the velocity are inserted here
        #for the purpose of future expantion.

    #These are the x,y,z components of the position
    #as defined by the partial kinematic equation:
    bx = bx + vx*dt #new x-component of the ball position
    by = by + vy*dt #new y-component of the ball position
    bz = bz + vz*dt #new z-component of the ball position
    #x = x0 + v*t. The quadratic time term is left out
    #because even though it does simulate the lower
    #new hight, after enough iterations the ball
    #will just stop bouncing and start to just slowly
    #move downward.

    #This is used to ensure an update of the position of the ball.
    ball.x = bx #Positions to the left and right of center screen
    ball.y = by #Positions above and below the center of the screen
    ball.z = bz #Positions behind and in front of the center of the screen

print by
## You need to update the position hre too.  x = x + vx * dt and so on.
## Then, after that, set ball.x = x, ball.y = y, ball.z = z
