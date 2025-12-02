class LogModule: 
  
  def __init__(self, filename, stdout = False): 
    self.filename = filename
    self.stdout = stdout
    self.__open_file()
  
  def __open_file(self):
    # fazer a abertura do arquivo e os devidos teste se o arquivo existe...
    m = MessageLog(f"arquivo {self.filename} aberto").info()
    print(m)

class MessageLog: 
  def __init__(self, message):
    self.mesage = message

  def info(self):
    return f"[info] {self.mesage}"
  
  def warn(self):
    return f"[warn] {self.mesage}"

  def error(self):
    return f"[error] {self.mesage}"  

