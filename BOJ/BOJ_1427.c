#include <stdio.h>
#include <string.h>
int main(){
	char a[10]={};
	int i,j,t;
	scanf("%s",&a);
	for(i=0; i<strlen(a); i++)
		for(j=0; j<strlen(a)-i-1; j++)
		{
			if(a[j]<a[j+1])
			{
			t=a[j];
			a[j]=a[j+1];
			a[j+1]=t;
			}
		}
		printf("%s",a);
}
