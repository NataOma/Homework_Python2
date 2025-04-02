# Задача 2. Треугольник
# Треугольник существует только тогда, когда сумма любых двух его сторон
# больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если
# хотя бы в одном случае отрезок окажется больше суммы двух других, то
# треугольника с такими сторонами не существует. Отдельно сообщить является
# ли треугольник разносторонним, равнобедренным или равносторонним.

a, b, c = 5, 5, 5

if a + b > c and b + c > a and c + a > b:
    print('Треугольник существет, ', end='')
    if a != b and a != c and b != c:
        print('он разносторонний')
    elif (a == b and a != c) or (b == c and b != a) or (a == c and c != b):
        print('он равнобедренный')
    else:    
    #elif a == b and a == c and b == c:
        print('он равносторонний')
else:
    print('Треугольник не существет')
