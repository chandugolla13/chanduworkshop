#include <stdio.h>

int main() 
{
  int A,B,C,ans;
  printf("Enter the three numbers: ");
  scanf("%d%d%d",&A,&B,&C);
    ans=A;
    while(ans>C && ans!=C)
    {
      ans=ans-B;
    }
  
    if(ans==C)
    {
       printf("YES");
    }
    else
    {
       printf("NO");
    }
  
return 0;
}
