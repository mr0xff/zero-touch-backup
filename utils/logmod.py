from utils.system_timer import get_current_datetime as getcd

class LogModule: 
  def __init__(self, filename, stdout = True): 
    self.filename = filename
    self.stdout = stdout
    self.__open_file()
    self.levels = { "info", "warn", "error" }
  
  def __open_file(self):
    # fazer a abertura do arquivo e os devidos teste se o arquivo existe...
    m = MessageLog(f"arquivo {self.filename} aberto").info()
    print(m)

  def write(self, message, level = "info"):
    
    m = self.__log_level(message, level)

    print(m)

  def __log_level(self, message, level = "info"):
    match level:
      case "error":
        return MessageLog(message).info()
      case "warn":
        return MessageLog(message).warn()
      case _:
        return MessageLog(message).info()


class MessageLog: 
  def __init__(self, message):
    self.mesage = message

  def info(self, def_label = "info"):
    dt = getcd()
    return f"[{dt["date"]} {dt["time"]}] [{def_label}] {self.mesage}"
  
  def warn(self, def_label = "warn"):
    dt = getcd()
    return f"[{dt["date"]} {dt["time"]}] [{def_label}] {self.mesage}"

  def error(self, def_label = "error"):
    dt = getcd()
    return f"[{dt["date"]} {dt["time"]}] [{def_label}] {self.mesage}"
  

