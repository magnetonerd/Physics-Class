#Program:.Final_Project ()
#Coder:...Christopher K. Rodgers
#Class:...PHYS 310
#Date:....Apr 15, 2015
#
#This code is intended to show a ball flying through a
#trajectory in a mist. It does so by starting the ball
#at an initial hight and then proceeds to move the ball
#according to the kinimetic equations of motion.
#Specifically: v = v0 + a*t. Also, the ball will change
#color as the height of the ball varies.

from visual import* #Library used in order to do visual effects
from random import random #Allows the use of the random number generator in python
import math #So that I can use the math.floor function to allow me to define the velocity ranges I want

#This class is used to calculate the arguments of the sine and
#cosine functions of the color change operation at the end of the program.
class color_change:
    #Function for calculating the change in height of ball
    def height(self, velocity, acceleration):
        self.ymax = velocity**2 / (2 * acceleration)
    #Function for calculating the argument of the trig functions
    def theta(self, y_init, ball_height):
        self.angle = (ball_height - y_init) * pi / (2 * (self.ymax - y_init))

##For some reason my ball is not going through an arc anymore
##Not sure why. This happened when I changed from having the
##function print the velocity.

#This function is the implimentation for the improved Euler's Method
def F(x,y,z,vx,vy,vz,t,m,c,k):
    dt = 0.01
    t = t + dt
    Bx = 0.2
    Bz = 0.3
    #Force terms
    Fx = -c*vx
    Fy = -c*vy-m*9.8 + (Bz*vx-Bx*vz)
    Fz = -c*vz
    #The statements that follow are done so that I only had to write one function instead of three
    if(k == 1):
        return Fx     
    if(k == 2):
        return Fy
    if(k == 3):
        return Fz

#############################################################################
#The following code is a modified version of some of the code from the
#example program Gas

#Natoms = 150 #number of particles in the mist
Ratom = 0.3  #radius of particles in the mist
#L=15         #size of box the mist is inside.

#Atoms = []   #List of particles that make up the mist
#poslist = [] #List of positions of the mist particles
#rlist = []   #List of radii the particles in the mist

###########################Setup positions of the red ball###################
#for i in range(Natoms):
#    m_mist = 0.1 #mass of mist particles
#    Lmin = -L
#    Lmax = L
    #The dimensions of the "box" the partilces will distribute over
#    x = Lmin+(Lmax-Lmin)*random()
#    y = Lmax*random()
#    z = Lmin+(Lmax-Lmin)*random()
r = Ratom
##################################initial Position###########################
#    if i == 0:
#        Atoms.append(sphere(pos=(x,y,z),radius=r,color=color.red,
#                            make_trail=True,retain=Natoms))
##################################All particles involved#####################
#    else:
#        Atoms.append(sphere(pos=(x,y,z),radius=r,color=color.red))
#    poslist.append((x,y,z))
#    rlist.append(r)
#############################################################################

#This function is used to define the random velocities of the projectile  
def rand_vel(a):
    #The lists that will store the random numbers that will be used for the velocities
    vals1 = [0]*3001 #vx and vz
    vals2 = [0]*1001 #vy
    values1 = range(0,2000)
    values2 = range(0,1000)
    if(a == 5):
        #Generates the numbers that will be used in the x and z velocities
        for i in values1:
            rand_var1 = 10*random()
            show_num1 = math.floor(rand_var1) + 5
            if((show_num1%2) == 1):
                vals1[i] = show_num1
            else:
                vals1[i] = -show_num1
            return vals1[i]
    if(a == 10):
        #Generates the numbers that will be used in the y velocity
        for i in values2:
            rand_var2 = 10*random()
            show_num2 = math.floor(rand_var2) + 10 #There are ranges for this that the sim doesn't like so the + 10 is used to ensure they aren't uesd
            vals2[i] = show_num2        
            return vals2[i]
        
#setting up camera position
#scene.height = 700
#scene.width = 700
#scene.range = (1,1,1)
#scene.center = (0,10,60)

#Gives 360 lighting to the set
light = local_light(pos=vector(0,40,0),color=color.gray(0.75))

#Calling the Color Change Class
val = color_change()

hopeImright = open("Rodgers ball.txt","w") #Opens a file to write data to

#Makes the headers of the write file.
hopeImright.write("Radius")
hopeImright.write(",")
hopeImright.write("Mass")
hopeImright.write(",")
hopeImright.write("\n")

#this is the boundary that is used to make the ball fly over.
#length defines how far to the left and right the background will extend
#hihght is how much the background extends in the up and down direction
#width is how far backward and forward the background will extend.
#color defines the color of the background. Green in this case
background = box(length = 30,hight = 1,width = 30, color = color.green)

#It is a good idea to have our system setup so that quick changes can
#be made to the intial conditions of the position of the ball
bx = -5.0 #x-component
by = 1.0 #y-component
bz = -5.0 #z-component

#This is the ball that will be made to fly.
#pos initialzes the position of the ball on the screen.
#Raduis defines the radius of the ball in the units that the
#call function defines.
#The color of the ball is blue.
ball = sphere(pos = vector(bx,by,bz),radius = 0.5, color = color.blue)

density_mist = 0.5 #Mist density

R_init = ball.radius #Initial radius of the ball

R = R_init #Setting up the use of R for later values

m_ball_init = 1.0 #Initial mass of the ball

m_ball = m_ball_init #Setting up the use of m_ball for later values

Volume_init = (4.0/3.0)*pi*R_init**3 #Initial volume of the ball
Density_init = m_ball_init*Volume_init #Initial density of the ball

density_ball = 1.0

cube1 = box(pos=vector(5,1.5,-5),length=2,width=2,height=2,color=color.cyan)
cube2 = box(pos=vector(-5,1.5,5),length=2,width=2,height=2,color=color.cyan)

#So that I can have the initial y value saved for later use.
x_init = bx
y_init = by
z_init = bz

#The lists that will store the random numbers that will be used for the velocities
vals1 = [0]*31 #vx and vz
vals2 = [0]*11 #vy

#Ranges for the for loops that are used for velocities
values1 = range(0,20)
values2 = range(0,10)

#Generates the numbers that will be used in the x and z velocities
for i in values1:
    vals1[i] = rand_vel(5)

#Generates the numbers that will be used in the y velocity
for i in values2:
    vals2[i] = rand_vel(10)

values3 = range(0,10)

y_max = 0

for j in range(0,100):
    for i in values3:

        vx = vals1[i]    #x-component of the velocity
        vy = -vals2[i]   #y-component of the velocity
        vz = vals1[i+10] #z-component of the velocity
        vel2 = sqrt((vx**2)+(vy**2))
#        if((vel2 > 15) and (vel2 < 17)):
#            print "vx =",vx,"vy =",vy,"vz =",vz
            #saves the initial y velocity for future use.
        vx_init = vx
        vy_init = vy
        vz_init = vz

        theta = math.atan(abs(vy_init/vx_init))*180/pi #Initial Launch angle

        ax = 2.0 #x-component of the acceleration
        ay = -9.8 #y-component of the acceleration
        az = 2.0 #z-component of the acceleration

        F0_mx = ax
        F0_my = ay
        F0_mz = az

            #Calling the height function in color change
        val.height(vy_init,-ay)

        dt = 0.01 #Step size of the time variable
        t = 0.0 #Initialization of the time variable
        tg = 0.0
            
            #boolen variable to determine when the loop will close.
        state = True

        vel = sqrt(vx**2+vy**2+vz**2) #magnetude of the velocity vector

            #This loop insures that the ball will fly until the window is closed
        while (state == True):
            rate(100)#Refresh rate
            t = t + dt #The time at each iteration of the loop
            tg = tg + dt
                #The ball will not fly unless it is told to do so.
                #The if statement defines the velocity based on the
                #position of the ball.

            m_ball = m_ball + (pi*r**2)*(vel*dt)*density_mist #how the mass of the ball changes as it travels through the mist

            R = (3.0*m_ball/(density_ball*4.0*pi))**(1.0/3.0) #how the radius of the ball changes as it travels through the mist

            ball.radius = R #Setting the radius of the ball again

            c = density_mist*1.55E-4*2*R #how the wind resistance changes as the ball gets bigger

                #Here are the calls for the different components of the original force
            F0x = F(bx,by,bz,vx,vy,vz,t,m_ball,c,1)
            F0y = F(bx,by,bz,vx,vy,vz,t,m_ball,c,2)
            F0z = F(bx,by,bz,vx,vy,vz,t,m_ball,c,3)

                #These are the x,y,z components of the position
                #as defined by the partial kinematic equation:
            bxg = bx + vx*dt #new x-component guess of the ball position
            byg = by + vy*dt #new y-component guess of the ball position
            bzg = bz + vz*dt #new z-component guess of the ball position
                #x = x0 + v*t. The quadratic time term is left out
                #because even though it does simulate the lower
                #new hight, after enough iterations the ball
                #will just stop bouncing and start to just slowly
                #move downward.

            vxg = vx + F0_mx*dt #new x-component guess of the ball velocity
            vyg = vy + F0_my*dt #new x-component guess of the ball velocity
            vzg = vz + F0_mz*dt #new x-component guess of the ball velocity

                #Here are the calls for the guessed compenents of the force
            Fgx = F(bxg,byg,bzg,vxg,vyg,vzg,t,m_ball,c,1)
            Fgy = F(bxg,byg,bzg,vxg,vyg,vzg,t,m_ball,c,2)
            Fgz = F(bxg,byg,bzg,vxg,vyg,vzg,t,m_ball,c,3)        

                #The 1.0 is the mass of the function
            bx = bx + (vx + vxg)*dt/2.0
            by = by + (vy + vyg)*dt/2.0
            bz = bz + (vz + vzg)*dt/2.0
            vx = vx + (F0x + Fgx)*dt/(2.0*1.0)
            vy = vy + (F0y + Fgy)*dt/(2.0*1.0)
            vz = vz + (F0z + Fgz)*dt/(2.0*1.0)

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

                #This is used to ensure an update of the position of the ball.
            ball.x = bx #Positions to the left and right of center screen
            ball.y = by #Positions above and below the center of the screen
            ball.z = bz #Positions behind and in front of the center of the screen

                #In order to keep the ball on the background it is set to its
                #initial conditions. This makes the ball follow a projectile
                #path, and then it restart from the beginning.
            if (abs(bx) > 10.0 or abs(bz) > 10.0):
                bx = x_init
                by = y_init
                bz = z_init
                vx = vx_init
                vy = vy_init
                vz = vz_init
                   #This boolean condition closes out the while loop
                   #it ensures that only one arc is gone through.
                state = False

            if((vy > -0.1) and (vy < 0.1) and (by > 1)):
                y_max = by
                       
                #This changes the color of the ball as it increases in height.
                #When the ball is near the ground it mainly blue, and when it
                #is near its appex it is mainly red.
            val.theta(y_init,by)
            ang = val.angle
            ball.color = (sin(ang), 0.0, cos(ang))

                #This writes to the file defined from above in the open statement
            hopeImright.write(str(theta))
            hopeImright.write(",")
            hopeImright.write(str(by))
            hopeImright.write(",")
            hopeImright.write("\n")

hopeImright.close() #Closes the write file
