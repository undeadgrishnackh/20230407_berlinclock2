#!/usr/bin/env bash
echo "🎬 start the API on port $1"
nohup uvicorn modules.api.berlin_clock:app --port $1 &
pid=$!
echo "😴 take a small nap to wait the API is reachable"
sleep 3
echo "🕵️‍♀️ check if the API responds to a query at the right address"
curl http://127.0.0.1:$1/1.0.0/getTime\?timestamp\=$2
result=$?
echo "💀 Time to kill the API server"
kill ${pid}
echo "DONE!"
exit ${result}
