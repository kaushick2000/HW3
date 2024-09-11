import time
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

def fun_original(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x = x + 1
    return x

def fun_modified(n):
    x = 1
    y = 1
    for i in range(n):
        for j in range(n):
            x = x + 1
            y = i + j
    return x


ns = list(range(1, 10001, 500))
times_original = []
times_modified = []

for n in ns:
    # Timing the original function
    start = time.time()
    fun_original(n)
    end = time.time()
    times_original.append(end - start)

    # Timing the modified function
    start = time.time()
    fun_modified(n)
    end = time.time()
    times_modified.append(end - start)

coeffs = np.polyfit(ns, times_original, 2)  
p = Polynomial(coeffs[::-1])  # Create Polynomial object for easy plotting

upper_bound = lambda n: 1.2 * p(n)  # Adjust multipliers to get tight bounds
lower_bound = lambda n: 0.8 * p(n)  # Adjust multipliers to get tight bounds

plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.plot(ns, times_original, 'bo-', label='Original Function')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Time vs n for Original Function')
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(ns, times_original, 'bo-', label='Time Taken')
plt.plot(ns, p(ns), 'r-', label='Fitted Curve')
plt.plot(ns, upper_bound(ns), 'g--', label='Upper Bound')
plt.plot(ns, lower_bound(ns), 'y--', label='Lower Bound')
plt.axvline(x=1800, color='grey', linestyle='--', label='n_0 = 1800')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Time vs n with Upper and Lower Bounds')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(ns, times_modified, 'bo-', label='Modified Function')
plt.plot(ns, p(ns), 'r-', label='Fitted Curve')
plt.plot(ns, upper_bound(ns), 'g--', label='Upper Bound')
plt.plot(ns, lower_bound(ns), 'y--', label='Lower Bound')
plt.axvline(x=1800, color='grey', linestyle='--', label='n_0 = 1800')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Modified Function with Upper and Lower Bounds and n_0')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
