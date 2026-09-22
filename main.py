import matplotlib.pyplot as plt
from ProjetosNovos.PID_Digital.Discret_TF import Discret_TF

def main():
    T = 0.05 #Tempo de amostragem
    tempo_simulacao = 10 #Segundos

    num = [0.0, 0.04553567, -0.03920755]
    den = [1.0, -1.70468809, 0.70468809]

    planta = Discret_TF(num, den)

    t = [] #Vetor de tempo
    y = [] #Vetor de saidas
    u = 1.0 #Entrada do sistema (step)

    for i in range(int(tempo_simulacao / T)):
        t.append(i * T)
        y.append(planta.update(u))

    plt.plot(t, y)
    plt.xlabel("Tempo [s]")
    plt.ylabel("Saída")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()