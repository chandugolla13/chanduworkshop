#include<stdio.h>

int main()
{
    int n,a,b,fpower=10000,spower=1,digit,i;
    scanf("%d",&n);
    while(n>0)
    {
      digit=n%10;
      b++;
      n=n/10;
    }
    for(i=1;i<=a;i++)
    {
        a=n/fpower;
        if(n>9)
        {
        a=a%spower;
        }
        else
        {
        
        if(a%2==0)
        {
            a++;
            printf("%d",a);
        }
        else
        {
            a--;
            if(a==0)
            {
                
            }
            else
            {
            printf("%d",a);
            }
        }
        }
        fpower=fpower/10;
        spower=spower*10;
    }
return 0;
}

