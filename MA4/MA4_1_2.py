
"""
Solutions to module 4
Review date:
"""

student = "David Wellmar"
reviewer = ""

import math as m
import random as r
import functools
# Radius r = 1
#rad = 1

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 

    #Create distant with Lambda function 
    sum = lambda x,y :x + y
    pow = lambda x: x**2
    
    # Calculate distant with functools.reduce
    # Map the elements with Lambda function d
    # Use functools to iterate over the values and sum
    n_in = 0
    for n in range(n):
        # Create  coordinates as list with List comprehensions
        coord = [r.uniform(-1, 1) for i in range(d)]
        
        # Calculate distant with functools.reduce and map
        # map: take the power of each coord element
        # functools.reduce: sum all elements
        dist = (functools.reduce(sum, map(pow, coord)))**0.5

        if dist <= 1:
             n_in += 1

    cube_vol = (2)**d
    hyper_sphere_approx = cube_vol* n_in/n
    # approx_vol = prob_inside * hypercube vol
    return hyper_sphere_approx

def hypersphere_exact(n,d):
    return m.pi**(d/2)/(m.gamma(1+d/2))
     
def main():
    n = 100000
    d = 2
    print("res: ", sphere_volume(n,d))
    print("facit:", hypersphere_exact(n,d))

    print("res: ", sphere_volume(100000,11))
    print("facit:", hypersphere_exact(100000,11))

# res:  3.1469114691146913
# facit: 3.141592653589793
# res:  1.945619456194562
# facit: 1.8841038793898994

if __name__ == '__main__':
	main()
