#include<stdio.h>

int main(void){


structsockaddr_in server_addr;
memset(&server_addr, 0, sizeof(server_addr));
server_addr.sin_faily = AF_INET;
server_addr.sin_port = htons(4000);
server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
if( -1 == connect(clinet_socket, (strct sockaddr*)&server_addr,sizeof(server)addr)))
{
	printf("connection error!\n");
	exit(1);
