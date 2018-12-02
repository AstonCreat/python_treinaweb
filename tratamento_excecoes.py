#É comum que, no desenvolvimento de uma aplicação, queiramos prever situações em que um erro possa ocorrer,
# com a finalidade de tratarmos estas situações para que a execução do nosso software não seja interrompida.

#Por exemplo: imagine que temos um programa responsável por realizar as quatro operações básicas da matemática.
# Sabemos que há alguns casos que são impossíveis de serem realizados, como a divisão por 0. Neste caso, nosso software precisa sempre verificar se esta situação está ocorrendo e, caso esteja, exibir uma mensagem de erro.

#No Python, os seguintes comandos são utilizados para o tratamento de exceções:

#try/except: tenta executar o determinado bloco de código definido no try e, caso este gere um erro, executa o bloco de código definido no except;
#try/finally: após o bloco try ser executado, com sucesso ou não, o código definido dentro do finally é executado;
#Raise: se, por algum motivo, precisarmos gerar uma exceção em nosso script, utilizamos o comando raise;
#Assert: assim como o comando raise, o assert serve para gerar exceções, porém é necessário definir uma condição para isso.

#Para tratar exceções utilizando o try/except, o Python utiliza a seguinte sintaxe:
#try:
    #<bloco de código>
#except:
    #<tratamento de erro>

#Dessa maneira, o Python irá tentar executar o bloco de código
# definido no try e, caso algum erro seja gerado, o comando except será chamado e seu código executado:

try:
    numero = 15/0
except:
    print("Divisão por zero não existe")

#Sendo assim, no código acima, ao executar o script, um erro será gerado ao tentar realizar a divisão por 0 e a
# mensagem "Divisão por zero não existe" será exibida para o usuário.

#Porém, podemos perceber que um erro de divisão por zero é comum na maioria dos programas a serem desenvolvidos. Por isso,
# o Python possui uma lista de exceções prontas para serem utilizadas e, assim, capturar um erro específico em nosso sistema, conforme pode ser visto em sua documentação: https://docs.python.org/3/library/exceptions.html

#Para utilizar estas exceções pré-definidas no Python, utilizamos o comando except da seguinte forma:

try:
    numero = 15/0
except ZeroDivisionError:
    print("Divisão por zero não existe")

#O finally, como visto em tópicos anteriores, serve para executar um determinado bloco de código
# imediatamente após a execução do try, independente se a execução foi feita com sucesso ou não.
# O finally não possui dependência com o try, ou seja, independente se o código definido no bloco try
# for executado corretamente ou não, o bloco contido na instrução finally será executado.
# Voltando ao exemplo da divisão por zero, imagine que queremos exibir uma mensagem sempre que o try seja finalizado
try:
    numero = 15/0
except ZeroDivisionError:
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada")

#O código acima irá entrar na exceção ZeroDivisionError e, logo após, executar o bloco de código contido
# na instrução finally. Vale lembrar que isso independe se o bloco try gerou ou não uma exceção.
# De qualquer forma, o bloco finally será executado.

#Para gerar exceções no Python, utilizamos o comando raise.
# Este comando retorna uma exceção, sendo utilizado quando queremos testar a execução do nosso software:

try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada")

#No código acima, o comando raise irá gerar uma exceção do tipo ZeroDivisionError,
# que será tratada pelo except definido logo abaixo e, com isso, exibir a mensagem "Divisão por zero não existe".


#Assim como o raise, utilizamos o assert para gerar exceções na execução do nosso sistema.
# Porém, o assert irá gerar essa exceção a depender de uma condição. Por exemplo:
try:
    numero = 15
    divisor = 0
    assert divisor != 0
except:
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada")
#Ou seja: sempre que a condição definida no assert for falsa, uma exceção será gerada.


