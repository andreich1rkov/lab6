import numpy as np

# Функция для ввода матрицы попарного сравнения критериев
def input_comparison_matrix(n):
    matrix = np.zeros((n, n))
    print("Введите значения матрицы попарного сравнения критериев:")
    for i in range(n):
        for j in range(i+1, n):
            while True:
                try:
                    value = float(input(f"Парное сравнение критериев {i+1} и {j+1} (отношение важности, 1/значение): "))
                    if value <= 0: 
                        error = ValueError
                        raise error
                    matrix[i][j] = value
                    matrix[j][i] = 1 / value
                    matrix[i][i] = 1
                    break
                except ValueError:
                    print("Введите положительное число")
    return matrix

# Функция для вычисления весовых коэффициентов
def calculate_weights(matrix):
    n = len(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    max_eigenvalue_index = np.argmax(eigenvalues)
    weights = np.abs(eigenvectors[:, max_eigenvalue_index] / np.sum(eigenvectors[:, max_eigenvalue_index]))
    return weights

# Ввод количества критериев
while True:
    try:
        num_criteria = int(input("Введите количество критериев: "))
        if num_criteria <= 0:
            error = ValueError
            raise error
        break
    except ValueError:
        print('Неверное значение')

# Получение матрицы попарного сравнения
comparison_matrix = input_comparison_matrix(num_criteria)

# Вычисление и вывод весовых коэффициентов
weights = calculate_weights(comparison_matrix)
print("Весовые коэффициенты:")
for weight in weights:
    print(f"{weight:.2f}", end=" ")