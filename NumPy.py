import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 6, 8])

print("Array A:", a)
print("Array B:", b)

print("\n--- Arithmetic Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** 2)

print("\n--- Statistical Operations ---")
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Max:", np.max(a))
print("Min:", np.min(a))
print("Square Root:", np.sqrt(a))
