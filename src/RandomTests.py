

class RandomTests():
  def __init__(self):
    FILENAME = "src/keys.txt"
    self.keys = []
    self.read_keys(FILENAME)

  def read_keys(self, filename):
    with open(filename) as rf:
      for line in rf.readlines():
        self.keys.append(line)

  def monobit_test(self):
    pass

  def poker_test(self):
    pass
  
  def run_test(self, long_run = False):
    print(long_run)

rt = RandomTests()
