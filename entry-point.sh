#!/bin/bash

# turn on bash's job control
set -m

# run python and put it in the background
cd /app/python
python3 server.py &

# now run node
cd /app/node
node index 