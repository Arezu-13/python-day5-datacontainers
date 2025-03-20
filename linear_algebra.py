import numpy as np
import scipy.linalg as sp

# a
# SciPy dense matrices are just numpy.ndarray
A = np.matrix("1 -2 3; 4 5 6; 7 1 9")

# b
b = np.arange(1, 4)

# c 
# Ax=b --> x=Ab
x = sp.solve(A, b)
print("x is: ", x)

# d
b = A @ x
print("b is: ", b)

# e
B = np.matrix("4 -1 0; 2 1 8; 5 7 3")
X_matrix = sp.solve(A,B)
B_check = A @ X_matrix
print("Double check B", B_check)

# f
eig_val_A, eig_vec_A = sp.eig(A)
print("Eigenvalues: ", eig_val_A)
print("Eigenvectors: ", eig_vec_A)

# g
# Determinant of A
det_A = sp.det(A)
# Calculate inverse (if determinant != 0)
if det_A != 0:
    inv_A = sp.inv(A)
    print("Inverse of determinant of A is :", inv_A)
else:
    print("\nMatrix A is singular; inverse does not exist.")

# h
# Maximum absolute column sum norm
norm_1 = sp.norm(A, ord=1)
print("Order 1", norm_1)

# Spectral norm (largest singular value)
norm_2 = sp.norm(A, ord=2)
print("order 2", norm_2)

# Maximum absolute row sum norm
norm_inf = sp.norm(A, ord=np.inf)
print("Maximum absolute row sum norm", norm_inf)

# Frobenius norm
norm_fro = sp.norm(A, ord='fro')
print("Frobenius norm", norm_fro)