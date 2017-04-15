length = None
width = None
area = None
perimeter = None
if_square = False
name = 'прямоугольника'

length = int(input('Введите высоту: '))
width = int(input('А теперь укажи ширину: '))
area = length * width
perimeter = 2 * (length + width)

if width == length:
    name = 'квадрата'

print('Площадь {}: {} '.format(name,area))
print('Периметр {}: {} '.format(name,perimeter))
