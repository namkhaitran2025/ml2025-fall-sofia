import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# number of data points
N = int(input("Enter an integer for the number of data points N: "))
# number of nearest neighbors
k = int(input("Enter an integer for the number of nearest neighbors k: "))

if N <= 0 or k <= 0:
    print("Error: Current inputs must be positive integers")
    exit()

if k > N:
    print("Error: k > N, cannot have more neighbors than data points")
    exit()

print("Let x be the feature and y be the label of each datapoint...")
points = np.empty((N, 2))
for i in range(N):
    x = float(input(f"Enter x value for datapoint #{i+1}: "))
    y = float(input(f"Enter y value for datapoint #{i+1}: "))
    points[i] = [x, y]

label_var = np.var(points[:, 1])
print(f"The variance of the training labels is: {label_var}")

print("______________ Scikit-learn kNN regression ______________")

X = float(input("\nEnter a value for X: "))

# L1 distance
model = KNeighborsRegressor(n_neighbors = k, metric = 'manhattan')
x_train = points[:, 0].reshape(-1, 1)     # shape (N,1)
y_train = points[:, 1]
model.fit(x_train, y_train)

# Predict Y for input X
Y = model.predict(np.array([[X]]))[0]

# Get neighbors based on L1 distances
neighbors = model.kneighbors(np.array([[X]]),
                             n_neighbors = k,
                             return_distance = False)

print(f"{k} Nearest neighbors based on L1 distance:")
print(points[neighbors[0]])
print(f"Predicted Y for {k}-NN regression: {Y}")