
# coding: utf-8

# In[3]:

#Import all package that we need
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.optimize as so
import scipy.integrate as si
#The initial values and small step
x0 = 1
z0=1
y0 = 2
h = 0.1
#Function is return y'
def f(z):
	R=z
	return R

#Function is return z'
def g(x,z):
	A= -2*z/x + 1/x - 1
	return A
  
# function to find values of z and y for a given x using step size h 
# and initial value y0,z0 at x0. 

def rungeKutta(x0, y0, z0, x, h): 
    
    # Count number of iterations using step size or 
    # step height h 
    
	n = (int)((x - x0)/h)  
    # Iterate for number of iterations 
    
	y = y0  # The first y is y0
    
	z=z0    # The first y is y0
    
	for i in range(1, n + 1): 
        
        #"Apply Runge Kutta Formulas to find next value of z and y"
        
		k1=h* f(z)
		L1=h* g(x0,z)
		k2=h*f(z+L1/2)
		L2=h*g(x0+h/2,z+L1/2)
		k3=h*f(z+L2/2)
		L3=h*g(x0+h/2,z+L2/2)
		k4=h*f(z+L3)
		L4=h*g(x0+h,z+L3)
  
        # Update next value of y 
		
		y +=  (1 / 6)*(k1 + 2 * k2 + 2 * k3 + k4) 
      
        # Update next value of y 
        
		z += (1 / 6)*(L1 + 2 * L2 + 2 * L3 + L4)

        # Update next value of x 
		x0 = x0 + h 
		
	return y

# Array all values between 1 and 4 with step size 0.1

x=np.arange(1,4.1,0.1)

#Creation of one array constitute of 0 such that this lenght is the same that x

b=np.zeros(len(x))

#for each x[i], we find a b[i] correspond. b= function rungeKutta

for i in range(len(x)):
    
	b[i]+= rungeKutta(x0, y0, z0, x[i], h)
  
 #Display x and b

print ('The array of t is: ',x)

print('The array of y is:',b)
k = 5/2

q = (-1/6)*x**2 + (1/2)*x - (5/6)/x + k

 #Plot the graph
plt.subplot(2,3,2)
plt.grid()
plt.plot(x,b, 'red')
plt.xlabel('x.axes')
plt.ylabel('b axes')
plt.title('Grap Runge Kutta 4 order')
plt.subplot(2,3,5)
plt.grid()
plt.plot(x,q, 'black')
plt.xlabel('x.axes')
plt.ylabel('q.axes')

 #Show the graph

plt.show()


# In[ ]:
