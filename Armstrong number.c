#include <stdio.h>

int main()
{
    int i,n,temp,sum=0,rem;
    scanf("%d",&n);
    temp=n;
    while(n!=0)
    {
        rem=n%10;
        sum=sum+(rem*rem*rem);
        n=n/10;
    }
    if(sum==temp)
    {
        printf("%d is armstrong number",temp);
    }
    else
    {
        printf("%d is not armstrong number",temp);
    }
    return 0;
}

