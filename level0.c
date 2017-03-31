#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>

//Had trouble with this one for sure, had to brush up on my networks...

#define HOST_NAME "semtex.labs.overthewire.org"
#define PORT_NUM "24000"

int main(int argc, char *argv[]) {

    int sockfd;
    int status;
    struct addrinfo address, *addrinfo, *temp;
    memset(&address, 0, sizeof(address));
    address.ai_family = AF_INET;
    address.ai_socktype = SOCK_STREAM;
    
    status = getaddrinfo(HOST_NAME, PORT_NUM, &address, &addrinfo);
    if (status != 0) {
        printf("Failed address retrieval\n");
        exit(1);
    }
    for (temp = addrinfo; temp != NULL; temp=temp->ai_next) {
        sockfd = socket(temp->ai_family, temp->ai_socktype, temp->ai_protocol);
        if (sockfd == -1) {
            printf("Socket failure\n");
            exit(1);
        } else {
            break;
        }
    }
    status = connect(sockfd, addrinfo->ai_addr, addrinfo->ai_addrlen);
    if (status == -1) {
        printf("connection error\n");
        exit(1);
    }
    
    int num_read = 0;
    int len = 0;
    int fd;
    fd = open("Level_0", O_RDWR);
    char c;
    int i, j;
    for(i = 1, j = 0; ; i++, j++) {

        num_read = read(sockfd, &c, 1);
        if (i % 2 == 0) continue; //skip second byte
        if (num_read == 0) break;
        write(fd, &c, 1);

    } 
}
    
    
    
    














