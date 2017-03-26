#include <stdio.h>

void main(){
	char *p = "|\\-/";
	int i=0;
	while(1){
		printf("%c\r",p[i%4]);
		i ++;	
	}



}
