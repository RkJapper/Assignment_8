import math
import sys
#Converting binary to decimal
def btod(binary):
    binary1 = binary
    d, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        d = d + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return d
#generating a parity bit
def Par(n):
    p = 0
    while n:
        p = ~p
        n = n & (n - 1)
    return p
# Taking input
z = (input("Enter Binary number"))
b = int(z)
n = btod(b)

if Par(n)==1:
    t=0
else:
    t=1
h=str(t)
#Converting string into list
y = (list(z))
y.append(h)
k=""
g = k.join(y)
#Printing output
print ("Parity bit data : ",g)
l = len(g)
i = 0
#Bit stuffing
while (i < l):
    if(y[i] == '0' and y[i+1] == '1' and y[i+2] == '0'):
        y.insert(i+3,'0')
    i=i+4
#Bit Appending
y.append('0')
y.append('1')
y.append('0')
y.append('1')
c = ""
q = c.join(y)
#Printing Output
print("Transmitting data: ",q)


