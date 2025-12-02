class LodModule: 
  
  def __init__(self, filename, stdout = False): 
    self.filename = filename
    self.stdout = stdout
    self.__open_file()
  
  def __open_file(self):
    # fazer a abertura do arquivo e os devidos teste se o arquivo existe...
    print(f"open file {self.filename}")

  def info(msg):
    pass
  
  def warn(): 
    pass

  def error():
    pass

class MessageLog: 
  def __init__(self, message):
    self.mesage = message
  

