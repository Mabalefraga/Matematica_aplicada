import math
def descobrir_angulo_com_lados(b, c, alpha):
    a = math.sqrt((b ** 2) + (c **2))
    print(a)
    beta = math.acos((pow(a, 2)+pow(c, 2)-pow(b, 2))/(2*a*c))
    angulo2 = math.degrees(beta)
    print("Angulo ^B:", angulo2)
    gamma=math.acos((pow(a, 2)+pow(b, 2)-pow(c, 2))/(2*a*b))
    angulo3 = math.degrees(gamma)
    print("Angulo ^C:", angulo3)
opcao = input("Digite a opção desejada: ")

if opcao == "2":
    b = float(input("Digite o valor do lado b: "))
    c = float(input("Digite o valor do lado c: "))
    alpha =  float(input("Informe o angulo ^A: "))
    print(descobrir_angulo_com_lados(b, c, alpha))
