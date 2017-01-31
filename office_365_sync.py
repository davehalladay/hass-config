from O365 import Schedule
import sqlite3
from time import mktime
from datetime import datetime
from os import environ

db_name = "office_365_cal.db"

conn = sqlite3.connect(db_name)

user_name = environ.get("OFFICE_USER_NAME")
password = environ.get("OFFICE_PASSWORD")

schedule = Schedule((user_name, password))
cal = schedule.getCalendars()
for calendar in schedule.calendars:
    event = calendar.getEvents()
    for event in calendar.events:
        try:
            with conn:
                subject = event.getSubject()
                start_time = datetime.fromtimestamp(mktime(event.getStart()))
                end_time = datetime.fromtimestamp(mktime(event.getEnd()))
                show_as = event.toJson()['ShowAs']
                conn.execute('insert into cal values(?, ?, ?, ?)', (subject, start_time, end_time, show_as))
        except sqlite3.IntegrityError:
            pass
    conn.commit()

