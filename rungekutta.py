#Runge-Kutta four-order
import numpy as np

def runge_kutta(function, h, y, x):
    K1 = h*function(x,y)
    K2 = h*function(x + 0.5*h, y + 0.5*K1)
    K3 = h*function(x + 0.5*h, y + 0.5*K2)
    K4 = h*function(x + h, y + K3)

    yplus = y + (1.0/6.0)*(K1 + 2*K2 + 2*K3 + K4)
    return yplus

def ed( x, y):
    return -y/(500 * 0.5*1e-6)

def main():
    print("Runge-Kutta DE solver")
    V = 20
    R = 500
    C = 0.5*1e-6

    #initial condition    
    y = V/R

    ti = 0
    tf = 1
    steps = 100
    h = (tf - ti)/steps
    x = np.linspace(ti, tf, steps)

    for i in range(x.size):
        if i == 0:
            continue
        
        
        pass

    print(i)



if __name__ == "__main__":
    main()
