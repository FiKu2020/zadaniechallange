
import time
import datetime


midnight = "00:00"
date_format = datetime.datetime.strptime(midnight,
                                         "%H:%M")

unix_time = datetime.datetime.timestamp(date_format)