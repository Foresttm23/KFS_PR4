import matplotlib.pyplot as plt

def var_init():
    s = 10
    r = 30
    b = 3
    Dt = 0.01

    x = y = z = 1
    t = 0

    xresult = [x]
    yresult = [y]
    zresult = [z]
    timesteps = [t]
    
    return x, y, z, t, s, r, b, Dt, xresult, yresult, zresult, timesteps

def fill_values(x, y, z, t, s, r, b, Dt, xresult, yresult, zresult, timesteps):
    next_x = x + (s * (y - x)) * Dt
    next_y = y + (r * x - y - x * z) * Dt
    next_z = z + (x * y - b * z) * Dt

    x, y, z = next_x, next_y, next_z
    t += Dt

    xresult.append(x)
    yresult.append(y)
    zresult.append(z)
    timesteps.append(t)

    return x, y, z, t, s, r, b, Dt, xresult, yresult, zresult, timesteps

def lorenz_plot(timesteps, xresult, yresult, zresult):
    plt.figure(figsize=(10, 7))

    plt.subplot(3, 1, 1)
    plt.plot(timesteps, xresult)
    plt.xlabel('t')
    plt.ylabel('x')

    plt.subplot(3, 1, 2)
    plt.plot(timesteps, yresult)
    plt.xlabel('t')
    plt.ylabel('y')

    plt.subplot(3, 1, 3)
    plt.plot(timesteps, zresult)
    plt.xlabel('t')
    plt.ylabel('z')

    plt.show()

    plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, projection='3d')
    ax.plot(xresult, yresult, zresult)
    plt.show()


if __name__ == '__main__':
    x, y, z, t, s, r, b, Dt, xresult, yresult, zresult, timesteps = var_init()

    while t < 30.:
        x, y, z, t, s, r, b, Dt, xresult, yresult, zresult, timesteps = fill_values(x, y, z, t, s, r, b, Dt, xresult, yresult, zresult, timesteps)

    lorenz_plot(timesteps, xresult, yresult, zresult)
    
