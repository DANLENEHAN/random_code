import database

import pika
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def server_setup(
    rmq_connection: str = "localhost",
    rmq_queue: str = "harrier",
    db_endpoint: str = "postgresql://localhost/dan"
) -> None:

    connection = pika.BlockingConnection(pika.ConnectionParameters(rmq_connection))
    channel = connection.channel()
    channel.queue_declare(queue=rmq_queue)

    postgres_engine = create_engine(db_endpoint)

    # Sessionmaker is a session factory for creating sessions
    # Using sessionmaker allows us to create sessions without engine
    Session = sessionmaker(postgres_engine)

    # Adding a connection Parameter to the callback function
    server_session = lambda ch, method, properties, message: server(
        Session, ch, method, properties, message
    )

    channel.basic_consume(
        queue=rmq_queue,
        auto_ack=True,
        on_message_callback=server_session
    )

    print(f"**Harrier server now consuming messages on {rmq_queue} queue **")
    channel.start_consuming()


def server(Session, ch, method, properties, message: str) -> None:

    message = json.loads(message)
    print(f"Recieved a '{message[0]}' from Queue")

    if message[0] == "create_user_attempt":
        database.create_user(Session, json.loads(message[1]))


if __name__ == "__main__":
    server_setup()
