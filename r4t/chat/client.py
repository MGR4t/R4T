import socket
import threading
import os

from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout


def clear():
    os.system(
        "cls" if os.name == "nt" else "clear"
    )


def receive(sock):
    """
    Listen for squeaks from other rats.
    """
    while True:
        try:
            message = sock.recv(1024).decode()

            if not message:
                break

            print(message)

        except:
            break


def start_client(ip, name):

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.connect((ip, 7331))


    # Start listening for other rats
    threading.Thread(
        target=receive,
        args=(sock,),
        daemon=True
    ).start()


    session = PromptSession()


    print()
    print("Commands:")
    print("/exit  leave burrow")
    print("/clear clear screen")
    print()


    while True:
        try:
            # This keeps incoming messages
            # from destroying your input line
            with patch_stdout():
                text = session.prompt("> ")

        except KeyboardInterrupt:
            continue

        except EOFError:
            break


        if text == "/exit":
            break


        if text == "/clear":
            clear()
            continue


        if text.strip() == "":
            continue


        sock.send(
            f"🐀 {name}: {text}".encode()
        )


    sock.close()

    print()
    print("🐾 You left the burrow")