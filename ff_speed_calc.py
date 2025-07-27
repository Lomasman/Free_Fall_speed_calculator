import math

#<><><>   FREE FALL SPEED CALCULATOR    <><><>#
#   Everything is in SI units

H = float(input("What height is the object falling from: "))    #   Height the object will fall from
i = float(input("resolution - increment of each fall segment: "))   #   Fall distance of each fall increment
k = float(input("What is drag coefficient of the object, 0.5*C*A: "))   #   Drag coef of the object, 0.5CA
h = 0   #   distance fell from the jumping point
R = 6378000 #   radius of Earth
u = 0   #   initial speed of the diver at the start of a fall segment
v = 0   #   final speed of the diver at the end of a fall segment
a = 0   #   approx. constant acceleration during the fall segment
t = 0   #   time of the fall segment
T = 0   #   Variable to add the time of the previous fall segments
p = 0   #   approx air density for that fall segment
Fd = 0  #   air drag on the diver for the segment
Fg = 0  #   gravitational force for the segment
M = 5.97 * pow(10, 24)  #   Mass of Earth
m = float(input("Mass of the falling object: "))    #   mass of diver
G = 6.67 * pow(10, -11)

while h < H:
    Fg = (G * M * m)/pow((R + 5000 - h), 2) #   Fg = GMm/r^2 -> Newton's Law of Gravitation
    p = (-0.11893 * pow((h/1000), 0.883936)) + 1.22637  #   Density of air with altitude, formula is rough estimate I got from desmos
    Fd = k * p * pow(u, 2)  #   Fd = 0.5CApv^2
    a = (Fg - Fd)/m     #   F = ma
    v = math.sqrt(pow(u, 2) + 2 * a * i)    #   v^2 = u^2 + 2as
    t = (v - u)/a   #   v = u + at
    T += t
    u = v
    h += i

print("Time for the fall: " + str(T) + " s")
print("Final speed of the fall:" + str(v) + " m/s")






#### Junk by LOMAS ####