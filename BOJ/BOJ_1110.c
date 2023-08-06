#include<stdio.h>
int main(){
	int n,temp,count=0;
	scanf("%d",&n);
	temp=n;
	do{
		if(n<10){
			n = n+n*10;
			count++;
		}
		else{
			n = (n%10)*10+(n+n/10)%10;
			count++;
		}	
	}while(temp!=n);
	printf("%d",count);
}
