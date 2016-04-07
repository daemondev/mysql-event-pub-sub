from pymysqlreplication import BinLogStreamReader
import zmq
import json
from time import sleep

import util as UTIL
import config as CONFIG

# Fetch the latest log_pos
log_pos = UTIL.fetch_latest_log_pos()
# Initialize ZMQ to publish
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % CONFIG.ZMQ_PORT)

print "Publishing starts !!!!! -----------------------------"
while True:
    # Create a stream of the mysqlbinlog
    stream = BinLogStreamReader(connection_settings = CONFIG.CONNECTION_SETTINGS, server_id = CONFIG.SERVER_ID, only_events = CONFIG.EVENTS, log_pos = log_pos)
    latest_log_pos = log_pos
    print "Publishing stream of length " + str(stream.__sizeof__())
    for event in stream:
        data = dict()
        # Collect data
        data['event'] = event.__class__.__name__
        data['table'] = event.table
        data['rows']  = UTIL.stringalise(event.rows)
        data['timestamp'] = str(event.timestamp)
        # Publish !
        socket.send(json.dumps(data))
        latest_log_pos = event.packet.log_pos
    if latest_log_pos == log_pos:
        print "Nothing to publish!"
    log_pos = latest_log_pos
    sleep(CONFIG.REFRESH_TIME)
    stream.close()
