import math
def descobrir_angulo_interno(a, b, c):
    alpha = math.acos((pow(b, 2)+pow(c, 2)-pow(a, 2))/(2*b*c))
    print (alpha)
    angulo1 = math.degrees(alpha)
    print("Angulo ^A:", angulo1)
    beta = math.acos((pow(a, 2)+pow(c, 2)-pow(b, 2))/(2*a*c))
    print(beta)
    angulo2 = math.degrees(beta)
    print("Angulo ^B:", angulo2)
    gamma=math.acos((pow(a, 2)+pow(b, 2)-pow(c, 2))/(2*a*b))
    print(gamma)
    angulo3 = math.degrees(gamma)
    print("Angulo ^C:", angulo3)

opcao = input("Digite a opção desejada: ")

if opcao == "1":
    a = float(input("Digite o valor do lado a: "))
    b = float(input("Digite o valor do lado b: "))
    c = float(input("Digite o valor do lado c: "))
    print(descobrir_angulo_interno(a, b, c))
    
