#Runge-Kutta four-order
import numpy as np
import matplotlib.pyplot as plt

V = 50
R = 5000
C = 5.200*1e-6

Npoints = 250 #points to plot

#initial condition
y = []    
y.append(V/R)

ti = 0
tf = .5
steps = 750
h = (tf - ti)/steps
x = np.linspace(ti, tf, steps)

def runge_kutta(function, h, y, x):
    K1 = h*function(x,y)
    K2 = h*function(x + 0.5*h, y + 0.5*K1)
    K3 = h*function(x + 0.5*h, y + 0.5*K2)
    K4 = h*function(x + h, y + K3)

    yplus = y + (1.0/6.0)*(K1 + 2.0*K2 + 2.0*K3 + K4)
    return yplus

def function( x, y):
    return -y/(R * C)

def main():
    print("Runge-Kutta DE solver")

    for i in range(x.size):
        if i == 0:
            # initial condition
            continue
        else:
            y.append( runge_kutta(function, h, y[i-1], x[i-1]) )

    xplot = x[0:Npoints]
    yplot = y[0:Npoints]
    
    # plot solution
    plt.plot(xplot, yplot,"r-.")
    plt.grid(b=True, which='major', color='g', linestyle='--')
    plt.ylabel("Current (A)")
    plt.xlabel("time (s)")
    plt.title("RC circuit R={Res}, Capacitance = {Cap}, Voltage = {Volt}".format(Res=R, Cap=C, Volt=V))
    #plt.xscale("log")
    plt.show()



if __name__ == "__main__":
    main()
