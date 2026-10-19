import turtle

def koch_curve(t, level, size):
	if level == 0:
		t.forward(size)
	else:
		size /= 3.0
		koch_curve(t, level - 1, size)
		t.left(60)
		koch_curve(t, level - 1, size)
		t.right(120)
		koch_curve(t, level - 1, size)
		t.left(60)
		koch_curve(t, level - 1, size)

def main():
	try:
		level = int(input("Введіть рівень рекурсії: "))
		if level < 0:
			print("Рівень рекурсії не може бути від'ємним.")
			return
	except ValueError:
		print("Помилка: будь ласка, введіть ціле число.")
		return

	size = 300

	screen = turtle.Screen()
	screen.bgcolor("white")
	screen.title(f"Сніжинка Коха (рівень рекурсії: {level})")

	t = turtle.Turtle()
	t.speed(100)
	t.penup()
	t.goto(-size / 2, size / 3)
	t.pendown()

	for _ in range(3):
		koch_curve(t, level, size)
		t.right(120)

	print("Малювання завершено! Закрийте вікно з графікою для виходу.")
	screen.mainloop()


if __name__ == "__main__":
	main()