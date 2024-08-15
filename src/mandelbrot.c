// mandelbrot.c
#include <stdio.h>

// Function to determine if a point belongs to the Mandelbrot set
int mandelbrot(double real, double imag, int max_iter) {
    // Initialize the complex number z = 0 + 0i
    double z_real = 0.0;
    double z_imag = 0.0;
    int iter = 0;

    // Iterate until the magnitude of z exceeds 2 (|zn|^2 <= 4 is equivalent)
    // or the maximum number of iterations is reached
    while (z_real * z_real + z_imag * z_imag <= 4.0 && iter < max_iter) {
        // Calculate the new value of z_real (z_real^2 - z_imag^2 + real)
        double temp_real = z_real * z_real - z_imag * z_imag + real;

        // Calculate the new value of z_imag (2 * z_real * z_imag + imag)
        z_imag = 2.0 * z_real * z_imag + imag;

        // Update z_real with the new calculated value
        z_real = temp_real;

        // Increment the iteration counter
        iter++;
    }

    // Return the number of iterations. If the point is in the Mandelbrot set, 
    // this will be equal to max_iter; otherwise, it will be less.
    return iter;
}
