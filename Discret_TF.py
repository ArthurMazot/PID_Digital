class Discret_TF:
    def __init__(self, num, den):
        '''
        Função de transferência discreta:

                    num(z)
        G(z) = -------------------
                    den(z)

        num = [b0, b1, b2, ...]
        den = [a0, a1, a2, ...]

        Assume:
        G(z) = (b0 + b1 z^-1 + ...)
               -------------------
               (a0 + a1 z^-1 + ...)
        '''

        # Normaliza os coeficientes para den[0] = 1
        a0 = den[0]

        self.num = [b / a0 for b in num]
        self.den = [a / a0 for a in den]

        # Vetores para armazenar amostras passadas
        self.u = [0.0] * len(self.num)
        self.y = [0.0] * (len(self.den) - 1)


    def update(self, ut):
        '''
        Recebe a entrada atual ut
        e retorna a saída atual y.
        '''

        self.u[0] = ut
        y = 0.0

        #Soma todos os termos para gerar a saida atual
        for i in range(len(self.num)):
            y += self.num[i] * self.u[i]

        for i in range(1, len(self.den)):
            y -= self.den[i] * self.y[i - 1]


        #Atualiza as entradas e saidas passadas
        for i in range(len(self.u) - 1, 0, -1):
            self.u[i] = self.u[i - 1]

        for i in range(len(self.y) - 1, 0, -1):
            self.y[i] = self.y[i - 1]

        self.y[0] = y

        return y