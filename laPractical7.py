import numpy as np
A = np.mat("3 -2; 1 0 ")
print("A\n",A)
print("Eigen values",np.linalg.eigvals(A))
eigenvalues,eigenvectors= np.linalg.eig(A)
print("First tuple of eig",eigenvalues)
print("Second tuple of eig",eigenvectors)
u = eigenvectors[:,0]
print(u)
lam=eigenvalues[0]
print(lam)
print(np.dot(A,u))
print(lam*u)
