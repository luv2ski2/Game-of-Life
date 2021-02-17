from tkinter import Canvas, Tk
import time as depression
import random

width = 400
height = 400

root = Tk()
c = Canvas(root, width = width, height = height, background = "white")
c.pack()

class cell:
    def __init__(self, x, y, width, height, canvas, state):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.state = state
        # self.state = random.randint(0, 1)
        if self.state == 1:
            self.fill = 'black'
        else:
            self.fill = 'white'
        ## have to remove stuff below, move to draw function
        self.rect = 0
        # self.rect = c.create_rectangle(x, y, x + width, y + height, fill = self.fill)
    def changeColor(self, color):
        self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=color)
    def draw(self):
        self.canvas.delete(self.rect)
        if self.state == 1:
            self.fill = 'black'
        else:
            self.fill = 'white'
        self.rect = c.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.fill)
        # print('General Kenobi')


def create2DArray(cols, rows):
    arr = []
    for i in range(cols):
        arr1 = []
        for j in range(rows):
            arr1.append(0)
        arr.append(arr1)
    return arr
#print(create2DArray(10, 10))
rows = 20
cols = 20
resolution = width / rows
grid = create2DArray(cols, rows)
def start():
    global grid
    for i in range(cols):
        for j in range(rows):
            grid[i][j] = cell(i * resolution, j * resolution, resolution, resolution, c, random.randint(0, 1))
            grid[i][j].draw()
    # print(count(grid, 0, 2))
    frame()

def frame():
    global grid
    grid = draw1()
    for i in range(cols):
        for j in range(rows):
            grid[i][j].draw()
    root.after(100, frame)


def draw1():
    global grid
    next = create2DArray(cols, rows)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            state = grid[i][j].state
            neighbors = count(i, j)
            if state == 0 and neighbors == 3:
                next[i][j] = cell(i * resolution, j * resolution, resolution, resolution, c, 1)
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                next[i][j] = cell(i * resolution, j * resolution, resolution, resolution, c, 0)
            # elif neighbors == 2 or neighbors == 3:
            else:
                next[i][j] = cell(i * resolution, j * resolution, resolution, resolution, c, grid[i][j].state)
    return next

def count(x, y):
    # loc = grid[x][y]
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # print(str((x + i)) + " , " + str((y + j)) + " state: " + str(grid[x + i][y +j].state))
            # grid[x + i][y + j].changeColor('green')
            col = (x + i + rows) % rows
            row = (y + j + cols) % cols
            sum = sum + grid[col][row].state
            # sum = sum + grid[x + i][y + j].state
    sum = sum - grid[x][y].state
    return sum

## main ##
start()
# cellTest = cell(10, 10, 10, 10, c)
# print('hi')
# root.after(5000, cellTest.draw)
# cellTest.state = 1
# print("hello there")
root.mainloop()