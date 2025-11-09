import numpy as np

# number of data points
N = int(input("Enter an integer for N: "))
# number of nearest neighbors
k = int(input("Enter an integer for k: "))

if N <= 0 or k <= 0:
    print("Error: Current inputs must be positive integers")
    exit()

if k > N:
    print("Error: k > N, cannot have more neighbors than data points")
    exit()

points = np.empty((N, 2))
for i in range(N):
    x = float(input(f"Enter x value for data point {i+1}: "))
    y = float(input(f"Enter y value for data point {i+1}: "))
    points[i] = [x, y]

X = float(input("\nEnter a value for X: "))

# L1 distance
distances = np.empty(N)
for i in range(N):
    distances[i] = np.abs(points[i][0] - X)

# Find indices of neighbors based on L1 distances
nearest_indices = np.argsort(distances)[:k]
Y = np.mean(points[nearest_indices, 1])

print(f"{k} Nearest neighbors based on L1 distance:")
print(points[nearest_indices])
print(f"Predicted Y for {k}-NN regression: {Y}")