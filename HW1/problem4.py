import math
import time
import matplotlib.pyplot as plt
import numpy as np

# increment from 10 to 1000 
lengths = np.arange(10, 10e2, 50)

def method1(A):
    n = len(A)
    maxVal = A[0]
    for i in range(n):
        isMax = True
        for j in range(n):
            if A[j] > A[i]:
                isMax = False
        if isMax:
            maxVal = A[i]
    return maxVal

def method2(A):
    n = len(A)
    maxVal = A[0]
    for i in range(1, n):
        if A[i] > maxVal:
            maxVal = A[i]
    return maxVal

# track method 1 and methdod 2 times in a list
method1Times = []
method2Times = []

for i in lengths:
    A = np.random.randint(0, 1000, int(i))
    start = time.time()
    method1(A)
    end = time.time()
    method1Times.append(end - start)

    start = time.time()
    method2(A)
    end = time.time()
    method2Times.append(end - start)

# plot the times
plt.plot(lengths, method1Times, label="Method 1")
plt.plot(lengths, method2Times, label="Method 2")
plt.xlabel("Length (n)")
plt.ylabel("Time (s)")
plt.title("Method 1 vs Method 2")
plt.legend()
plt.show()



# Theoretical comparison for the second part of question 4
n = [i for i in range(1, 10)]

f_n = [2 ** i for i in n]

g_n = [math.factorial(i) for i in n]

# plot the functions - Figure 2
plt.plot(n, f_n, label="f(n) = 2^n")
plt.plot(n, g_n, label="g(n) = n!")
plt.xlabel("n")
plt.ylabel("f(n) and g(n)")
plt.title("f(n) = 2^n vs g(n) = n!")
plt.legend()
plt.show()