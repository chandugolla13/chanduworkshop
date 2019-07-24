#include <stdio.h>

int main()
{
    int arr[50],n,i,j;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n-1;j++)
        {
            if(arr[i]==arr[j])
            {
                printf("%d ",arr[i]);
            }
        }
    }
    return 0;
}
