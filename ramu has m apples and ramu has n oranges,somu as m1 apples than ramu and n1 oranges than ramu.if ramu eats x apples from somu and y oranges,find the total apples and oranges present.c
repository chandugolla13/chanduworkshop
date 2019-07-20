#include <stdio.h>

int main()
{
   int m,n,m1,n1,x,y,ramuapp,ramuorg,somuapp,somuorg;
   scanf("%d%d%d%d%d%d",&m,&n,&m1,&n1,&x,&y);
   ramuapp=m;
   ramuorg=n;
   somuapp=m+m1-x;
   somuorg=n+n1-y;
   printf("%d %d",ramuapp+somuapp,ramuorg+somuorg);
    return 0;
}
