import sys
import zmq
import json
from pymongo import MongoClient

port = "5556"

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

# mongo connection
connection = MongoClient()
db = connection.testdb

print "Collecting updates from weather server..."
socket.connect ("tcp://localhost:%s" % port)
socket.setsockopt(zmq.SUBSCRIBE, '')
while True:
    string = socket.recv()
    data = json.loads(string)
    if data['event'] == 'WriteRowsEvent':
        table = data['table']
        db[table].insert(data['rows'][0]['values'])
