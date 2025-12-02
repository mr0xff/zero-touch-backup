from utils.logmod import LogModule
from utils.system_timer import get_current_datetime

if __name__ == "__main__":
  a = LogModule("log.txt")
  a.write("test", "invalid")
  print(get_current_datetime())

  