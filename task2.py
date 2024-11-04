#!python3

'''
use a for loop to iterate through all possible integers to find the factors of 24
'''
if __name__ == "__main__":
 def main():
    factors = []
    n = 24
    for i in range(1, 25):
        if n%i==0:
            factors.append(i)
