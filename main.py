import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Inputs
S = 98.88 # Initial stock price
mu = 0.215 # Mean return
sigma = 0.15 # Volatility
T = 2 # Time horizon (in years)
dt = 0.25 # Time step size
n_sim = 1000000 # Number of simulations
target_price = 141.45 # Target Price
samsize = 1000 # sample size for plot

# Simulation
returns = np.random.normal(mu*dt, sigma*np.sqrt(dt), (int(T/dt), n_sim))
prices = S*np.cumprod(np.concatenate((np.ones((1, n_sim)), 1+returns), axis=0), axis=0)
#print(prices)
df1 = pd.DataFrame(prices) 
df = df1.sample(n=samsize,axis='columns')  #randomly take 1000 sample to represent 1,000,000 results

df2 = df1.iloc[-1]
df2 = df2[df2 > target_price]
up = len(df2)
down = len(df1.iloc[-1]) - len(df2)
pup = round((up/len(df1.iloc[-1]))*100, 2)
pdown = round(100 - pup, 2)

def count():
  #print("There are {} simulations in {} that result in the end price being higher than {}.".format(up,len(df1.iloc[-1]),target_price))
  print('The stock price reaches the target price ${} in {} of {} ({}% of) simulations.'.format(target_price,up,len(df1.iloc[-1]),pup))
  
count()
# Plot Brownian Motion using sample size
plt.plot(df)
plt.xlabel('Time (Quaters)')
plt.ylabel('Stock Price')
plt.show()

#Histogram using sample size
#plt.hist(df.iloc[-1])
#plt.xlabel('Stock Price')
#plt.ylabel('Density')
#plt.show()

#Scatter plot average of sample size
#average = df.mean(axis=1)
#x1 = list(range(0,9))
#plt.scatter(x1, average)
#plt.show()