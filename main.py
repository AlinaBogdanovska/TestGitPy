# 2 /ᐠ｡ꞈ｡ᐟ\

def calculate_rectangle_perimeter(length, width):
    if length < 0 or width < 0:
        return "❗Сторони не можуть бути від'ємними!"
    return 2 * (length + width)

a = 5.5
b = 3.2
S = calculate_rectangle_perimeter(a, b)
print("Периметр -> ", S)