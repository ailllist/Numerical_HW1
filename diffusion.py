import time
import numpy as np
import matplotlib.pyplot as plt

DATA_SIZE = (640, 640)


def diffusion(u_in, dt, D=1.0):
    xmax, ymax = DATA_SIZE
    u_new = [[0.0] * ymax for x in range(xmax)]
    for i in range(xmax):
        for j in range(ymax):
            dxx = (u_in[(i + 1) % xmax][j] +
                   u_in[(i - 1) % xmax][j] -
                   2.0 * u_in[i][j])

            dyy = (u_in[i][(j + 1) % ymax] +
                   u_in[i][(j - 1) % ymax] -
                   2.0 * u_in[i][j])

            u_new[i][j] = u_in[i][j] + D * dt * (dxx + dyy)
    return u_new


def dropInk(max_iter):
    xmax, ymax = DATA_SIZE
    u = [[0.0] * ymax for x in range(xmax)]

    ink_low = int(DATA_SIZE[0] * 0.4)
    ink_high = int(DATA_SIZE[0] * 0.6)
    for i in range(ink_low, ink_high):
        for j in range(ink_low, ink_high):
            u[i][j] = 0.005
    u_init = u

    start = time.time()
    for i in range(max_iter):
        u = diffusion(u, 0.1)
    end = time.time()
    return end - start, u_init, u


tot_time, u_init, u_ = dropInk(100)

u_ = np.array(u_)
plt.imshow(u_)
plt.show()