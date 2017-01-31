import sqlite3

table_create_query = '''
create table cal (
  subject text,
  start_time timestamp,
  end_time timestamp,
  show_as text,
  primary key (subject, start_time)
)
'''
db_name = "office_365_cal.db"

conn = sqlite3.connect(db_name)
conn.execute(table_create_query)