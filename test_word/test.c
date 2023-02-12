#include<stdio.h>
#include<stdlib.h>
int binary(int);
int main()
{
    printf("%c",binary(10));
}
int binary(int number)
{   int i=0;
    int list1[];
    int bin=0;
    do
    {   
        bin+=number%2;
        list[]=bin;
        i++;
        number/=2;
    }

    while(number!=1);
    
}