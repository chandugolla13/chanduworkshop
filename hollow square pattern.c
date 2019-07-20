#include <stdio.h>

/*
Program to swap 1st and 2nd bit of hexadecimal value stored in data variable
*/

int main()
{
    int i,j,n;
    scanf("%d",&n);
    for(i=1;i<n;i++)
    {
        for(j=1;j<n;j++)
        {
            if(i==1 || i==n-1 || j==1 || j==n-1)
                printf("%d",i);
            else
            printf(" ");
        }
        printf("\n");
    }

    return 0;
}

