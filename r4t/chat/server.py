import socket
import threading


PORT = 7331

clients = []


def broadcast(message):
    for client in clients.copy():
        try:
            client.send(message.encode())
        except:
            clients.remove(client)


def handle(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            broadcast(message.decode())

        except:
            break

    clients.remove(client)
    client.close()


def start_server():
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind(("", PORT))
    server.listen()

    print("🕳️ Burrow opened")

    while True:
        client, _ = server.accept()

        clients.append(client)

        threading.Thread(
            target=handle,
            args=(client,),
            daemon=True
        ).start()