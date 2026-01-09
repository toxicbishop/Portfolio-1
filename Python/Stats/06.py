import numpy as np 
import matplotlib.pyplot as plt 
def normal_distribution(x, mu, sigma): 
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2) 
def binomial_distribution(n, p, k): 
    from math import comb 
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) 
def poisson_distribution(lmbda, k): 
    from math import exp, factorial 
    return (lmbda ** k * exp(-lmbda)) / factorial(k) 
def bernoulli_distribution(p, k): 
    return p ** k * (1 - p) ** (1 - k) 
mu = 0 
sigma = 1 
n = 10 
p = 0.5 
lmbda = 3
x = np.linspace(-5, 5, 100) 
normal_y = normal_distribution(x, mu, sigma) 
k_values = np.arange(0, n + 1) 
binomial_y = [binomial_distribution(n, p, k) for k in k_values] 
poisson_k_values = np.arange(0, 15) 
poisson_y = [poisson_distribution(lmbda,k) for k in poisson_k_values] 
bernoulli_k_values = [0, 1] 
bernoulli_y = [bernoulli_distribution(p, k) for k in bernoulli_k_values] 
plt.figure(figsize=(12, 8)) 
plt.subplot(2, 2, 1) 
plt.plot(x, normal_y, label='Normal Distribution', color='blue') 
plt.title('Normal Distribution') 
plt.xlabel('X') 
plt.ylabel('Probability Density') 
plt.grid() 
plt.subplot(2, 2, 2) 
plt.bar(k_values, binomial_y, label='Binomial Distribution', color='orange') 
plt.title('Binomial Distribution') 
plt.xlabel('Number of Successes') 
plt.ylabel('Probability') 
plt.grid() 
plt.subplot(2, 2, 3) 
plt.bar(poisson_k_values, poisson_y, label='Poisson Distribution', color='green') 
plt.title('Poisson Distribution') 
plt.xlabel('Number of Events') 
plt.ylabel('Probability') 
plt.grid() 
plt.subplot(2, 2, 4) 
plt.bar(bernoulli_k_values, bernoulli_y, label='Bernoulli Distribution', color='red') 
plt.title('Bernoulli Distribution') 
plt.xlabel('Outcome') 
plt.ylabel('Probability') 
plt.xticks(bernoulli_k_values) 
plt.grid() 
plt.tight_layout() 
plt.show()