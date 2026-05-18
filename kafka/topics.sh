#!/bin/bash

kafka-topics \
  --create \
  --topic weather-events \
  --bootstrap-server kafka:9092 \
  --partitions 1 \
  --replication-factor 1