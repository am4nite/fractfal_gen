import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, axis = plt.subplots()

x_grid = 10
y_grid = 10
L = 50
limit = 55

for x in range(x_grid):
    for y in range(y_grid):
        value = L+y
        if value < limit:
            pixel = Rectangle(
            (x, y),          # bottom-left corner
            1,               # width
            1,               # height
            facecolor="black",
            edgecolor="white"
        )
            axis.add_patch(pixel)
        pair = (x, y)
        print(pair, value)
pixel_position = pixel.get_xy()



axis.set_xlim(0, x_grid)
axis.set_ylim(0, y_grid)
axis.set_aspect("equal", adjustable="box")
axis.set_xlabel("x")
axis.set_ylabel("y")
axis.grid(True)

plt.show()