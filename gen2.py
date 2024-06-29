import itertools

def generate_combinations(arr):
    # Создаем список для хранения всех комбинаций
    combinations = []
    
    # Проходим по каждому элементу массива
    for i in range(len(arr)):
        new_combinations = []
        
        # Для каждой текущей комбинации добавляем новые варианты
        for combination in combinations or [[]]:
            for value in range(arr[i] + 1):
                new_combinations.append(combination + [value])
                
        combinations = new_combinations
    
    return combinations

def write_combinations_to_file(combinations, filename):
    with open(filename, 'w') as file:
        for combination in combinations:
            file.write(str(combination) + '\n')

# Исходный массив
arr = [120, 1, 120, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]

# Генерация всех комбинаций
combinations = generate_combinations(arr)

# Запись комбинаций в файл
write_combinations_to_file(combinations, 'combinations.txt')
