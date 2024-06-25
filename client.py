import socket

# Define the server address and port
SERVER_IP = '127.0.0.1'
PORT = 18000
BUFFER_SIZE = 5000

def main():
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    try:
        client_socket.connect((SERVER_IP, PORT))
        print(f"Connected to server at {SERVER_IP}:{PORT}")

        while True:
            message = input("Enter message to send (type 'quit' to exit): ")

            if message.lower() == 'quit':
                break

            # Send message to server
            client_socket.sendall(message.encode())
            print(f"Sent: {message}")

            # Receive server response
            response = client_socket.recv(BUFFER_SIZE).decode()
            print(f"Received: {response}")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
