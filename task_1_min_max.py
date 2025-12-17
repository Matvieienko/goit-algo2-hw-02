def find_min_max(arr):
    """
    Знаходить мінімальний та максимальний елементи в масиві
    використовуючи метод «розділяй і володарюй» забезпечуючи складність O(n).
    
    Args:
        arr: список чисел
        
    Returns:
        tuple: (мінімум, максимум)
    """
    # Базовий випадок: пустий масив
    if not arr:
        return None, None

    # Допоміжна рекурсивна функція, що працює з індексами
    def divide_and_conquer(low, high):
        # Базовий випадок: один елемент
        if low == high:
            return arr[low], arr[low]
        
        # Базовий випадок: два елементи
        if high == low + 1:
            if arr[low] < arr[high]:
                return arr[low], arr[high]
            else:
                return arr[high], arr[low]
        
        # Розділяємо
        mid = (low + high) // 2
        
        # Рекурсія
        min1, max1 = divide_and_conquer(low, mid)
        min2, max2 = divide_and_conquer(mid + 1, high)
        
        # Об'єднання
        return min(min1, min2), max(max1, max2)

    # Викликаємо допоміжну функцію для всього масиву
    return divide_and_conquer(0, len(arr) - 1)


# Приклади використання
if __name__ == "__main__":
    # Тест 1: пустий масив
    test_arr1 = []
    min_val, max_val = find_min_max(test_arr1)
    print(f"Масив: {test_arr1}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}\n")

    # Тест 2: звичайний масив
    test_arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    min_val, max_val = find_min_max(test_arr2)
    print(f"Масив: {test_arr2}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}\n")
    
    # Тест 3: масив з негативними числами
    test_arr3 = [-5, -2, -10, 3, 7, -1]
    min_val, max_val = find_min_max(test_arr3)
    print(f"Масив: {test_arr3}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}\n")
    
    # Тест 4: масив з одним елементом
    test_arr4 = [42]
    min_val, max_val = find_min_max(test_arr4)
    print(f"Масив: {test_arr4}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}\n")
    
    # Тест 5: масив з двома елементами
    test_arr5 = [10, 5]
    min_val, max_val = find_min_max(test_arr5)
    print(f"Масив: {test_arr5}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}\n")
    
    # Тест 6: рандомний масив на 20 елементів
    import random
    test_arr6 = [random.randint(-100, 100) for _ in range(20)]
    min_val, max_val = find_min_max(test_arr6)
    print(f"Масив: {test_arr6}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}")
