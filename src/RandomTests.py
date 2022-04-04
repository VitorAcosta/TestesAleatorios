from modules.KeyConverter import KeyConverter

class RandomTests():
  def __init__(self):
    self.FILENAME = "src/keys.txt"
    self.keys = []
    self.kc = KeyConverter()

  def read_keys(self, filename, return_type_expected):
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
    pass

  def poker_test(self):
    pass

  def run_test(self, long_run = False):
    print(long_run)

rt = RandomTests()
a = rt.read_keys("src/keys.txt","binary")
print(a[-1])
