import numpy as np
import matplotlib.pyplot as plt

M = np.zeros((8, 8))
M[::2, ::2] = 2 
M[1::2, 1::2] = 2 

print(M)