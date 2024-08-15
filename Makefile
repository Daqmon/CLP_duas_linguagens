# Variables
CC = gcc
CFLAGS = -Wall -fPIC
TARGET = mandelbrot

# Build the shared library
all: $(TARGET).so

$(TARGET).so: src/mandelbrot.c
	$(CC) $(CFLAGS) -shared -o $(TARGET).so src/mandelbrot.c

# Run the case study (execute the Python script)
run: all
	python src/main.py

# Clean up build files
clean:
	rm -f $(TARGET).so
