"""
For URI MTH 418 
Script for CG Method
"""
import pprint
from sklearn.datasets import make_spd_matrix
from sklearn.datasets import make_sparse_spd_matrix
import numpy as np
from Krylov_Functions import * 
import time 

def main():
    for n in range(2,8):
        #change this to modify the dimension of the SPD matrix we have 
        A = make_sparse_spd_matrix(n_dim=n, norm_diag=False, random_state=42)
        
        #create and randomize vector, b, which is in R^n 
        b = np.random.uniform(low=0.0, high=1.0, size=(n,))

        #print results for both A and B 
        print("-"*50+"\nMatrix A: ")
        pprint.pp(A)
        print("-"*50+"\nVector b: ")
        pprint.pp(b)
        both_vecs = solve(A,b)
        print("-"*50+"\nVector x: ")
        pprint.pp(both_vecs[0])
        print("-"*50+"\nCG Estimate")
        pprint.pp(both_vecs[1])

main()