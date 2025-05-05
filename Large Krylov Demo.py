"""
For URI MTH 418 
Script for CG Method.
Done off screen.
This takes awhile. 
"""
import pandas as pd
from sklearn.datasets import make_spd_matrix
from sklearn.datasets import make_sparse_spd_matrix
import numpy as np
from Krylov_Functions import * 
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt
import time 

def do_test(is_sparse : bool):

    if(is_sparse):
        print("Testing Sparse Matrices")
    else:
        print("Testing Dense Matrices") 

    n_val : list [int]= []
    err : list[int] = []
    time_elapsed : list[int] =[]

    max: int = 200
    for n in range(1,max+1):
        
        #generate corresponding dense or sparse matrix 
        if(is_sparse):
            A = make_sparse_spd_matrix(n_dim=n, norm_diag=False, random_state=42)
        else:
            A = make_spd_matrix(n_dim=n, random_state=42)

        #create and randomize vector, b, which is in R^n 
        b = np.random.uniform(low=0.0, high=1.0, size=(n,))

        start = time.time()
        result = efficient_conjugate_gradient(A,b,0.05)
        end = time.time()

        #using built in solver
        preciseRes = np.linalg.solve(A,b)
        e = preciseRes-result 
        n_val.append(n)
        err.append(np.dot(e,e))
        time_elapsed.append(end-start)

    d = {'Dimension': n_val, 'Error Squared': err}
    d2 = {'Dimension': n_val, 'Time Elapsed Seconds': time_elapsed}
    dfError = pd.DataFrame(data=d)
    dfTime = pd.DataFrame(data=d2)

    #for error
    plt.subplot(1, 2, 1)
    plt.title("Sparse A CG Error Plot")
    sns.scatterplot(dfError,
                x='Dimension',
                y='Error Squared')
    
    #Time complexity Plot
    plt.subplot(1, 2, 2)
    plt.title("Sparse CG Time Plot")
    #render time complexity approximation
    sns.scatterplot(dfTime,
                x='Dimension',
                y='Time Elapsed Seconds')
    plt.show()

def main():
    #test both sparse and dense matrices 
    do_test(True)
    #do_test(False)

main()