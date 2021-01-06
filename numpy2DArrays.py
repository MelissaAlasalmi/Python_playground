import numpy as np

np_2d = np.array([[1.88, 1.88, 1.82, 1.91,  1.91,  1.85],
                  [81.6, 97.5, 95.3, 85.3, 90.7, 81.6]])
print(np_2d)
print(type(np_2d))
print("Rows and columns of np_2d: " + str(np_2d.shape))
print("First row of np_2d: " + str(np_2d[0]))
print("Second row of np_2d: " + str(np_2d[1]))
print("Second and third columns of np_2d: " + str(np_2d[:,1:3]))
print("Value at row 2, column 4 of np_2d: " + str(np_2d[1, 3])) # or np_2d[1][3]