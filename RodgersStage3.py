#Program:.Stage_3_Project (Color Change with Altitude)
#Coder:...Christopher K. Rodgers
#Class:...PHYS 310
#Date:....Feb 18, 2015
#
#This code is intended to show a ball flying through a
#trajectory on a surface. It does so by starting the ball
#at an initial hight and then proceeds to move the ball
#according to the kinimetic equations of motion.
#Specifically: v = v0 + a*t. Also, the ball will change
#color as the height of the ball varies.

from visual import* #Library used in order to do visual effects

#This class is used to calculate the arguments of the sine and
#cosine functions of the color change operation at the end of the program.
class color_change:
    #Function for calculating the change in height of ball
    def height(self, velocity, acceleration):
        self.ymax = velocity**2 / (2 * acceleration)
    #Function for calculating the argument of the trig functions
    def theta(self, y_init, ball_height):
        self.angle = (ball_height - y_init) * pi / (2 * (self.ymax - y_init))

#setting up camera position
scene.height = 700
scene.width = 700
scene.range = (1,1,1)
scene.center = (0,10,45)

#Gives 360 lighting to the set
light = local_light(pos=vector(0,40,0),color=color.gray(0.75))

#Calling the Color Change Class
val = color_change()

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
#color defines the color of the background. Green in this case
background = box(length = 40,hight = 1,width = 40, color = color.green)
#This is the ball that will be made to fly.
#pos initialzes the position of the ball on the screen.
#Raduis defines the radius of the ball in the units that the
#call function defines.
#The color of the ball is blue.
ball = sphere(pos = vector(-5,1,-5),radius = 0.5, color = color.blue)

cube1 = box(pos=vector(5,1.5,-5),length=2,width=2,height=2,color=color.cyan)
cube2 = box(pos=vector(-5,1.5,5),length=2,width=2,height=2,color=color.cyan)

#It is a good idea to have our system setup so that quick changes can
#be made to the intial conditions of the position of the ball
bx = -5.0 #x-component
by = 1.0 #y-component
bz = -5.0 #z-component

y_init = by

#This is used to set the different components of the ball. This will
#allow for quick changes made to position vector of the ball.
ball.x = bx #Positions to the left and right of center screen
ball.y = by #Positions above and below the center of the screen
ball.z = bz #Positions behind and in front of the center of the screen

vx = 5.0 #x-component of the velocity
vy = -18.0 #y-component of the velocity
vz = -10.0 #z-component of the velocity

vy_init = vy

ax = 0.0 #x-component of the acceleration
ay = -9.8 #y-component of the acceleration
az = 0.0 #z-component of the acceleration

#Calling the height function in color change
val.height(vy_init,-ay)

#These values are used to figure out where the ball will be at
#when it reaches the end of its trajectory. This is information
#is then used later on in an if statement to tell the program
#what to do with the ball at that point.
time_flight = 2 * vy_init / ay
x_final = bx + vx * time_flight + (1.0/2.0) * ax * time_flight**2
z_final = bz + vz * time_flight + (1.0/2.0) * az * time_flight**2

dt = 0.01 #Step size of the time variable
t = 0.0 #Initialization of the time variable

n = 0

#This loop insures that the ball will fly until the window is closed
while n < 4:
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
    if (abs(bx) > abs(x_final) or abs(bz) > abs(z_final)):
        bx = -5.0
        by = 1.0
        bz = -5.0
        vx = 5.0
        vy = -20.0
        vz = 5.0
        #n is the number of times this if statement is true.
        #it is used to determine the number of iterations of
        #of the while loop.
        n = n + 1

    #This changes the color of the ball as it increases in height.
    #When the ball is near the ground it mainly blue, and when it
    #is near its appex it is mainly red.
    val.theta(y_init,by)
    ang = val.angle
    ball.color = (sin(ang), 0.0, cos(ang))

    #This writes to the file defined from above in the open statement
    hopeImright.write(str(t))
    hopeImright.write(",")
    hopeImright.write(str(by))
    hopeImright.write(",")
    hopeImright.write("\n")

hopeImright.close() #Closes the write file
