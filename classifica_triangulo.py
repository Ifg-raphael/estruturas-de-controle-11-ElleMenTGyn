#Entra com os valores para cada um dos lados do triângulo
a = int(input())

b = int(input())

c = int(input())

#Verificar primeiramente se é um triângulo, através da fórmula da desigualdade triangular. 
if a < b + c and b < a + c and c < a + b:
    
#Condicional para definir a classificação do triângulo
    if a == b and b == c:
        print("equilátero")
    elif a == b or a ==c or b ==c:
        print("isósceles")
    else:
        print("escaleno")
        
else:
    print("Não forma triângulo")
