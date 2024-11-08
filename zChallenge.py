#!python3
# Explain what this code does

import random
x = []
for i in range(40):
    if random.randint(0,1):
        x.append(random.randint(1,10))
    else:
        x.append(random.randint(1,10) + random.randint(1,10)/10)

print(x)
#  x are 40 random number from 1,10,and x have half chance to be a integer and half chance to be a float.

