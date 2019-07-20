#include <stdio.h>

int main()  
{
  int i,j,n,temp;
  printf("enter the size: ");
  scanf("%d",&n);
  int arr[n];
  printf("enter the array elements: ");
  for(i=0;i<sizeof(arr)/sizeof(arr[0]);i++)
  {
    scanf("%d",&arr[i]);
  }
  for(i=0;i<=n-1;i++)
  {
    for(j=0;j<=n-i-1;j++)
    {
      if(arr[j]>arr[j+1])
      {
         temp =arr[j];
         arr[j]=arr[j+1];
         arr[j+1]=temp;
      }

    }

  }
  printf("Ascending Order: ");
  for(i=0;i<sizeof(arr)/sizeof(arr[0]);i++)
  {
    printf("%d\t",arr[i]);
  }
  printf("\n");
  printf("Desending Order: ");
  for(i=0;i<=n-1;i++)
  {
    for(j=0;j<=n-i-1;j++)
    {
      if(arr[j]<arr[j+1])
      {
         temp =arr[j];
         arr[j]=arr[j+1];
         arr[j+1]=temp;
      }

    }

  }
  for(i=0;i<sizeof(arr)/sizeof(arr[0]);i++)
  {
    printf("%d\t",arr[i]);
  }



  return 0;
}
