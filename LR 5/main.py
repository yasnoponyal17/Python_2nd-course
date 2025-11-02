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
    n_list = list(range(10, 300, 10))
    
    result_recursive = []
    result_iterative = []

    for n in n_list:
        time_recursive = benchmark(fact_recursive, n, number=1000, repeat=3)
        time_iterative = benchmark(fact_iterative, n, number=1000, repeat=3)
        
        result_recursive.append(time_recursive)
        result_iterative.append(time_iterative)

    plt.plot(n_list, result_recursive, 'go-',  label="Рекурсивный", markersize=4)
    plt.plot(n_list, result_iterative, 'ro-',  label="Итеративный", markersize=4)
    plt.xlabel("Число для факториала")
    plt.ylabel("Время (секунды)")
    plt.title("Сравнение рекурсивного и итеративного факториала")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()


