#include <stdio.h>
int main(){
	int n,result,i,j;
	scanf("%d", &n);
		for(j=0; j*3<=n; j++){
		for(i=0; j*3+i*5<=n; i++){
			if(i*5+j*3==n)
				{
				result=i+j;
				goto clear;
			}
			else
				result=-1;				
		}
	}
	clear:
	printf("%d", result);
}
