import numpy as np
from nptyping import NDArray, Float64

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

def add(left: NDArray[np.float64], right: NDArray[np.float64]) -> NDArray[np.float64]:
	print(left + right)

def multiple(arr: NDArray[np.float64], scalar: Float64) -> NDArray[np.float64]:
	print(arr * scalar)

def hadamard(left: NDArray[np.float64], right: NDArray[np.float64]) -> NDArray[np.float64]:
	print(left * right)

def dot(left: NDArray[np.float64], right: NDArray[np.float64]) -> NDArray[np.float64]:
	print(np.dot(left, right))

add(a, b)
multiple(a, 10)
hadamard(a, b)
dot(a, b)

c = np.array([a, b])
print(c)