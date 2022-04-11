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

  def monobit_test(self, key, verbose = False):
    """Executa o 'monobit test'.
    """
    return self.run_t.monobit_test(key, verbose)

  def poker_test(self, key, verbose = False):
    """Executa o 'poker test'.
    """
    return self.run_t.poker_test(key, verbose)
    

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
  answer = ""
  verbose = int(input("Obter resultado completo?\n(i.e. opção verbose)\n[0]-Não\n[1]-Sim\n>"))
  output_file = open("RandomTestsOutputs.txt","w")
  rt = RandomTests()
  keys = rt.read_keys("src/keys.txt","binary")

  for idx, key in enumerate(keys):
    m_test = rt.monobit_test(key, verbose)
    p_test = rt.poker_test(key, verbose)
    r_test = rt.run_test(key, verbose)
    lr_test = rt.long_run_test(key)


    if verbose:
      approved = m_test[0] and p_test[0] and r_test[0] and lr_test 
      answer += f"""=====================================
      Chave {idx+1} - Aprovado: {approved}
      Monobit: {m_test[0]}
      \t>Count: {m_test[1]}\n  
      Poker: {p_test[0]}
      \t>Valor (X): {p_test[2]}
      \t>Count: {p_test[1]}\n                
      The Run Test: {r_test[0]}
      \t>Bits 1 count:{r_test[1]}
      \t>Bits 0 count:{r_test[2]}\n     
      Long Run Test: {lr_test}
      """
    else:
      approved = m_test and p_test and r_test and lr_test 
      answer += f"""=====================================
      Chave {idx+1} - Aprovado: {approved}
      Monobit: {m_test}  
      Poker: {p_test}        
      The Run Test: {r_test}         
      Long Run Test: {lr_test}
      """

  print(answer)
  print("Escrevendo arquivo...")
  output_file.write(answer)
  print("Arquivo finalizado")
  output_file.close()




