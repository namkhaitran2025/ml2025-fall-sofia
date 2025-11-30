import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Training data
N = int(input("Enter a positive integer N for the number of training data point: "))
if N <= 0:
    print("Error: Current inputs must be a positive integer")
    exit()

training_set = np.empty((N, 2))
for i in range(N):
    x = float(input(f"Enter input feature for training pair - x #{i+1}: "))
    y = int(input(f"Enter class label for training pair   - y #{i+1}: "))
    if y < 0:
        print("Error: y value must be non-negative")
        exit()

    training_set[i] = [x, y]

print("----------------------------------------")
# Test data
M = int(input("Enter a positive integer N for the number of testing data point: "))
if M <= 0:
    print("Error: Current inputs must be a positive integer")
    exit()

test_set = np.empty((M, 2))
for i in range(M):
    x = float(input(f"Enter input feature for testing pair - x #{i+1}: "))
    y = int(input(f"Enter class label for testing pair   - y #{i+1}: "))
    if y < 0:
        print("Error: y value must be non-negative")
        exit()

    test_set[i] = [x, y]

# Reshape for kNN
X_train = training_set[:, 0].reshape(-1, 1)
y_train = training_set[:, 1].astype(int)
X_test = test_set[:, 0].reshape(-1, 1)
y_test = test_set[:, 1].astype(int)

print("###########################################")

# Testing for k from 1 to 10
best_k = None
test_accuracy = -1

for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"k = {k}, accuracy = {acc:.5f}")

    if acc > test_accuracy:
        test_accuracy = acc
        best_k = k

print("============================================")
print("\nBest k:", best_k)
print("Best test accuracy:", round(test_accuracy, 5))