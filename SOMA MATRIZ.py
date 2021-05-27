#calcula a soma das linhas, colunas e diagonal de uma matriz
import random

def preencheMatrix(dimension, matrix):
    for i in range(dimension):
        for j in range(dimension):
            matrix[i][j] = random.randint(0, 50)


def printMatrix(dimension, matrix):
    for i in range(dimension):
        print(matrix[i])


def somaLinha(matrix, dimension):
    soma_linhas = []
    for i in range(dimension):
        soma = 0
        for j in range(dimension):
            soma += matrix[i][j]
        soma_linhas.append(soma)
    return soma_linhas


def somaColuna(matrix, dimension):
    soma_colunas = []
    for i in range(dimension):
        soma = 0
        for j in range(dimension):
            soma += matrix[j][i]
        soma_colunas.append(soma)
    return soma_colunas


def somaDiagonalPrincipal(matrix, dimension):
    soma = 0
    for i in range(dimension):
        soma += matrix[i][i]
    return soma


def main():
    soma_linha = 0
    dimension = int(input('Digite a dimensão da sua matriz: '))
    matrix = [[0 for x in range(dimension)] for y in range(dimension)]
    preencheMatrix(dimension, matrix)
    printMatrix(dimension, matrix)
    print(f'Soma linhas:{somaLinha(matrix, dimension)}')
    print(f'Soma colunas:{somaColuna(matrix, dimension)}')
    print(f'Soma diagonal principal:{somaDiagonalPrincipal(matrix, dimension)}')


main()