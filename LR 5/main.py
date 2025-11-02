import timeit
import matplotlib.pyplot as plt

def fact_recursive(n):
    if n < 0:
        return 'Число не должно быть меньше нуля'
    if n == 0 or n == 1:
        return 1
    return n * fact_recursive(n - 1)

def fact_iterative(n):
    if n < 0:
        return 'Число не должно быть меньше нуля'
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def benchmark(func, n, number=1, repeat=3):
    times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
    return min(times)


def main():
    test_data = list(range(7, 228, 7))
    
    result_recursive = []
    result_iterative = []

    for n in test_data:
        time_recursive = benchmark(fact_recursive, n, number=1000, repeat=3)
        time_iterative = benchmark(fact_iterative, n, number=1000, repeat=3)
        
        result_recursive.append(time_recursive)
        result_iterative.append(time_iterative)

    plt.plot(test_data, result_recursive,  label="Рекурсивный", markersize=4)
    plt.plot(test_data, result_iterative,  label="Итеративный", markersize=4)
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного факториала")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()


