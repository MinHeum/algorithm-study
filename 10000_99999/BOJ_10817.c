#include <stdio.h>
int main(){
	short arr[3]={}, t;
	scanf("%d %d %d",&arr[0],&arr[1],&arr[2]);
	if(arr[0]<arr[1])
	{
		t=arr[0];
		arr[0]=arr[1];
		arr[1]=t;
	}
	if(arr[1]<arr[2])
	{
		t=arr[1];
		arr[1]=arr[2];
		arr[2]=t;
	}
	if(arr[0]<arr[1])
	{
		t=arr[0];
		arr[0]=arr[1];
		arr[1]=t;
	}
	printf("%d",arr[1]);
}
