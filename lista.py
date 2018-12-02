#nome_da_lista = [elemento1, elemento2, elemento3]


#Para inserir novos elementos em uma lista, utilizamos o método append().
#Este método irá inserir determinado elemento ao final da lista em questão:
lista = ["Arroz", "Feijão"]
lista.append("Macarrão")
print(lista) #Arroz, Feijão, Macarrão

#Para inserir elementos em uma determinada posição de uma lista, utilizamos o método insert().
# Este método recebe como parâmetro o elemento a ser inserido e sua posição:
lista = ["Arroz", "Feijão"]
lista.insert(1, "Macarrão")
print(lista) #Arroz, Macarrão, Feijão

#Para remover elementos de uma lista, utilizamos o método remove().
#Este método recebe como parâmetro o elemento a ser removido:
lista = ["Arroz", "Feijão"]
lista.insert(1, "Macarrão")
print(lista) #Arroz, Macarrão, Feijão
lista.remove("Macarrão")
print(lista) #Arroz, Feijão

#Além dos métodos citados acima, o Python dispõe de outros meios para manipularmos listas:

#pop(índice): remove o elemento da lista;
#index(elemento): retorna o índice do elemento na lista;
#count(elemento): retorna a quantidade de vezes em que um elemento aparece na lista;
#sort(): ordena a lista;
#reverse(): inverte a ordem da lista.

