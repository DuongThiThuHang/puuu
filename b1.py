import numpy as np 
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
print(A)
print(B)
#Tổng 2 ma trận 
C = A + B 
print(C)
#Hiệu 2 ma trận
D = A - B 
print(D)
#Tích 2 ma trận 
E = np.dot(A, B)
print(E)
#Tính tích Hadamard 
G = A * B 
print(G)
#Tính định thức của ma trận A 
det_A = np.linalg.det(A)
print(det_A)
#Tính ma trận nghịch đảo của A
A_inv = np.linalg.inv(A)
print(A_inv)
#Tính ma trận chuyển vị của A 
A_transpose = A.T 
print(A_transpose)
#Tính giả nghịch đảo Moore-Penrose của ma trận A 
A_pinv = np.linalg.pinv(A)
print(A_pinv)
#Tính chuẩn Frobenius của ma trận A 
frobenius_norm = np.linalg.norm(A)
print(frobenius_norm)
#Tính norm L1 và L2 
l1_norms = np.linalg.norm(A, ord=1, axis=1)
l2_norms = np.linalg.norm(A, ord=2, axis=1)
print(l1_norms)
print(l2_norms)
#Tìm ma trận con 2x2 
submatrix = A[:2, :2]
print(submatrix)
#Thực hiện phép nhân vô hướng 
a = 2 
result = A * a 
print(result)
#Tính ma trận đối xứng 
A_T = A.T 
A_symmetric = (A + A_T) / 2 
print(A_symmetric)
#Tính tổng các phần tử trên đường chéo chính 
diagonal_elements = np.diagonal(A)
diagonal_sum = np.sum(diagonal_elements)
print(diagonal_sum)
#Tìm các giá trị riêng và vector riêng
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)
#Kiểm tra xem ma trận A có khả năng chéo hóa không
eig_vec_matrix = np.array(eigenvectors)
if np.linalg.det(eig_vec_matrix) != 0:
    print("Ma trận A có thể chéo hóa.")
else:
    print("Ma trận A không thể chéo hóa.")
#Tạo một ma trận H có kích thước 3x3 với tất cả phần tử bằng 1 sau đó cộng A
H = np.ones((3, 3))
result = A + H 
print(result)
#Tạo ma trận đường chéo các phần tử của một vector ngẫu nhiên có kích thước 3 
vector = np.random.randint(1, 10, size=3)
diagonal_matrix = np.diag(vector)
print(vector)
print(diagonal_matrix)
#Kiểm tra xem ma trận A có phải ma trận trực giao không
#Tạo ma trận vuông K kích thước 4x4 
K = np.random.randint(0, 10, size=(4, 4))
print(K)
#Tính ma trận khả nghịch
det_K = np.linalg.det(K)
if det_K != 0:
    print("Ma trận K là khả nghịch.")
else: 
    print("Ma trận K không là khả nghịch.")
    
    







