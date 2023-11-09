import numpy as np
g = np.sqrt(9.81)
v = ((g * 100) * (np.tan(30) ** 2)) / (2 * (np.cos(np.pi/3)**2) * (1 - np.tan(30) * np.tan(np.pi/3)))** 0.5
print(v)

h = np.pi / 10
k = np.log(2)*np.log(10)**2 / np.pi**2
e = np.exp(1)
T = 200
ε = 300
n = (2/(np.pi ** 0.5)) * (h / ((k*T) ** (3/2))) * e**-ε/k*T * ε**T/2
print(n)

"""
X = Xo + Vo*x*t 
Y = Yo + Vo*x*t - (gt**2)/2"""



'''EF GF GJ DY GP AC DF AB AN AP 20'''