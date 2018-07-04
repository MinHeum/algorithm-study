#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	char a[6]={0};
	int i, j=1, num=0, l=0;
	gets(a);
	l = strlen(a);
	for(i=l-1; i>=0; i--){
		switch(a[i]){
			case '0' :num+=0*j;break;
			case '1' :num+=1*j;break;
			case '2' :num+=2*j;break;
			case '3' :num+=3*j;break;
			case '4' :num+=4*j;break;
			case '5' :num+=5*j;break;
			case '6' :num+=6*j;break;
			case '7' :num+=7*j;break;
			case '8' :num+=8*j;break;
			case '9' :num+=9*j;break;
			case 'A' :num+=10*j;break;
			case 'B' :num+=11*j;break;
			case 'C' :num+=12*j;break;
			case 'D' :num+=13*j;break;
			case 'E' :num+=14*j;break;
			case 'F' :num+=15*j;break;
			default : break;
		}
		j=16*j;
	}
	printf("%d",num);
}
