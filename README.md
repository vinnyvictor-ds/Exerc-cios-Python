# Exercícios-Python
Repositórios com os exercícios de PROGRAMAÇÃO 1A praticados na linguagem de programação Python.
### Sobre o exercício 5:
Resumidamente, o exercício 5 pede para que o usuário digite o nome, a idade e o sexo de 4 pessoas e mostre, em seguida, a média de idades do grupo, qual o nome do homem mais velho e quantas mulheres tem menos de 21 anos. 

### Aprendizados neste exercício:
Pude aprofundar meus conhecimentos sobre o uso de listas e sublistas. Em listas, destaco:
## 1: USO E MANIPULAÇÃO DE LISTAS/SUBLISTAS ##

        dados_pessoas = [nome,idade,sexo]
        pessoas.append(dados_pessoas)

Essa parte é muito importante no código, pois ela permite alocar dentro da lista 'pessoas' uma outra lista chamada dados_pessoas que, a partir disso, funcionará como uma sublista de pessoas.

Além disso, uma coisa importante de destacar é que para manipular os dados da sublista dados_pessoas, eu não preciso necessariamente tentar manipular a lista geral 'pessoas'. Eu posso simplesmente usar a própria sublista para conseguir o que eu quero. Como assim?

sabemos que dados_pessoas é uma lista que contém, respectivamente, essas variáveis: nome, idade, sexo. Nesse sentido, se eu quiser fazer alguma manipulação no código que necessita do nome, da idade ou do sexo, então eu posso simplesmente fazer:

dados_pessoas[0] para NOME; dados_pessoas[1] para IDADE; dados_pessoas[2] para SEXO.

Exemplo disso: 
        if (dados_pessoas[2] == 'F') and (dados_pessoas[1] < 21):
            idades_femininas = idades_femininas + 1
Perceba que eu estou verificando o índice 2, isto é, se o SEXO é F e se, no índice 1, isto é, a IDADE é menor do que 21.

## 2: ORGANIZAÇÃO DOS DADOS DA LISTA UTILIZANDO COMO REFERÊNCIA A **IDADE** ##
Uma outra dúvida pertinente que surgiu era: Como eu poderia organizar a lista pela idade, isto é, pelo índice 1 se eu tinha uma lista de listas? Eu sabia que o método sort() era capaz de ordenar os elementos de uma lista. No entanto, eu não sabia como eu poderia fazer isso NESTE exercício. Então, surgiu uma solução com o auxílio do Gemini: utilizar a função anônima lambda.

## O que é a função lambda? ##
Resumidamente, a função lambda é uma função anônima, pois o programador não precisa alocá-la em uma variável como nas funções padrões, exemplo:
Ao invés de fazer:
  def dobrar_valor(x):
    return 2 * x
podemos fazer simplesmente:
    lambda x: 2*x
Percebe como tudo fica muito mais simples? pois é, eu utilizei isso no meu código através do próprio sort() passando key= como parâmetro.
O key= define apenas o modo como o sort() vai organizar os itens da lista. Como eu fiz isso?

 pessoas.sort(key=lambda p: p[1]) 
Dentro do parâmetro, fiz a seguinte definição: 
para cada valor p que percorrerá a lista pessoas, retorne o p[1], isto é, retorne as idades. Isso faz p percorrer a lista pessoas e retornar as sublistas na ordem da menor pra maior idade.

