import matplotlib.pyplot as plt
from Discret_TF import Discret_TF

def main():
    T = 0.05 #Tempo de amostragem
    tempo_simulacao = 50 #Segundos
        
    #Sem integrador
    num = [1, -0.8734]
    den = [1, -0.7046]

    #Com integrador
    numI = [0.04553567, -0.03920755]
    denI = [1.0, -1.70468809, 0.70468809]

    Gz = Discret_TF(num, den)

    #Vetores para o plot
    t = [] #Vetor de tempo
    saida = [] #Vetor de saidas

    y = 0
    r = 1.0 #Entrada do sistema (step)

    for i in range(int(tempo_simulacao / T)):
        y = Gz.update(r-y)

        t.append(i*T)
        saida.append(y)

    plt.plot(t, saida)
    plt.xlabel("Tempo [s]")
    plt.ylabel("Saída")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
