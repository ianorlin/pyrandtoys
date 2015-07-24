#!/usr/bin/env python3
import random
import math

random.seed()
def randAngle():
     return random.uniform(0, 2*math.pi)
def randAngleDeg():
     return math.degrees(random.uniform(0, 2*math.pi))

print ("x=", randAngle() , " radians")
print ("y= ", randAngleDeg(), " degrees")

print ("sin(x) = ", math.sin(randAngle()))
 
