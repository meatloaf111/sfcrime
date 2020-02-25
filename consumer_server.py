from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         consumer_timeout_ms=1000)

consumer.subscribe("org.sf.pdcalls")

for message in consumer:
    print(message.value)