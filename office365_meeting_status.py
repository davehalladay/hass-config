import sqlite3
from datetime import datetime

db_name = "office_365_cal.db"

conn = sqlite3.connect(db_name)

in_meeting = False
with conn:
    sql = '''
    select subject from cal where start_time < ? and end_time > ? and show_as = 'Busy'
    '''
    current_date = datetime.now()
    cur = conn.cursor()
    cur.execute(sql, (current_date, current_date))
    if cur.fetchone():
        in_meeting = True

print(in_meeting)
