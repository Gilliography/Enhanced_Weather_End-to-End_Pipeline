#!/bin/bash
kafka-topics \
--create \
--topicvweather-events \
--boostrap-server kafka:9092 \
--partitions 1 \
--replication-factor 1
