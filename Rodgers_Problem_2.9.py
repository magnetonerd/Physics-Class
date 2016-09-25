from visual import *
from visual.graph import *
import math

#Coder:.. Christopher Rodgers
#Program: Ball Falling from top of Empire State Building
#Course:. PHYS 310
#Date:... March 27,2015

#This function calulates the derivative of the position as it changes
def velocity(y,g,b):
    #This equation is the velocity of an object in free fall
    #as it travels through air
    v = sqrt((g/b)*(1-math.e**(-2*b*(378.80-y))))
    return v

win=700

vdist = gdisplay(x=0,y=0,ymax=100,width=win,height=win*0.6,
                 xtitle="Position(m)",ytitle="Kinetic Energy(J)")

g = 9.8   #acceleration due to gravity
m = 0.145 #mass of ball

##Some values are exagerated so that the ball can be seen on screen

x = 50.0
y = 378.79 #Height ball starts at
z = 50.0

ball = sphere(pos=vector(x,y,z),radius = 5,color = color.cyan)

Empire_State = box(pos=vector(0,y/2.0,0),length = 20, height = 378.79, width = 20, color = color.red)

D = 2*0.0366 #Diameter of ball

c = 2.2*10**(-1)*D**2 #air resistence constant
b = c/m

dt = 0.01

vx = 0.0
vy = velocity(y,g,b) #Calulating the velocity of the ball
vz = 0.0

t = 0.0

init_potential_energy = m*g*y #Initial potential energy of the ball

result = gcurve(color = color.red)

while (y > 0.002):
    rate(100)
    t = t + dt

    vy = velocity(y,g,b) #New velocity5

    y = y - vy*dt #New position after time dt
    
    ball.y = y #Reminding program that this is the balls position

    Kinetic_Energy = (1.0/2.0)*m*vy**2 #Kinetic energy at velocity vy

    result.plot(pos=(y,Kinetic_Energy))

Total_Energy = init_potential_energy - Kinetic_Energy #Total Energy of the system

print "PE =",init_potential_energy,"KE =",Kinetic_Energy,"Total Energy =",Total_Energy
