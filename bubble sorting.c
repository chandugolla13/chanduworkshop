#include<stdio.h>
int main()
{
    int arr[]={12,14,23,7,62,19,20},n=7,temp,index,print;
    int count;
    for(count=1;count<=n-1;count++)
    {
    for(index=0;index<=n-(count+1);index++)
    {
        if(arr[index]>arr[index+1])
        {
            temp=arr[index];
            arr[index]=arr[index+1];
            arr[index+1]=temp;
        }
    }
        for(print=0;print<n;print++)
            printf("%d ",arr[print]);
        printf("\n");
    }

    return 0;
}
