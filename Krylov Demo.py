"""
For URI MTH 418 
Script for CG Method
"""
import pprint
from sklearn.datasets import make_spd_matrix
from sklearn.datasets import make_sparse_spd_matrix
import numpy as np
from Krylov_Functions import * 

def main():
    #create SPD matrix, and denote it A.
    #for the sake of simplicity this matrix is in R^NxN 

    #change this to modify the dimension of the SPD matrix we have 
    n: int = 5
    A = spd_matrix = make_sparse_spd_matrix(n_dim=n, norm_diag=False, random_state=42)
    
    #create and randomize vector, b, which is in R^n 
    b = np.random.uniform(low=0.0, high=1.0, size=(n,))

    #print results for both A and B 
    print("-"*50+"\nMatrix A: ")
    pprint.pp(A)
    print("-"*50+"\nVector b: ")
    pprint.pp(b)

    #0.05 param is the amount of error that we are willing to except 
    result = efficient_conjugate_gradient(A,b,0.05)
    print("-"*50)
    print(result)
    print("-"*50)
    preciseRes = np.linalg.solve(A,b)
    e = preciseRes-result 
    print(np.dot(e,e))

main()