from time import ctime
from time import strptime
from datetime import date

def get_current_datetime():
  datetime = strptime(ctime())

  return {
    "date": date.today().isoformat(),
    "time": ':'.join([str(datetime.tm_hour), str(datetime.tm_min)])
  }