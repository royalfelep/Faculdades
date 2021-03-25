# Trabalho 1
## Participantes:
  | Nome | Matricula |
  | - | - |
  | Felipe Correa da Cruz | 18/0100530 |
  | Edvan Barreira Gomes Junior | 17/0032591 |
  | Iago de Andrade Sousa | 16/0124701 |
  | Pedro Menezes Rodiguero | 19/0139323 |
  | Eduardo de Souza Felix de Almeida | 17/0102254 |
  
## O Código:
<p> Primeiramente, o código pede ao usuário o nome de um arquivo "dicionario" para ser utilizado (Esse arquivo deve possuir uma palavra por linha). Em seguida, pede o número de outros dois arquivos "texto-de-referencia" (TRA.txt, TRB.txt) para serem análisados em relação ao dicionário. Em seguida, o código cria um arquivo para cada texto de referência (bowA.txt, bowB.txt), no qual imprime todas as palavras do dicionário e ao lado quantas palavras dessas existem no texto de referência usando ponteiros (contA, contB). Depois, ele imprime para o usuário todas as palavras do dicionario, as ocorrências no texto A (contA) e no texto B (contB) em forma de tabela. Por último, o código calcula a distância euclidiana entre os valores dos dois ponteiros "contA" e "contB".

## Notação Big-O, Big-Θ e Big-Ω
| Função(linha) | O | Θ | Ω |
| - | - | - | - |
| Main(21) | O(n) | Θ(n * m * (d + tr)) | Ω(n) |
| calculaBOW(18:22:26:36) | O(n * m * (d + tr)) | Θ(n * m * (d + tr)) | Ω(n * m * (d + tr))
| contaPalavras(10) | O(n) | Θ(n) | Ω(n)
| distanciaEuclidiana(9) | O(n) | Θ(n) | Ω(n)
| retirarPontuacao(10) | O(n) | Θ(n) | Ω(n)
| tabelaDicionario(18) | O(n) | Θ(n) | Ω(n)
