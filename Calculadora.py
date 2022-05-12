#Este programa é uma calculadora básica feita em python 
#O objetivo é que o utilizador introduza dois números escolha o tipo de calculo que quer fazer e o resultado irá ser dado ao utilizador

from re import sub


def soma(n1,n2):
    return n1 + n2

def subtração(n1,n2):
    return n1 - n2

def mutiplicação(n1,n2):
    return n1 * n2

def divisão(n1,n2):
    return n1 / n2



print("*Calculadora do nuno*")
print("Somar-1")
print("Subtrair-2")
print("Multiplicar-3")
print("Dividir-4")
print("Sair-0")

e = input("Qual é a sua opção? : ")



while (e != "0"):

    if e == "1":
        n1 = float(input("Introduza o primeiro número:"))  
        n2 = float(input("Introduza o primeiro número:"))  
    
        print("O resultado da soma é:", soma(n1,n2))

        
        print("\n*Calculadora do nuno*")
        print("Somar-1")
        print("Subtrair-2")
        print("Multiplicar-3")
        print("Dividir-4")
        print("Sair-0")

        e = input("Qual é a sua opção? : ")

    elif e == "2":
        
        n1 = float(input("Introduza o primeiro número:"))  
        n2 = float(input("Introduza o primeiro número:"))  
    
        print("O resultado da subtração é:", subtração(n1,n2))
        
        
        print("\n*Calculadora do nuno*")
        print("Somar-1")
        print("Subtrair-2")
        print("Multiplicar-3")
        print("Dividir-4")
        print("Sair-0")

        e = input("Qual é a sua opção? : ")
    
    elif e == "3":
        n1 = float(input("Introduza o primeiro número:"))  
        n2 = float(input("Introduza o primeiro número:"))  
    
        print("O resultado da multiplicação é:", mutiplicação(n1,n2))

  
        print("\n*Calculadora do nuno*")
        print("Somar-1")
        print("Subtrair-2")
        print("Multiplicar-3")
        print("Dividir-4")
        print("Sair-0")

        e = input("Qual é a sua opção? : ")

    elif e == "4":
        n1 = float(input("Introduza o primeiro número:"))  
        n2 = float(input("Introduza o primeiro número:"))  
    
        print("O resultado da divisão é:", divisão(n1,n2))
    
        
        print("\n*Calculadora do nuno*")
        print("Somar-1")
        print("Subtrair-2")
        print("Multiplicar-3")
        print("Dividir-4")
        print("Sair-0")

        e = input("Qual é a sua opção? : ")

    else:
        quit()