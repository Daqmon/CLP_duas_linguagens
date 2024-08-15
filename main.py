import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library into ctypes
mandelbrot_lib = ctypes.CDLL('./mandelbrot.so')

# Define the function prototype for the C function
mandelbrot_func = mandelbrot_lib.mandelbrot
mandelbrot_func.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
mandelbrot_func.restype = ctypes.c_int

# Parameters for the Mandelbrot set
width, height = 800, 800
max_iter = 1000
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

# Create an array to store the Mandelbrot set data
mandelbrot_set = np.zeros((height, width), dtype=np.int32)

# Calculate the Mandelbrot set
for i in range(width):
    for j in range(height):
        real = xmin + (xmax - xmin) * i / width
        imag = ymin + (ymax - ymin) * j / height
        mandelbrot_set[j, i] = mandelbrot_func(real, imag, max_iter)

# Display the Mandelbrot set using matplotlib
plt.imshow(mandelbrot_set, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()
