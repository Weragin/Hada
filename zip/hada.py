import tkinter as tk

snake = [(250, 250)]
direction = (0, -1, "N")
time = 0
speed = 100

root = tk.Tk()
root.geometry("500x500")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()


def loop():
    global snake, direction, time, speed
    fw = open("data/hada.txt", mode="w")
    canvas.create_rectangle(snake[-1][0], snake[-1][1], snake[-1][0] + 1, snake[-1][1] + 1, outline="black")
    snake.append((snake[-1][0] + direction[0], snake[-1][1] + direction[1]))
    canvas.after(100, lambda: loop())


def turn(e):
    global direction
    print("stasdf")
    if e.char == "w" or e.char == "Up":
        direction = (0, -1, "H")
    elif e.char == "a" or e.char == "Left":
        direction = (-1, 0, "L")
    elif e.char == "s" or e.char == "Down":
        direction = (0, 1, "D")
    elif e.char == "d" or e.char == "Right":
        direction = (1, 0, "P")


canvas.focus_set()
canvas.bind("<KeyPress>", turn)
canvas.after(100, loop)

root.mainloop()
