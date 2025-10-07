# Лабораторная работа 3. Построение бинарного дерева
## Постановка задачи
Разработайте программу на языке Python, которая будет строить бинарное дерево (дерево, в каждом узле которого может быть только два потомка). Отображение результата в виде словаря (как базовый вариант решения задания). Далее исследовать другие структуры, в том числе доступные в модуле collections в качестве контейнеров для хранения структуры бинарного дерева. 

Необходимо реализовать рекурсивный вариант gen_bin_tree

Алгоритм построения дерева должен учитывать параметры, переданные в качестве аргументов функции. Пример: 

```python
def gen_bin_tree(height=<number>, root=<number>):
    pass
```

Если параметры были переданы, то используются они. В противном случае используются параметры, указанные в варианте.

Дерево должно обладать следующими свойствами:

1. В корне дерева (root) находится число, которое задает пользователь (индивидуально для студента).
2. Высота дерева (height) задается пользователем (индивидуально для студента).
3. Левый (left leaf) и правый потомок (right leaf) вычисляется с использованием алгоритмов, индивидуальных для каждого студента в группе и приведен ниже.
4. Если ваш номер в группе, больше чем последний номер в списке ниже, начинаете отсчет с начала (пример: если вы под №19, то ваш вариант условия №1)

Вариант условия 9:
root = 9, height = 6
left_leaf = root * 2 + 1
right_leaf = 2 * root - 1

## Код программы
### Обычный
```python
height = int(input("Введите значение height: "))
root = int(input("Введите значение root: "))

def bin_tree(height, root):
    if height == 0:
        return None
    
    dictionary_tree = {
        'root': root,
        'left': bin_tree(height - 1, root * 2 + 1),
        'right': bin_tree(height - 1, root * 2 - 1)
    }

    return dictionary_tree

def print_tree(tree, level=0):
    if not tree:
        return None
    
    print_tree(tree['right'], level + 1)
    print("   " * level + str(tree['root']))
    print_tree(tree['left'], level + 1)

print("Бинарное дерево:")
print_tree(bin_tree(height, root))

```
### С использованием модуля collections
```python
from collections import deque

height = int(input("Введите значение height: "))
root = int(input("Введите значение root: "))

def bin_tree(height, root):
    if height == 0:
        return None
    return {
        'root': root,
        'left': bin_tree(height - 1, root * 2 + 1),
        'right': bin_tree(height - 1, 2 * root - 1)
    }

def deque_tree(tree):
    if not tree:
        return None
    
    queue = deque([tree])
    result = []
    
    while queue:
        current = queue.popleft()
        if current:
            result.append(current['root'])
            queue.append(current.get('left'))
            queue.append(current.get('right'))
    
    return result

print("Значения дерева:", deque_tree(bin_tree(height, root)))
```

## Результат
### Результат 1
![Результат](images/result.png)
На изображении видно только часть результата, так как бинарное дерево слишком большое.
### Результат 2
![Результат_2](images/result-2.png)

## Пояснение к коду
### Общий код
Сначала пользователь вводит значения для **height** и **root**.

В функции **bin_tree** рекурсивно создается бинарное дерево с помощью словаря. Если **height** = 0, то будет возвращено пустое значение. В ином случае будет возвращен словарь, в котором ключ **root** отвечает за текущее значение дерева, **left** и **right** означают левое и правое поддеревья с высотой на 1 меньше и вычислениями, заданными в условии.

### Функция print_tree
Данная функция выводит бинарное дерево в повернутом виде. Функция принимает дерево, которое будет выводиться и переменную **level**, которая будет добавлять пробелы для более наглядного вывода. Если дерево оказывается пустым, то выводится пустое значение.

Сначала будет печататься правое поддерево, затем текущее дерево и после его левое поддерево. То есть правое поддерево будет находиться сверху, а левое снизу от узла.

Пример:
&nbsp;&nbsp;&nbsp; 5
3
&nbsp;&nbsp;&nbsp; 7

### Функция deque_tree
Данная функция обходит бинарное дерево, используя deque (очередь) из модуля collections. Сначала идет проверка на пустое дерево или нет. Если нет, то создается очередь **queue**, в которую помещается корень дерева и список **result** для записи значений.

Дальше пока очередь **queue** не пуста из неё извлекают первое значение и помещают в переменную **current**. После чего его добавляют в список **result**, а в очередь **queue** добавляются левое и правое поддеревья этого элемента.

Пример:
[3, 7, 5]

## Тестирование
```python
import unittest

def bin_tree(height, root):
    if height == 0:
        return None
    
    dictionary_tree = {
        'root': root,
        'left': bin_tree(height - 1, root * 2 + 1),
        'right': bin_tree(height - 1, root * 2 - 1)
    }

    return dictionary_tree

class TestBinTree(unittest.TestCase):
    def test_example_1(self):
        tree = bin_tree(0, 9)
        self.assertEqual(tree, None)
    def test_example_2(self):
        tree = bin_tree(1, 9)
        self.assertEqual(tree['root'], 9)
        self.assertEqual(tree['left'], None)
        self.assertEqual(tree['right'], None)
    def test_example_3(self):
        tree = bin_tree(3, 3)
        # 1 уровень дерева
        self.assertEqual(tree['root'], 3) 
        # 2 уровень дерева
        self.assertEqual(tree['left']['root'], 7)
        self.assertEqual(tree['right']['root'], 5)
        # 3 уровень дерева
        self.assertEqual(tree['left']['left']['root'], 15)
        self.assertEqual(tree['left']['right']['root'], 13)
        self.assertEqual(tree['right']['left']['root'], 11)
        self.assertEqual(tree['right']['right']['root'], 9)
        
				
unittest.main(verbosity = 2)
```
## Результат
![Тестирование](images/test_result.png)

### Ефимов Сергей Робертович, 2 курс, ИВТ-2
