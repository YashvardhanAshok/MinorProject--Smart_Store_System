import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean = 0
std_dev = 1

x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)

pdf = norm.pdf(x, mean, std_dev)

plt.figure(figsize=(10, 6))
plt.plot(x, pdf, label=f'Normal Distribution\nMean = {mean}, Std Dev = {std_dev}')
plt.title('Normal Distribution Curve')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()