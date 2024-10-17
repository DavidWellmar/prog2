
"""
Solutions to module 4
Review date:
"""

student = "David Wellmar"
reviewer = ""

import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    n_c = 0
    # Write your code here
    plt.figure(figsize=(8, 8))
    for i in range(n):
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)

        dist = (x**2+y**2)**(1/2) 
        color = 'red' if dist <= 1 else 'blue'
        plt.scatter(x, y, marker = '.', c = color)
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

        if dist <= 1:
             n_c += 1
    
    pi_approx = 4*n_c/n
    plt.savefig(f'pictures/mc_circle_{n}')
    plt.show()

    return  pi_approx
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
       #print(approximate_pi(n))
        print("hej")
    # 3.068, 3.1372, 3.14164
if __name__ == '__main__':
	main()
