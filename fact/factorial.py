#!/usr/bin/env python3
# math
x = int(input("Enter a number: "))
f= 1
for i in range(1, x+1):
    f = f * i
print(str(x) + '! = ' + str(f))