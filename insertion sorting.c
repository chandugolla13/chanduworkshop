#include<stdio.h>
int main()
{
    int arr[]={12,14,23,7,62,19,20},n=7,safe,index,print,compare;
    int shift;
    for(index=1;index<=n-1;index++)
    {
        for(compare=0;compare<=index-1;compare++)
        {
            if(arr[compare]>arr[index])
                break;
        }
        safe=arr[index];
        for(shift=index;shift>=compare+1;shift--)
            arr[shift]=arr[shift-1];
        arr[compare]=safe;
    }
        for(index=0;index<n;index++)
        {
            printf("%d\t",arr[index]);
        }
    return 0;
}

