import socket

def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN on {host}")
        else:
            print(f"Port {port} is CLOSED on {host}")

        sock.close()

    except Exception as e:
        print("Error:", e)

# User Input
host = input("Enter IP address or hostname: ")
port = int(input("Enter port number: "))

check_port(host, port)