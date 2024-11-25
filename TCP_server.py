import socket

def start_server():
    """
    @brief Starts the TCP server that listens for incoming client connections.
    
    This function initializes the server to listen on IP address '192.168.0.120' and port 1500.
    It handles incoming connections by receiving raw data, converting it to a hexadecimal 
    format, printing the data, and sending a response back to the client.
    
    @return None
    """
    
    # Define server address and port
    host = '192.168.0.110'  # Server's IP address
    port = 1500  #Port to bind the server socket to

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """
      @brief Binds the server socket to the specified IP address and port.
      
      This step prepares the server to listen for incoming client connections on the given 
      IP address and port number.
      
      @param host The IP address on which the server listens.
      @param port The port number the server binds to.
     
      @return None
    """
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(5)  #The server can handle up to 5 incoming connections at once
    print(f"Server listening on {host}:{port}...")

    # Accept connections from clients
    while True:
        # Wait for a client connection
        client_socket, client_address = server_socket.accept()

        """
          @brief Handles the communication with a client that has connected to the server.
          
          Once a client connects, the server receives data in raw byte format. The server then
          converts the data to a hexadecimal format and prints it to the console. Afterward, the
          server sends a response back to the client.
          
          @param client_socket The socket through which the communication occurs.
          @param client_address The IP address and port of the client.
          
          @return None
        """
        print(f"Connection from {client_address}")

        try:
            # Receive the data from the client (assuming the data is in raw bytes)
            data = client_socket.recv(1024)

            """
              @brief Converts the received byte data to a hexadecimal string with spaces between values.
              
              This function processes each byte in the received data, converts it to a two-character 
              hexadecimal representation, and then joins all hexadecimal values with a space.
              
              @param data Raw byte data received from the client.
              
              @return None
            """
            hex_data = ' '.join([f"{byte:02x}" for byte in data])  # Format each byte and join with space
            print(f"Received data in hex: {hex_data}")

            # Optionally, send a response back to the client (in ASCII format)
            ##response = "Data received successfully"
            ##client_socket.send(response.encode('ascii'))
        
        except Exception as e:
            # Handle any errors that occur during communication
            print(f"Error: {e}")
        
        finally:
            # Close the client socket connection
            client_socket.close()

if __name__ == "__main__":
    start_server()
