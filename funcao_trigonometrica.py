from math import pi, sin, floor, ceil, sqrt
import matplotlib.pyplot as plt
import numpy as np

def main () :
    def menu():
        print("O que você deseja fazer:")
        print("1 - Função de seno")
        print("2 - Função de cosseno")
        print("3 - Função da tangente")
    
    def periodo_seno(c):
        if c < 0:
            c = c * -1 
            periodo_s = (2 * pi) / c
            print("período: ", periodo_s)
        else:
            periodo_s = (2 * pi) / c
            print("período: ", periodo_s)
    
    def imagem_seno(a,b):
        im1 = a - b
        im2 = a + b
        if im1 > im2:
            print("imagem: [", im2, ",", im1, "]")
        else:
            print("imagem: [", im1, ",", im2, "]")

    def amplitude_seno(b):
        if b < 0:
            b = b * -1
            print("amplitude: ", b)
        else:
            print("amplitude: ", b)

    def grafico_seno(a, b, c, d, p):
        x = np.linspace(floor(p-d), ceil((3.5*p)-d), 1000)
        y = a+b*np.sin(c*x+d)
        plt.ylim(floor(a-b)-1,ceil(a+b)+1)
        plt.xlim(p-d,(3.5*p)-d)
        plt.plot(x,y)
        plt.grid()
        plt.show()
        return grafico_seno(a, b, c, d, p)

    def periodo_cosseno(c):
        if c < 0:
            c = c * -1 
            periodo_s = (2 * pi) / c
            print("período: ", periodo_s)
        else:
            periodo_s = (2 * pi) / c
            print("período: ", periodo_s)
    
    def imagem_cosseno(a,b):
        im1 = a - b
        im2 = a + b
        if im1 > im2:
            print("imagem: [", im2, ",", im1, "]")
        else:
            print("imagem: [", im1, ",", im2, "]")
        
    def amplitude_cosseno(b):
        if b < 0:
            b = b * -1
            print("amplitude: ", b)
        else:
            print("amplitude: ", b)
    
    def grafico_cosseno(a, b, c, d, p):
        x = np.linspace(floor(p-d), ceil((3.5*p)-d), 1000)
        y = a+b*np.cos(c*x+d)
        plt.ylim(floor(a-b)-1,ceil(a+b)+1)
        plt.xlim(p-d,(3.5*p)-d)
        plt.plot(x,y)
        plt.grid()
        plt.show()
    
    def periodo_tan(c):
        if c < 0:
            c = c * -1
            periodo = pi/c
            print("período: ", periodo)
        else:
            periodo = pi/c
            print("período: ", periodo)    
    def grafico_tangente(a, b, c, d, p):
        x = np.linspace(floor(p-d), ceil((3.5*p)-d), 1000)
        y = a+b*np.tan(c*x+d)
        y[:-1][np.diff(y) < 0] = np.nan
        plt.ylim(floor(a-b)-1,ceil(a+b)+1)
        plt.xlim(p-d,(3.5*p)-d)
        plt.plot(x,y)
        plt.grid()
        plt.show()

    menu()
    opcao = input("digite a opcao desejada: ")
    if opcao == "1":
        print("Insira as variáveis da função:")
        a = eval(input("Insira o valor de a: "))
        b = eval(input("Insira o valor de b: "))
        c = eval(input("Insira o valor de c: "))
        d = eval(input("Insira o valor de d: "))
        print("a função que você inseriu é: y = ", a,"+", b, "* sen(", c, " * x", "+", d, ")")
        p = (2 * pi)/abs(c)
        periodo_seno(c)
        imagem_seno(a,b)
        amplitude_seno(b)
        grafico_seno(a, b, c, d, p)

    elif opcao == "2":
        print("Insira as variáveis da função:")
        a = float(input("Insira o valor de a: "))
        b = float(input("Insira o valor de b: "))
        c = float(input("Insira o valor de c: "))
        d = float(input("Insira o valor de d: "))
        print("a função que você inseriu é: y = ", a,"+", b, "* sen(", c, " * x", "+", d, ")")
        p = (2 * pi)/abs(c)
        periodo_cosseno(c)
        imagem_cosseno(a,b)
        amplitude_cosseno(b)
        grafico_cosseno(a, b, c, d, p)

    elif opcao == "3":
        print("Insira as variáveis da função:")
        a = float(input("Insira o valor de a: "))
        b = float(input("Insira o valor de b: "))
        c = float(input("Insira o valor de c: "))
        d = float(input("Insira o valor de d: "))
        print("a função que você inseriu é: y = ", a,"+", b, "* sen(", c, " * x", "+", d, ")")
        p = (pi)/abs(c)
        periodo_tan(c)
        grafico_tangente(a, b, c, d, p)



if __name__ =='__main__':
    main ()
