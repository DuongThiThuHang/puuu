import numpy as np 
#1
A = np.array([[2, 3, 1], [4, 1, 5], [3, 2, 4]])
B = np.array([1, 2, 3])
A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)
print("Nghiệm của phương trình bài 1 là:", X)
#2
A = np.array([[1, 2, 3], [2, 3, 1], [3, 1, 2]])
B = np.array([7, 4, 5])
X = np.linalg.solve(A, B)
print("Nghiệm của phương trình bài 2 là:", X)
#3
A = np.array([[1, 1, 1], [2, 3, 5], [4, 0, 5]])
B = np.array([6, -4, 27])
X = np.linalg.solve(A, B)
print("Nghiệm của phương trình bài 3 là:", X)
#4
A = np.array([[2, -3, 1], [4, -6, 2], [-1, 3, -1]])
B = np.array([5, 10, -3])
det_A = np.linalg.det(A)
if det_A != 0:
    X = np.linalg.solve(A, B)
    print("Nghiệm của phương trình bài 4 là:", X)
else:
    print(" Bài 4 Không có nghiệm duy nhất, hệ phương trình có thể phụ thuộc hoặc vô nghiệm.")
#5
A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
B = np.array([1, 0, 1])
X = np.linalg.solve(A, B)
print("Nghiệm của phương trình bài 5 là:", X)
    


