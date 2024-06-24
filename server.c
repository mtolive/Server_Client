#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h> // for inet_pton etc.
#include <sys/socket.h>
#include <unistd.h>

#define PORT 18000
#define BUFFER_SIZE 5000
#define SA struct sockaddr



int main(int argc, char **argv){

    int serverfd, clientfd, bytes_received;
    uint8_t buffer[BUFFER_SIZE];
    uint8_t recBuffer[BUFFER_SIZE];
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);

    // Create Socket (internet, TCP)
    if((serverfd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
        perror("socket");
        exit(EXIT_FAILURE);
    }

    // Bind Socket
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(PORT);

    if(bind(serverfd, (SA *) &server_addr, sizeof(server_addr)) < 0){
        perror("Bind Failed");
        close(serverfd);
        exit(EXIT_FAILURE);
    }

    // Listen
    if(listen(serverfd, 10) < 0){
        perror("Listen Failed");
        close(serverfd);
        exit(EXIT_FAILURE);
    }

    printf("Listening on port %d\n", PORT);

    while(1){

        if((clientfd = accept(serverfd, (SA *)&client_addr, &client_addr_len)) < 0){
            perror("Accept Failed");
            continue;
        }

        while((bytes_received = recv(clientfd, recBuffer, BUFFER_SIZE, 0)) > 0){
            recBuffer[bytes_received] = '\0';
            printf("Received: %s\n", buffer);
            send(clientfd, recBuffer, bytes_received, 0);
        }
    }

    close(clientfd);
    return 0;
}