# Kafka consumer placeholder. Run as separate process or in worker.
# Subscribes to tenant/billing/audit events and acts (e.g. update cache, sync subscription).

import os

KAFKA_BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")


def run_consumer():
    # TODO: aiokafka or confluent_kafka consumer loop
    # Topics: audit_events, subscription_events (placeholder names)
    pass


if __name__ == "__main__":
    run_consumer()
