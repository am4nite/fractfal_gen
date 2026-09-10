import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np  
import c_module 


x_grid = 2
y_grid = x_grid
N = 250 #pocet px na stranu
rec_size = x_grid / N
iter = 10
limit = 40000

for i, Q in enumerate(np.arange(-2, 2, 0.05)):
    fig, axis = plt.subplots()

    cx = 0.314
    cy = Q

    for x in np.arange(-x_grid, x_grid, rec_size):
        for y in np.arange(-y_grid, y_grid, rec_size):
            #value = c_module.iterate_point(x, y, cx, cy, iter)
            #if value < limit:
            if c_module.iterate_point(x, y, cx, cy, iter) < limit:
                pixel = Rectangle(
                (x, y),          # bottom-left corner
                rec_size,               # width
                rec_size,               # height
                facecolor="black",
                edgecolor="black"
            )
                axis.add_patch(pixel)
            pair = (x, y)

    axis.set_xlim(-x_grid, x_grid)
    axis.set_ylim(-y_grid, y_grid)
    axis.set_aspect("equal", adjustable="box")
    axis.set_axis_off()

    plt.savefig(
        f"fractal_{i}.png",
        dpi=150,
        bbox_inches="tight",
        pad_inches=0
    )
    plt.close(fig)