#!/bin/sh
node node/index &
cd /app/python
python3 server.py &