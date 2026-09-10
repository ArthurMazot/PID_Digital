import matplotlib.pyplot as plt
from planta import planta

def main():
    t = []
    u = 1
    y = []
    for i in range(1000):
        t.append(i*0.05)
        y.append(planta(u))

    plt.plot(t, y)
    plt.show()


if __name__ == '__main__':
    main()