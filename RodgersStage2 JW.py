#Program:.Stage_1_Project (Bouncing Ball)
#Coder:...Christopher K. Rodgers
#Class:...PHYS 310
#Date:....Jan 28, 2015
#
#This code is intended to show a ball flying through a
#trajectory on a surface. It does so by starting the ball
#at an initial hight and then proceeds to move the ball
#according to the kinimetic equations of motion.
#Specifically: v = v0 + a*dt

### and x = x + v*dt

from visual import* #Library used in order to do visual effects

hopeImright = open("Rodgers Altitude.dat","w") #Opens a file to write data to

#Makes the headers of the write file.
hopeImright.write("Time")
hopeImright.write(",")
hopeImright.write("Altitude")
hopeImright.write(",")
hopeImright.write("\n")

#this is the boundary that is used to make the ball fly over.
#length defines how far to the left and right the background will extend
#hihght is how much the background extends in the up and down direction
#width is how far backward and forward the background will extend.
#color defines the color of the background. Red in this case
background = box(length = 10,hight = 1,width = 10, color = color.red)
#This is the ball that will be made to fly.
#pos initialzes the position of the ball on the screen.
#Raduis defines the radius of the ball in the units that the
#call function defines.
#The color of the ball is blue.
ball = sphere(pos = vector(-5,1,-5),radius = 0.5, color = color.blue)

cube1 = box(pos=vector(4,1.5,-4),length=2,width=2,height=2,color=color.cyan)
cube2 = box(pos=vector(-4,1.5,4),length=2,width=2,height=2,color=color.cyan)

### I like the cubes.  Nice use of color, and adds some perspective to the
### motion.

#It is a good idea to have our system setup so that quick changes can
#be made to the intial conditions of the position of the ball
bx = -5.0 #x-component
by = 1.0 #y-component
bz = -5.0 #z-component

#This is used to set the different components of the ball. This will
#allow for quick changes made to position vector of the ball.
ball.x = bx #Positions to the left and right of center screen
ball.y = by #Positions above and below the center of the screen
ball.z = bz #Positions behind and in front of the center of the screen

vx = 3.0 #x-component of the velocity
vy = -10.0 #y-component of the velocity
vz = 3.0 #z-component of the velocity

### I changed the initial vx and vz, in order to make it bounce before
### it reaches the edge, just to see.


ax = 0.0 #x-component of the acceleration
ay = -9.8 #y-component of the acceleration
az = 0.0 #z-component of the acceleration

dt = 0.01 #Step size of the time variable
t = 0.0 #Initialization of the time variable

#This loop insures that the ball will fly until the window is closed
while True:
    rate(100)#Refresh rate
    t = t + dt #The time at each iteration of the loop

    #The ball will not fly unless it is told to do so.
    #The if statement defines the velocity based on the
    #position of the ball.

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
### are you sure you do not want to ahve vz = vz + az*dt here too?
### If bounced in the y, it might still accelerate in the z....

        
    else:
        #If the acceleration term is not added into this statement
        #the ball will reach the background and then it will start
        #over at the beginning. So, the acceleration in the y
        #direction term insures that the ball will actually move
        #through a trajectory. Giving the ball the apperance of projectile.
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

    #In order to keep the ball on the background it is set to its
    #initial conditions. This makes the ball follow a projectile
    #path, and then it restart from the beginning.
    if (bx > 5.0):
        bx = -5.0
        by = 1.0
        bz = -5.0
        vx = 5.0
        vy = -10.0
        vz = 5.0
### This does so only in the x direction, you could make it a combo
### if OR condition for reaching edge of bx OR bz.


    #This writes to the file defined from above in the open statement
    hopeImright.write(str(t))
    hopeImright.write(",")
    hopeImright.write(str(by))
    hopeImright.write(",")
    hopeImright.write("\n")

hopeImright.close() #Closes the write file
