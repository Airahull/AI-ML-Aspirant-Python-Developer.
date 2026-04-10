# some theory stuff about numpy in python 
'''
📘 What is NumPy?

NumPy (Numerical Python) is a powerful Python library used for numerical computations and working with arrays.

It provides a high-performance multidimensional array object (ndarray) and tools to perform mathematical operations on large datasets efficiently.

🧠 Key Features of NumPy
Multidimensional Arrays
Faster and more efficient than Python lists
Example: 1D, 2D, 3D arrays
Vectorized Operations
Perform operations on entire arrays without loops
Example: a + b instead of using for loop
Mathematical Functions
Supports functions like mean, sum, standard deviation, etc.
Broadcasting
Allows operations on arrays of different shapes
Integration
Works with libraries like:
Pandas
TensorFlow
PyTorch
🤖 Why NumPy is Important for AI & Development
1. Foundation of AI/ML
Almost all AI libraries are built on NumPy arrays
Data in AI models is handled as matrices and vectors

👉 Example:

Images = matrix of pixels
Dataset = table → converted to arrays
2. High Performance
Written in C → very fast
Handles large datasets efficiently

👉 Important in AI because:

Models train on millions of data points
3. Simplifies Complex Math

AI involves:

Linear Algebra (matrices)
Statistics
Probability

NumPy makes these easy:

import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b)   # [5 7 9]
4. Data Preprocessing

Before training AI models:

Cleaning data
Normalization
Transformation

All done using NumPy arrays

5. Backbone of Other Libraries

Libraries like:

Scikit-learn
Pandas

depend heavily on NumPy.

🎯 Real-World Example
Image Processing → pixels stored as arrays
Recommendation Systems → matrix operations
Self-driving cars → sensor data processing
Finance apps → numerical analysis
📝 Conclusion

NumPy is the core building block of AI and scientific computing in Python. Without NumPy:

AI development becomes slow
Mathematical operations become complex

👉 That’s why every AI/ML developer must understand NumPy.



'''

import numpy as np

# creating a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1d)           