#include <stdio.h>
int main(){
	short num[9]={};
	short i,j,sum=0,finalsum=0,temp;
	for(i=0; i<9; i++){
		scanf("%d", &num[i]);
		sum += num[i];
	}
	finalsum = sum;
	for (i=0; i<9; i++)
	{
		for (j=i+1; j<9; j++)
		{
			sum = sum-num[i]-num[j];
			if (sum==100)
				break;
			else
				sum = finalsum;
		}
		if (sum==100)
		break;
	}
	num[i] = 0;
	num[j] = 0;
	for (i=0; i<9; i++)
	{
		for(j=0; j<9-i; j++)
		{
			if(num[j]>num[j+1])
			{
				temp = num[j];
				num[j] = num[j+1];
				num[j+1] = temp;
			}
		}
	}
	for(i=3; i<10; i++){
		printf("%d\n", num[i]);
	}
}
