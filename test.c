#include <stdio.h>
#include <stdlib.h>

int check(int i){
    i = (i == 0) ?  1 : 0;
    return i;
}

int main()
{
    int a = 1;
    printf("%d", check(a));
    return 0;
}