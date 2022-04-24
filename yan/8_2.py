import numpy as np

my_data = np.genfromtxt('input.csv', delimiter=',', skip_header=True)
maxa = (my_data.sum(axis=0))
print(maxa.argmax(axis=0)+1)