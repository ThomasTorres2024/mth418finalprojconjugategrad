import numpy as np

"""Computes R^2 error between 2 vectors"""
def compute_error(x1,x2):
    e = x1-x2
    return np.dot(e,e)


"""Iterates until we reach an acceptable margin of error instead of when
residual vector has reached zero
A - matrix 
b - target vector in Ax=b
t - int, threshold value for error
"""
def efficient_conjugate_gradient(A,b, t : float):
    x = np.zeros((A.shape[0],))
    d = r = b 
    while(not np.dot(r,r)<t):
        aProdD = np.matmul(A,d)
        a = np.dot(r,r)/np.dot(d,aProdD)
        x = x + a*d
        rNew = r-a*aProdD
        b = np.dot(rNew,rNew)/np.dot(r,r)
        d = rNew + b*d

        #update r discard rNew 
        r=rNew

    #when r becomes zero, we are done, we have minimized r. 
    return x 
"""Takes in a positive definite matrix A, and a vector B
where A is in
Precisely computes to the full answer doesn't end at an approximation  
 """
def full_conjugate_gradient(A, b):
    #we take x^(0) to be 0 here
    x = zero = np.zeros((A.shape[0],))
    d = r = b 
    for i in range(5):
    #while(not np.array_equal(r,zero)):
        aProdD = np.matmul(A,d)
        a = np.dot(r,r)/np.dot(d,aProdD)
        x = x + a*d
        rNew = r-a*aProdD
        b = np.dot(rNew,rNew)/np.dot(r,r)
        d = rNew + b*d

        #update r discard rNew 
        r=rNew

    #when r becomes zero, we are done, we have minimized r. 
    return x 



"""Normalize vector"""
def normalize_vec(v):
    norm = np.linalg.norm(v)
    #check if vector is zero, avoid div by 0 error
    if(norm !=0):
        v=v/norm
    return v 

"""Returns an orthnormal basis of matrix A.
   Essentially this is just Arnoldi iteration. 
"""
def obtain_orthonormal_krylov_basis(A,b):
    #initialize basis by starting with normalized b 
    krylov_base = np.zeros((A.shape[0],A.shape[1]))
    krylov_base[0:,]= normalize_vec(b)
    #iterate over the columns of A
    for i in range(1,A.shape[1]):
        #multiply prev vector by A 
        qI = np.matmul(A,krylov_base[i-1,:])

        #this part down here is essentially gram-schmidtt 
        for j in range(0,i-1):
            #compute dot product between previous vectors and itself 
            dot = np.dot(qI,krylov_base[j])
            #take off parallel part
            qI = qI - dot*krylov_base[j]
            
        #normalize vec and add to krylov base 
        krylov_base[:,i]=normalize_vec(qI)
    return krylov_base 

"""Returns an orthonormal basis for a Krylov space given by A,b
   Note, this is not a desireable basis this is just an example one 
"""
def standard_krylov_basis(A,b):
    #reserv a slot in memory for the krylov space we are going to compute to, note to future self size of this does not need to be size n 
    krylov_base = np.zeros((A.shape[0],A.shape[1]))
    krylov_base[0:,]=b
    #compute A^n * b successively 
    for i in range(1,krylov_base.shape[1]):
        krylov_base[:,i]=np.matmul(A,krylov_base[i-1,:])

    #use arnoldi iteration to create an orthonormal basis for our vectors 
    
    return krylov_base