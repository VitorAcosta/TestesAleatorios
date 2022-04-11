from modules.KeyConverter import KeyConverter
from modules.RunTest import RunTest

class RandomTests():
  def __init__(self):
    self.FILENAME = "src/keys.txt"
    self.keys = []
    self.kc = KeyConverter()
    self.run_t = RunTest()

  def read_keys(self, filename, return_type_expected = None):
    """Método que lê as chaves dadas.
    A partir de um arquivo de chaves, realiza a leitura
    sequencial e, se desejado, pode transformar as chaves
    em binário.

    Args:
      filename (str): Nome do arquivo de chaves + extensão do arquivo
      return_type_expected (str): Tipo de retorno das linhas lidas esperado:
                Digite "binary" para retorno binário, ou deixe vazio para
                retorno das linhas na forma original.
    
    Returns:
      (list): Lista com cada linha lida do arquivo fonte de chaves.
    """
    with open(filename) as rf:
      for line in rf.readlines():
        treated_line = line.replace("\"","").replace("'","").replace("\n","")
        if treated_line != '':
          if return_type_expected == "binary":
            converted_line = self.kc.convert_hex_to_binary(treated_line)
          else:
            converted_line = treated_line

          self.keys.append(converted_line)
      
      return self.keys

  def monobit_test(self):
    """Executa o 'monobit test'.
    """
    pass

  def poker_test(self):
    """Executa o 'poker test'.
    """
    pass

  def run_test(self, key, verbose = False):
    """Executa o 'run test'.

    Args:
      key (str): Chave binária que será avaliada no 'run test'.
      verbose (int): Define o retorno verboso ou não.
              Caso o retorno seja verboso, o dicionário
              de contagem de bits (para os bits 1 e 0)
              são retornados junto com o resultado de
              'Aprovado' ou 'Reprovado' no teste.
    
    Returns:
      Caso o argumento verbose é verdadeiro, o retorno é:
      (bool, dict, dict): Retorno informando em [0] se o teste passou,
                          [1] o dicionário de contagens de bits 1, e,
                          [2] o dicionário de contagens de bits 0.
      Caso contrário:
      (bool): Teste passou ou não.
    """
    return self.run_t.the_run_test(key, verbose)

  def long_run_test(self, key):
    """Executa o 'long run test'.

    Args:
      key (str): Chave binária que será avaliada no 'long run test'.
    
    Returns:
      (bool): Teste passou ou não.
    """
    return self.run_t.long_run_test(key)

if __name__ == "__main__":
  verbose = int(input("Obter resultado completo?\n(i.e. opção verbose)\n[0]-Não\n[1]-Sim\n>"))
  rt = RandomTests()
  keys = rt.read_keys("src/keys.txt","binary")
  for idx, key in enumerate(keys):
    r_test = rt.run_test(key, verbose)
    lr_test = rt.long_run_test(key)

    if verbose:
      print(f"""      =====================================
      Chave {idx+1}                    
      The Run Test: {r_test[0]}
      \t>Bits 1 count:{r_test[1]}
      \t>Bits 0 count:{r_test[2]}\n     
      Long Run Test: {lr_test}
      """)
    else:
      print(f"""      =====================================
      Chave {idx+1}                    
      The Run Test: {r_test}         
      Long Run Test: {lr_test}
      """)


