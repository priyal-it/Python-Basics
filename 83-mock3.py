'''a square metal plate in 20 space is the setup we are going tow ork with. The spatial extent of the metal plate is given by

0<=x, y<=5

The temperature at any point (x,y) on the plate is given by the following equation. The temperature is measured in Celsius and can be negative.

f(x,y) = 30 + x**2 + y**2 - 3x - 4y

A micro-organism lives on the surface of the metal plate. It occupies only those points on the plate where both the coordinates are integers. The organism can survive only in those regions where the temperature lies in the range [low, high], end-points inclusive. If no such region is found, it can't survive. Here, low and high are integers.

Accept the value low as input in the first line and high as input in the second line. Print all those coordinates where the organism can survive. The values should be printed in assembly order of x-coordinate. For the same x-coordinate, the values should be printed in ascending order of y-coordinate. At the end, print YES if the organism can survive and No otherwise. Note that the organism can survive only if there is at least one point on the metal plate where the temperature is within the given range. Each line should be printed as x,y. Avoid any spaces anywhere in the line.
'''

low=int(input())
high=int(input())

for x in range(0,6):
    for y in range(0,6):
        if low<(30 + x**2 + y**2 - 3*x - 4*y) and high>(30 + x**2 + y**2 - 3*x - 4*y):
            print(str(x),",",str(y))
            flag=True
    if flag==True:
        print("Yes")
    else:
        print("No")