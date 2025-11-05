#range(5) -> 0, 1, 2, 3, 4          -> range(n) -> todos os num int de 0 a n-1
# range(5, 10) -> 5, 6, 7, 8, 9     -> range(m, n) -> todos os num int de m a n-1
# range(4, 11, 2) -> 4, 6, 8, 10    -> range(m, n, s) -> todos os num int de m a n-1 com um step de s

#range(4)      # 0, 1, 2, 3
#range(0, 4)   # 0, 1, 2, 3
#range(4, 8)   # 4, 5, 6, 7
#range(12, 18, 2) #12, 14, 16

#for i in range(4, 20, 2):
    #print(i, end=" ") #escrever tudo na mesma linha


#num = int(input("Digite o número do mês (1 a 12): "))

"""
match num:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Mês inválido!")
        """
 """
nomes = ["Ana", "Bruno", "Carlos"]

print(nomes[0])      # mostra 'Ana'
nomes.append("Diana") # adiciona um nome
print(nomes)          # mostra ['Ana', 'Bruno', 'Carlos', 'Diana']
nomes.remove("Bruno") # remove 'Bruno'
print(len(nomes))     # mostra o tamanho da lista
 """

 """
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nova_lista = [i * 3 for i in lista]

print("Lista original:", lista)
print("Nova lista (triplo):", nova_lista)
 """

 """
lista_str = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
lista_int = [int(i) for i in lista_str]

print("Lista original (strings):", lista_str)
print("Nova lista (inteiros):", lista_int)
 """
 """
lista_str = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# criar nova lista convertendo cada valor para inteiro
lista_int = [int(i) for i in lista_str]

# mostrar resultado
print("Lista original (strings):", lista_str)
print("Nova lista (inteiros):", lista_int)
"""

def soma():
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    res = num1 + num2
    print(res)


def soma2(num1, num2):
    res = num1 + num2
    return res

res_soma = soma2(num1: 2, num2: 4)
print(".... codigo e mais codigo....")

print(res_soma)

res_soma2 = soma2(res_soma, num2: 4)

print(res_soma2)
