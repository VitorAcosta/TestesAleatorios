import itertools as itr

class RunTest():
  def __init__(self):
    self.valid_lenghts = {
      "1": [2267, 2733],
      "2": [1079, 1421],
      "3": [502, 748],
      "4": [223, 402],
      "5": [90, 223],
      "6+": [90, 223]
    }

  def the_run_test(self, key, verbose = False):
    """Método para execução do 'The Runs Test'.
    Através de uma determinada chave, é realizado o teste 
    'The Runs Test':
      Conta-se a quantidade de bits consecutivos, todos um ou todos zero,
      e salva a contagem no dicionário de avaliação, indexado pelas quantidades
      1, 2, 3, 4, 5 e 6+.
      O teste passa caso as contagens estejam nos intervalos definidos 
      (@see has_passed).      

    Args:
      key (str): Chave para ser testada nos parâmetros do teste.
      verbose (bool): Se o retorno do teste será verboso, apresentando
                      também a quantia de bits que foram distribuídas
                      entre 1, 2, 3, 4, 5 e 6+.

    Returns:
      Caso o argumento verbose é verdadeiro, o retorno é:
      (bool, dict, dict): Retorno informando em [0] se o teste passou,
                          [1] o dicionário de contagens de bits 1, e,
                          [2] o dicionário de contagens de bits 0.
      Caso contrário:
      (bool): Teste passou ou não.
    """
    seq_len = 0

    count_zero = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6+": 0}
    count_one = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6+": 0}

    for i, j in itr.groupby(key):
      seq_len = len(list(j))
      if i == "0":
        if seq_len >= 6:
          count_zero["6+"] += 1
        else:
          count_zero[str(seq_len)] += 1
      else:
        if seq_len >= 6:
          count_one["6+"] += 1
        else:
          count_one[str(seq_len)] += 1
    
    if self.__has_passed(count_one) and self.__has_passed(count_zero):
      return_value = (True, count_one, count_zero) if verbose else True
    else:
      return_value = (False, count_one, count_zero) if verbose else False
    
    return return_value
    

  def __has_passed(self, current_lenghts):
    """Método privado que verifica se a chave testada passou no run test.
    A partir dos tamanhos das rodadas (chave do dicionário)
    e a quantia contada (valores do dicionário) é avaliada
    se a quantia está nos intervalos pré-definidos para a 
    avaliação.

    Args:
      current_lenghts (dict): Dicionário que mapeia os valores de bits um
              ou zero contados nas chaves 1,2,3,4,5 e 6+.

    Returns:
      (bool): True caso a chave testada passou no teste.
              False caso a chave testada não passou no teste.
    """
    valid_count = 0
    for key,value in current_lenghts.items():
      if (value >= self.valid_lenghts[key][0] and 
            value <= self.valid_lenghts[key][1]):
        valid_count += 1
    
    return valid_count == 6


  def long_run_test(self, key):
    """Método que realiza o teste de long run para uma chave dada.
    A partir de uma chave binária, é realizado o teste 'Long Run test':
      Uma 'long run' é uma passada de tamanho 34 ou mais, de todos bits
      zeros ou um. Em uma amostra de 20.000 bits, o teste
      é passado caso não exista uma 'long run'.

    Args:
      key (str): Chave binária que passará pelo 'long run test'.

    Returns:
      (bool): True caso a chave passe pelo teste.
              False caso da chave não passe pelo teste.
    """
    for _, j in itr.groupby(key):
      if len(list(j)) >= 34:
        return False
    return True



