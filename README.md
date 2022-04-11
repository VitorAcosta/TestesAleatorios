# Testes Aleatórios

Para chaves de criptografia, a geração deve conter:
+ Distribuição Uniforme
+ Valores não pedizíveis
+ Cadeia longa e integralmente alcançável

Para isso, o repositório atual aborda os testes de aleatoriedade determinados pela FIPS 140-1. Existem quatro testes que determinam se os requisitos de segurança de uma cadeia de 20.000 bits foram alcançados.

## *1. The Monobit Test*
+ 1. Conte o número de uns em uma corrente de 20.000 bits. Chame essa quantidade de X.
+ 2. O teste é passado se 9.654 < X < 10.346.

## *2. The Poker Test*
+ 1. Divida a corrente de 20.000 bits em 5.000 segmentos contínuos de 4 bit (nible). Conte e aramazena o número de ocorrências de cada um das 16 possibilidades de valores de 4 bit. Chame *f(i)* como o número de cada valor *i* 4 bit onde 0 <= *i* <= 15.
+ 2. Valide a fórmula:
- <img src="https://latex.codecogs.com/gif.latex?X=\frac{16}{5000}\times (\sum_{i=0}^{15}[f(i)]^2) - 5000 " /> 
+ 3. O teste é passado se 1.03 < X < 57.4.

## *3. The Runs Test*
+ 1. Uma passada (*run*) é definida como a sequência máxima de bits consecutivos,de todos um ou todos zero, que são parte de uma corrente de amostra de 20.000 bit. Todas as ocorrências das passadas (para tanto os zeros consecutivos como os uns consecutivos) de tamanho >= 1 na corrente devem ser contados e armazenados.
+ 2. O teste é passado se o número de passadas que ocorrem (de tamanhos 1 até 6+) estão entre o intervalo especificado abaixo:

| **Tamanho da passada** | **Intervalo válido** |
|------------------------|----------------------|
| 1                      | 2.267 - 2.733        |
| 2                      | 1.079 - 1.421        |
| 3                      | 502 - 748            |
| 4                      | 223 - 402            |
| 5                      | 90 - 223             |
| 6+                     | 90 - 223             |

+ Note que passadas de tamanho maior que 6 são agrupadas no grupo '6+'.

## *4. The Long Run Test*
+ 1. Uma passada longa (*long run*) é definida como uma passada de tamanho maior ou igual que 34 (de todos zeros ou uns).
+ 2. Em uma amostra de 20.000 bits, o teste é passado se **não** existem passadas longas.