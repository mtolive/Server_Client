import socket

# Define the server address and port
SERVER_IP = '127.0.0.1'
PORT = 18000
BUFFER_SIZE = 5000

def main():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((SERVER_IP, PORT))
        print(f"Connected to server at {SERVER_IP}:{PORT}")

        while True:
            # Get user input
            message = input("Enter message to send (type 'quit' to exit): ")

            # Check if the user wants to quit
            if message.lower() == 'quit':
                break

            # Send the message to the server
            client_socket.sendall(message.encode())
            print(f"Sent: {message}")

            # Receive the server's response
            response = client_socket.recv(BUFFER_SIZE).decode()
            print(f"Received: {response}")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
