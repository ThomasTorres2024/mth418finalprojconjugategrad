The computational cost for traditional solvers is $O(n^3)$ which is very high when $n$ is large
Traditional direct solvers such as $LU$ decomposition and 

Why Krylov?
-We prefer Iterative Methods when: 
    - A is large, direct methods are very computationall expensive
    - Ax is easy to compute
    - A is sparse
    - Ax computation with FMM 
    - Krylov methods are some of the most efficient solvers for iterative solutions

    - When we compute Krylov we want to know whats the best vector in the space? What determines Xj? 
    - Xj is chosen from Kj in the CG method by 
    - At each step of this process we are essentially forcing the residuals to be orthogonal to the whole Krylov space 
    - to ensure that the residual is orthogonal i believe its good to make everthing in the space $k$ 

-How do Krylov methods work?    
    - Since we canot directly minimize x and $x^k$, we are stuck with minimizing $r^k = b-Ax^k$
    - Krylov methods minimize the residual, namely the quantity $\| \mathbf{x^k} - \mathbb{x} \|$
    - Vandermonde matrices are poorly conditioned 
        -How do we judge good/poor condition of a matrix? 
        - We know Det(Kr) neq 0 
        - V^tV is the "Gram" Matrix 
        - Q^TQ = I, coniditon number is 1 
        - Condition number is the best possible number when 1 most linearly indepdent you can be obtained from sigmas from gram matrix

-CG Method 
    - CG only works on positive definite symmetric matrices 
    - CG method is NOT guaranteed to work on positive definite matrices 
    - Computing vectors in the basis of the krylov space is really quick 
    - Rj vector is orthogonal to the whole space, the residual vector, will return to this, we need Arnoldi Iteration first 
    - We want to stop our iteration before n is less than j, approximations here are just good enoguh, if we have 10^5, its okay we can stop at 10^2 
    - MIT Methods for Engineers Lec 19 
        - Xk $\in \mathcal(K)_{f}$
        - Residuals are orthogonal to each other and to everything in the Krylov subspace, each residual is a multiple of the new Q 
        - We can call the change in correction of the values of $x_{k}$ corrections, denoted as $\del x_{k} = x_{k} - x_{k+1}$
        - We get also that the corrections to $A$ as $(x_{})^T A x$, where $x^T A x$ is orthogonal, so $(x_{i}-x_{i-1}^T)Ax(x_{k}-x_{k-1}) = 0$
            - The name conjugate comes from here, gives that in the inner product $<x:y> = x^TAy = 0$, meaning the two vectors here are orthogonal
        - CG for Ax=b is composed of 5 steps 
            - d0 = b, x0=0, r0 = $b-A_{x_{0}}$
            ~18 minutes in on the conjugate gradient vid 
            1. We enter search cycle with some new value of d, d is a search direction some $\del x$, alpha is how long we travel along in the direction
                $\alpha_{k} = r_{k-1}^T$ 
            2. we can find difference in x 
            3. we can find difference in r 
            4. what direction do we travel next? we compute this with beta 
            5. search direction is recomputed to be R but with the correction given by b 

            Notice that the krylov idea is implicit here, at the top in step 1 we are doing 1 multiplivation by a in order to get here and also in 3 

            Cost: 
            - 1 multiplication A and the seharch direction, because A is sparse, the cost is the number of non-zeroes in the matrix A. 
            - the other computations we do consist of an inner product in step 1, we use the same value three times, and an inner product involving A, so in total there are two unique inner products, with vectors of length n, so 2*n multiplications also 2n multiplies 
            - we have some vectors being multiplied by scalars as well, maybe 2-3 vector updates 

            In total, with this algorithm, we have a relatively small cost 
            if the algorithm converges quickly, this is a pretty good algorithm 

            After k steps, what is the error? How is it related to the error at the start? 
            Well what is the error to begin with? 
            1 estimate for the convergence factor consists of the eigen values of the system (what even is this 24:10)
            Error is given by $e^T A e$ where its norm is $||e||_{A}$

            Where does gradient come into this? 
            Gradient of what?
            Something to do with the energy? $E(x)=\frac{1}{2} x^T Ax - b^T x$? We are minimizing energy, but HOW is this related? 
            What is the link? 
            By minimizing this expression, the gradient is Grad(e) is 
            $Ax=b$, this is the "natural energy for the proglem",
            when we minimize it and set derivative to zero, we get $Ax=b$ at the minimum of the function
            - Solving the linear eq and the energy function here are the exact same thing 
            - We know A has a min because A is positive definite 
            - How do we minimize A? Given a function and looking for the min, we figure out the gradient, and figure it out 
            - We make some guess along the surface, maybe somewhere along it we have a point, and we want to get to the bottom of the bowl, well the way we do this is whats the steepest way down, so thats the quickest way that we can get to this point 
            - We assume this valley is given to us through a nice 2nd degree polynomial 
            - Stepest descent is very first thought, and brings us in the direction of $r$  
            - the trouble with gradient descent is that we do a lot of work to do little progress, we aren't really going anywhere new, it takes a lot longer than it actually should, each r is not orthogonal 
            -if we take a direction d in step 5 of the algorithm, this is our step, this removes our component in the direction that we took, and in turn that we have a new direction that is "A" orthogonal to previous directions 
            - we can get at this by drawing function contours, we get a bunch of elipes 
            - we are traveling orthogonally in the A inner product
            - non linear conjugate gradient ? 

            

- Arnoldi Iteration
    - Our basis is easy to compute since its sparse but it is "poorly conditioned"
    - We want our basis to be orthonormal
    - Arnoldi Iteration takes the set of vectors in the Krylov space and Orthogonalizes them 
    - With this we produce q1,q2,q3...qr 
    -AQ = QH 
        - very important EQ 
        - A symmetric, original basis
        - Q is the orthonormal basis for Krylov space
        -QH is like QR in Gram Schmiddt, Q is orthogonal, and H is Hessenberg
        - H is symmetric and also tridiagonal, which tells us we have short recurrences 
        - Aq1 = Cq1 + C2q2
        - A = QHQ^T, H must be symmetric, since H=QAQ^T is also just the same when we take its transpose 
        - We can orthonganalize Krylov basis very quickly and easily etiehr by computation or by keeping things orthogonal `

    -Overview, it is like Gram schmidtt 
    - We take first vector b, and just normalize it 
    - we need to saw off the part which is parallel to the vectors just save the orthogonal component, and just normalize at the end 
    - Process is pretty quick when we don't have to substract off too many early components, which occurs when A is symmetric (why?)
