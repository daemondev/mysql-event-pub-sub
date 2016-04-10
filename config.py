from pymysqlreplication.row_event import ( DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent, )

CONNECTION_SETTINGS = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'passwd': 'goodluck'}
SERVER_ID = 1 # check /etc/my.cnf
EVENTS = [DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent]
REFRESH_TIME = 3 # seconds
ZMQ_PORT = 5556
