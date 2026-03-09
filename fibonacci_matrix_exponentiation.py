#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Complexity Analysis:

The Fibonacci number F(n) is computed using matrix exponentiation instead of 
iterative or recursive linear computation.

Normally, Fibonacci is computed using:
    F(n) = F(n-1) + F(n-2)

This requires O(n) time because we must compute all previous terms up to n.

However, Fibonacci can also be represented using the transformation matrix:

    T = [[1, 1],
         [1, 0]]

Such that:

    [F(n)    ] = T^(n-2) * [F(2)]
    [F(n-1)]             [F(1)]

Instead of multiplying T by itself (n-2) times (which would be O(n)),
we use binary exponentiation (also called fast exponentiation).

Binary exponentiation works by:

1. Repeatedly squaring the matrix.
2. Reducing the exponent by half at each step (n = n // 2).

Since the exponent is halved in every iteration, 
the number of iterations required is proportional to log₂(n).

For n up to 10^18, log₂(10^18) ≈ 60,
so the loop runs at most around 60 times.

Each matrix multiplication takes constant time 
(because we are multiplying fixed 2×2 matrices).

Therefore:

Time Complexity:
    O(log n)

Space Complexity:
    O(1)

because we only store a few 2×2 matrices and no additional arrays.

Modulo arithmetic ensures that intermediate values remain bounded,
so arithmetic operations remain constant time.
"""

def fibonacci(n):

    if n == 1:
        return 1
    if n == 2:
        return 2

    mod = 10 ** 9 + 7

    #Matrix multiplication logic
    def matrix_mult(A, B):
        return [
            [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, 
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod ],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]             
                ]  

    #Given transformation matrix
    T = [[1,1],[1,0]]

    #assume result as identity matrix
    result = [[1,0],[0,1]]

    #power to be calculated
    p = n-2

    #exponentiation logic
    while p>0:
        if p % 2 == 1:
            result = matrix_mult(result, T)
        T = matrix_mult(T, T)
        p = p // 2

    T_power = result

    Fn = (T_power[0][0] * 2 + T_power[0][1] * 1) % mod
    return Fn


# ===== Required Main Block =====
if __name__ == "__main__":
    n = int(input().strip())

    if n < 1 or n > 10**18:
        print("Input out of allowed range")
    else:
        print(fibonacci(n))


# In[ ]:




