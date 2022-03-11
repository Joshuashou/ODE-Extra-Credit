# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import numpy as np
import matplotlib.pyplot as plt

def Lissajous_Curves(a,b):
    x = np.array([])
    y = np.array([])
    t = 0
    maxT = 100
    iteration = 0.01

    while t < maxT:
        x = np.append(x,math.cos(a*t))
        y = np.append(y,math.sin(b*t))

        t += iteration

    return x,y

def plot_curve(x, y,title):
    print(x)
    print(y)
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #First, we want to try iterations where A,B are both integers
    avariation = [1,8]
    bvariation = [1,2,3]
    for a in avariation:
        for b in bvariation:
            curvex,curvey = Lissajous_Curves(a,b)
            title = "Lissajous Curve for integer A and B"
            plot_curve(curvex,curvey,title)
    plt.show()

    #Next, we want to change A,B by factor of lambda to see difference.

    lmb = 0.5 #No matter what I change lambda to, it always stays the same!
    for a in avariation:
        for b in bvariation:
            curvex, curvey = Lissajous_Curves(lmb*a, lmb*b)
            title = "Lissajous Curve for integer A and B multiplied by lmbd = 0.5"
            plot_curve(curvex, curvey, title)
    plt.show()

    #Now, we want to demonstrate for irrational values.
    curvex,curvey = Lissajous_Curves(math.pi, 1)
    title = "Lissajous Curve for A=Pi and B=1"
    plot_curve(curvex,curvey,title)
    plt.show()

    #Finally, I want to check to see if this behavior exists if irrationals are factors of each otehr.
    curvex, curvey = Lissajous_Curves(math.pi, 2*math.pi)
    title = "Lissajous Curve for A=Pi and B=2*pi"
    plot_curve(curvex, curvey, title)
    plt.show()
    #It turns out it's more about the factor between the two numbers.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
