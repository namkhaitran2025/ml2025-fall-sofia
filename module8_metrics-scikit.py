import numpy as np
from sklearn.metrics import precision_score, recall_score

N = int(input("Enter an integer for the number of data points N: "))
if N <= 0:
    print("Error: Current input must be positive integers")
    exit()

print("------------------------------------")

X = np.empty(N, dtype=int)  # Ground truth labels
Y = np.empty(N, dtype=int)  # Predicted labels

for i in range(N):
    X[i] = int(input(f"Enter ground truth    #{i+1} (0/1): "))
    Y[i] = int(input(f"Enter predicted class #{i+1} (0/1): "))
    if (not (X[i] == 0 or X[i] == 1) or     # Strictly binary
        not (Y[i] == 0 or Y[i] == 1)):
        print("Error: Current input must be 0 (False) or 1 (True)")
        exit()

precision = precision_score(X, Y, zero_division=0)  # Can show warning with zero_division="warn"
recall = recall_score(X, Y, zero_division=0)

print("------------------------------------")
print("Precision:", precision)
print("Recall:   ", recall)