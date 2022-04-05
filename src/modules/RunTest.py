class RunTest():
  def __init__(self):
    self.current_lenghts = {
      "1": 0,
      "2": 0,
      "3": 0,
      "4": 0,
      "5": 0,
      "6+": 0
    }

    self.valid_lenghts = {
      "1": [2267, 2733],
      "2": [1079, 1421],
      "3": [502, 748],
      "4": [223, 402],
      "5": [90, 223],
      "6+": [90, 223]
    }

  def test(self, key, long_run = False):
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
      long_run (bool): Se o tipo de Run Test é long run.

    Returns:
      None 
    """
    previous_char = ""
    curr_char = ""
    seq_len = 0

    for char in key:
      
      curr_char = char
      
      # Primeiro caractere lido
      if previous_char == "":
        previous_char = curr_char

      if previous_char == curr_char:
        seq_len += 1

      else:
        if seq_len >= 6:
          self.current_lenghts["6+"] += 1
          previous_char = curr_char
        else:
          self.current_lenghts[str(seq_len)] += 1
          previous_char = curr_char
        seq_len = 1

        
  def get_results(self):
    """Retorna as contagens, indexadas pelas quantidades.
    A partir das quantidades de avaliação (a saber, 1, 2, 3, 4, 5 e 6+),
    retorna as quantidades de bits.

    Args:
      None
    Returns:
      current_lenghts (dict): Dicionário indexado pela quantidade de
      bits contados. Sendo que em sequências maiores ou iguais a 6 bits
      é categorizado como 6+ no dicionário.
    """
    return self.current_lenghts

  def has_passed(self):
    """Verifica se a última chave testada passou no teste.
    A partir dos tamanhos das rodadas (chave do dicionário)
    e a quantia contada (valores do dicionário) é avaliada
    se a quantia está nos intervalos pré-definidos para a 
    avaliação.

    Args:
      None

    Returns:
      (bool): True caso a última chave testada passou no teste.
              False caso a útlima chave testada não passou no teste.
    """
    valid_count = 0
    for key,value in self.current_lenghts.items():
      if (value >= self.valid_lenghts[key][0] and 
            value <= self.valid_lenghts[key][1]):
        valid_count += 1
    
    return valid_count == 6
  
  def clear_key_dict(self):
    """Limpa o dicionário de teste.
    
    """
    # Zera o dicionário atual para nova avaliação
    for key in self.current_lenghts.keys():
      self.current_lenghts[key] = 0


