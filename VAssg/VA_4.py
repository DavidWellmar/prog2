"""
Solutions to module VA 4

Student:
Mail:
"""
#!/usr/bin/env python3

#from person import Person
from numba import njit
import time
import matplotlib.pyplot as plt 
 

"""
Write a script that gives a plot for comparison of two approaches for Fibonacci numbers
"""

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)	
	
def main():
	# f = Person(50)
	# print(f.getAge())
	# print(f.getDecades())

	# f.setAge(51)
	# print(f.getAge())
	# print(f.getDecades())
	n_lst = [5, 10, 15, 20, 25, 30, 35, 40, 45, 47, 50]
	n_lst = [5, 8, 10, 12, 15, 18, 20, 22, 25, 28, 30]
	
	# Save the times for each fib calculation
	numba_lst = [None]*len(n_lst)
	py_lst = [None]*len(n_lst)

	for i, n in enumerate(n_lst):
		#Numba calculation
		print(n)
		start = time.perf_counter()
		a = fib_numba(n)
		end = time.perf_counter()
		numba_lst[i] = round(end-start, 3)

		#Python calculation
		start = time.perf_counter()
		b = fib_py(n)
		end = time.perf_counter()
		py_lst[i] = round(end-start, 3)

		print(a, numba_lst[i], b, py_lst[i])

		plt.scatter(n, numba_lst[i], label = "Numba", marker = '.', c="red")
		plt.scatter(n, py_lst[i], label = "Python", marker = '.', c="blue")
		plt.xlabel("n for fibonacci")
		plt.ylabel("time elapsed")
	plt.savefig("Time_comparison")
	plt.show()


if __name__ == '__main__':
	main()


"""What is the result for Fibonacci with n=47? Why?"""