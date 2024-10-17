
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
import concurrent.futures as futures
import functools
import time

def sphere_volume(n, d):
    sum = lambda x,y :x + y
    pow = lambda x: x**2
    n_in = 0
    for n in range(n):
        coord = [r.uniform(-1, 1) for i in range(d)]
        dist = (functools.reduce(sum, map(pow, coord)))**0.5
        if dist <= 1:
             n_in += 1
    cube_vol = (2)**d
    hyper_sphere_approx = cube_vol* n_in/n
    return hyper_sphere_approx  

def hypersphere_exact(n, d):
    return m.pi**(d/2) / (m.gamma(1 + d/2))

def sphere_volume_parallel1(n, d, np):
    # Using multiprocessor to perform np iterations of volume function
    start = time.perf_counter()

    with futures.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, [n]*np, [d]*np)

    end = time.perf_counter()
    elapsed_time = end - start
    print(f"Elapsed time with 10 parallel tasks: {elapsed_time} seconds")
    res = sum(results) / np
    return res

def sphere_volume_parallel2(n, d, np):
    # Parallel code - parallelize actual computations by splitting data
    split = n//np
    with futures.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, [split]*np, [d]*np)
    res = sum(results) / np
    return res

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 10
    print(f"facit: {hypersphere_exact(n,d)}")

    start = time.perf_counter()
    results = []
    for y in range (np):
        results.append(sphere_volume(n, d))
    end = time.perf_counter()
    elapsed_time = end - start
    
    res = sum(results)/np
    print(f"Elapsed time with 10 tasks: {elapsed_time:.6f} seconds")
    print(f"The volume is calculated to: {res}")

    res = sphere_volume_parallel1(n*10, d, np)
    print(f"The volume is calculated to: {res}")

    res = sphere_volume_parallel2(n, d, np)
    print(f"The volume is calculated to: {res}")

if __name__ == '__main__':
	main()
     
# Elapsed time: 15.822135 seconds
