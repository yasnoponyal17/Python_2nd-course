import timeit
import matplotlib.pyplot as plt
from functools import lru_cache

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

@lru_cache(maxsize=None)
def fact_recursive_memo(n):
    if n < 0:
        return 'Число не должно быть меньше нуля'
    if n == 0 or n == 1:
        return 1
    return n * fact_recursive_memo(n - 1)

class FactorialMemoizer:
    def __init__(self):
        self.cache = {0: 1, 1: 1}
    
    def fact_iterative_memo(self, n):
        if n < 0:
            return 'Число не должно быть меньше нуля'
        
        if n in self.cache:
            return self.cache[n]
        
        result = 1
        last_cached = max(k for k in self.cache.keys() if k <= n)
        result = self.cache[last_cached]
        
        for i in range(last_cached + 1, n + 1):
            result *= i
            self.cache[i] = result
        
        return result

fact_memoizer = FactorialMemoizer()

def benchmark(func, n, number=1, repeat=3):
    times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
    return min(times)

def main():
    test_data = list(range(7, 228, 7))
    
    result_recursive = []
    result_iterative = []
    result_recursive_memo = []
    result_iterative_memo = []

    for n in test_data:
        time_recursive = benchmark(fact_recursive, n, number=100, repeat=3)
        time_iterative = benchmark(fact_iterative, n, number=100, repeat=3)
        
        fact_recursive_memo.cache_clear()
        time_recursive_memo = benchmark(fact_recursive_memo, n, number=100, repeat=3)
        
        fact_memoizer.cache.clear()
        fact_memoizer.cache = {0: 1, 1: 1} 
        time_iterative_memo = benchmark(lambda x: fact_memoizer.fact_iterative_memo(x), n, number=100, repeat=3)
        
        result_recursive.append(time_recursive)
        result_iterative.append(time_iterative)
        result_recursive_memo.append(time_recursive_memo)
        result_iterative_memo.append(time_iterative_memo)

    plt.figure(figsize=(12, 8))
    
    plt.plot(test_data, result_recursive, label="Рекурсивный (оригинал)", marker='o', markersize=3)
    plt.plot(test_data, result_iterative, label="Итеративный (оригинал)", marker='s', markersize=3)
    plt.plot(test_data, result_recursive_memo, label="Рекурсивный (мемоизация)", marker='^', markersize=3)
    plt.plot(test_data, result_iterative_memo, label="Итеративный (мемоизация)", marker='d', markersize=3)
    
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение различных реализаций факториала")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

    # Демонстрация работы мемоизации на последовательных вызовах
    print("Демонстрация мемоизации:")
    print("Первые вызовы:")
    
    fact_memoizer.cache.clear()
    fact_memoizer.cache = {0: 1, 1: 1}
    fact_recursive_memo.cache_clear()
    
    n_test = 50
    print(f"fact_recursive_memo({n_test}): {benchmark(fact_recursive_memo, n_test, number=1, repeat=1):.6f} сек")
    print(f"fact_iterative_memo({n_test}): {benchmark(lambda x: fact_memoizer.fact_iterative_memo(x), n_test, number=1, repeat=1):.6f} сек")
    
    print("\nПовторные вызовы (должны быть быстрее):")
    print(f"fact_recursive_memo({n_test}): {benchmark(fact_recursive_memo, n_test, number=1, repeat=1):.6f} сек")
    print(f"fact_iterative_memo({n_test}): {benchmark(lambda x: fact_memoizer.fact_iterative_memo(x), n_test, number=1, repeat=1):.6f} сек")

if __name__ == "__main__":
    main()