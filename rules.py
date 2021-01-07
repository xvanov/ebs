
from datetime import datetime
from dateutil.rrule import *

dtstart = datetime(2015, 9, 4)
weekdays = rrule(WEEKLY, byweekday=(MO, TU, WE, TH, FR), dtstart=dtstart)
laborday = rrule(DAILY, dtstart=datetime(2015, 9, 7), count=1)
offsite_training = rrule(DAILY, dtstart=datetime(2015, 9, 10), count=4)

rules = [
        (laborday,  0),
        (offsite_training, 3),
        (weekdays,  8),
]

