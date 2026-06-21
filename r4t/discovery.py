import socket
import threading


DISCOVERY = 7330
CHAT = 7331


def host_discovery():

    def listen():

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        sock.bind(("", DISCOVERY))


        while True:

            data, addr = sock.recvfrom(1024)

            if data.decode() == "RAT?":

                sock.sendto(
                    b"BURROW",
                    addr
                )


    threading.Thread(
        target=listen,
        daemon=True
    ).start()


def find_burrow():

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_BROADCAST,
        1
    )

    sock.settimeout(2)


    try:

        sock.sendto(
            b"RAT?",
            ("255.255.255.255", DISCOVERY)
        )

        _, addr = sock.recvfrom(1024)

        return addr[0]


    except:
        return None