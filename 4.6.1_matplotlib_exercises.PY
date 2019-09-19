import matplotlib.pyplot as plt
import pandas as pd
import math
df = pd.read_csv('stock.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()# Plot y = x^2 - x +2 and add annotation for 0,0

x = range(-8,9)
y = [(i**2 - i + 2) for i in x]
plt.plot(x,y,c='blue')
plt.xlim(-3,3)
plt.ylim(0,5)
plt.annotate('Origin', xy=(0, 0), xytext=(1.5, 1.5),arrowprops={'facecolor': 'blue'})
plt.show()

x = range(2,8)
y = [math.sqrt(i) for i in x]
z = [i**3 for i in x]
a = [math.tan(i) for i in x]
b = [pow(2,i) for i in x]

plt.figure(figsize=(5,5))
plt.subplot(2,2,1)

plt.plot(x,y,c='cyan', label='$\sqrt{x}$')
plt.xlim(0,6)
plt.ylim(0,3)
plt.xlabel('$x$',fontsize=10)
plt.ylabel('$y$',fontsize=10)
plt.legend(loc='upper left')


plt.subplot(2,2,2)
plt.plot(x,z,c='red', label='$x^3$')
plt.xlim(0,6)
plt.ylim(0,50)
plt.xlabel('$x$',fontsize=10)
plt.ylabel('$y$',fontsize=10)
plt.legend(loc='upper left')


plt.subplot(2,2,3)
plt.plot(x,a,c='blue',label='$\tan(x)$')
plt.xlim(0,6)
plt.ylim(-20,20)
plt.xlabel('$x$',fontsize=10)
plt.ylabel('$y$',fontsize=10)
plt.legend(loc='upper left')


plt.subplot(2,2,4)
plt.plot(x,b,c='magenta',label='$\ 2^x$')
plt.xlim(0,6)
plt.ylim(0,50)
plt.xlabel('$x$',fontsize=10)
plt.ylabel('$y$',fontsize=10)
plt.legend(loc='upper left')
plt.tight_layout()