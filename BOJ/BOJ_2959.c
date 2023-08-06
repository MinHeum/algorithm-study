#include <stdio.h>
int main(){
	short a[4] = {}, i, j, t;
	for(i=0; i<4; i++){
		scanf("%d",&a[i]);
	}
	for(i=0; i<4; i++){
		for(j=i+1; j<4; j++){
			if(a[i]>a[j])
			{
				t=a[i];
				a[i]=a[j];
				a[j]=t;
			}
		}
	}
	printf("%d\n",a[0]*a[2]);
}
