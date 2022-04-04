class KeyConverter:
  def __init__(self):
    pass
  def convert_hex_to_binary(self, key):
    """Método de conversão de uma chave string hexadecimal para binário.
    Através de uma chave hexadecimal do tipo string, é feita a conversão
    para binário.

    Args:
      key: Chave hexadecimal do tipo string.
    
    Return:
      binary_line (str): Chave convertida para binário.
    """
    num_key = int(key, 16)
    binary_line = str(bin(num_key))[2:]
    return binary_line
