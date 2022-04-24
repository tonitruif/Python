import numpy as np

my_data = np.genfromtxt('8_4.csv', delimiter=',', skip_header=False)
for iy, ix in np.ndindex(my_data.shape):
    if ((ix % 2 == 0) and (iy % 2 == 1)) or ((ix % 2 == 1) and (iy % 2 == 0)):
        my_data[iy, ix] /= 2
print(my_data)
with open("output.csv", "w") as file:
    np.savetxt(file, my_data, newline='\n', fmt="%g", delimiter=',')

