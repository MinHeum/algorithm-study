#include <stdio.h>
#include <stdlib.h>
int main(){
	int A_D, A_H, B_D, B_H;
	scanf("%d %d",&A_D, &A_H);
	scanf("%d %d",&B_D, &B_H);
	do{
		B_H -= A_D;
		A_H -= B_D;
		if(B_H<=0 && A_H>0)
			{
			printf("PLAYER A");
			goto GG;
			}
		else if(A_H<=0 && B_H>0)
			{
			printf("PLAYER B");
			goto GG;
			}
		else if(A_H<=0 && B_H<=0)
			{
			printf("DRAW");
			goto GG;
			}
	}while(1);
	GG:
	return 0;	
}
