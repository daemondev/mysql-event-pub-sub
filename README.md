## MySQL event Publish Subscribe
This script listens to MySQL events. Every write/update action is emitted as an event which can be used for various purposes. The event is recorded in a binary log file, which is used for master slave replication as well. Here it has been used to save data into MongoDB. But it can be used to send push notifications too.

## Installation
`pip install -r requirements.txt`

ZMQ, MongoDB, MySQL packages have been used. ZMQ is used so that the events can be stored and published sequentially for each client. Pub-Sub model of zmq manages the queue and messaging internally.

## Setting up MySQL
A sample `my.cnf` has been provided but it should be configured properly. Read more about it. Settings at row level, table specific with TTL for logs etc. can be easily configured. Don't forget to restart the mysql server to see the effects. Logs are used to replicate in case master slave is being used. Hence avoid deleting logs abrubtly.

## How-to
Run the client and server. For each collection/table, the events should be handled separately. In the client, I have simply written the data into mongodb collection with same name as the table's name.

PyMySQL is used to parse bin-logs. It may be slightly buggy. Goodluck !
