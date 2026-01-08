#!/bin/bash

cd "$(dirname "$0")"

echo "Producer baslatiliyor..."
source venv/bin/activate
python producer/producer.py &

PRODUCER_PID=$!
echo "Producer PID: $PRODUCER_PID"

sleep 3

echo "Consumer baslatiliyor..."
python consumer/consumer.py &

CONSUMER_PID=$!
echo "Consumer PID: $CONSUMER_PID"

echo ""
echo "Producer ve Consumer calisiyor!"
echo "Durdurmak icin: kill $PRODUCER_PID $CONSUMER_PID"
echo ""
echo "Kibana'ya erisin: http://localhost:5601"

wait
