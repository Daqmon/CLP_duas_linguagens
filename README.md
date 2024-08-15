# CLP_duas_linguagens

Aluno: Diego Aquino Montero

Implementação de fractal de Mandelbrot

Resumo
Este projeto implementa uma aplicação gráfica do fractal de Mandelbrot usando duas linguagens de programação. Python é usado para o desenvolvimento da interface, e C para o cálculo dos valores representados. O projeto foi realizado em Windows 11.

Requisitos para compilação
GCC para compilar o Código em C
Python 3.x
Bibliotecas Python: 'numpy' e 'matplotlib'* para as operações matemáticas e implementação da interface respectivamente. 

*Para compilar o programa é necessário instalar as dependências do Python com 'pip install' no terminal.
pip install numpy
pip install matplotlib

Crie o arquivo .so ao compilar 'mandelbrot.c' usando 'gcc -shared -o mandelbrot.so -fPIC mandelbrot.c' para ter uma biblioteca compartilhada.

Código-fonte
'mandelbrot.c' é um arquivo de tipo C que inclui a implementação dos cálculos dos valores do fractal de Mandelbrot.
'main.py' é um arquivo de tipo Python que inclui a implementação da interface para a visualização do fractal e aplica os cálculos em 'mandelbrot.c'.

Estrutura de diretórios (GitHub)
- `src/`: Contém o código-fonte (mandelbrot.c,main.py)
- `Documentação_do_projeto`: Documento em PDF da implementação.
- `Makefile`: Script para compilar o código C e execução de caso de estudo.
