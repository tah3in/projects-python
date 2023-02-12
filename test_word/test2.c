#include <stdio.h>
#include <stdlib.h>
int main()
{
    // printf("%d",recognition(1));
    // printf("Hello word!\n")
    char a ='c';
    char ch = 's';
    
    printf("%c",a);
    

}
#include <stdio.h>
#include <stdlib.h>
int pow(int,int);
int binary(int);
int recognition(int);
/*int main()
{
    int number=101;
    printf("%i\n",number);
    printf("Hello mostafa welcome to my page\n");
    int myNum = 5;
    char myLetter = 'D';
    printf("My number is %d and my letter is %c", myNum, myLetter);
    printf("Hello My number : %d")

}
*/

int main()
{
    printf("%d",recognition(10));
    // printf("Hello word!\n")

}

int binary(int number)
{   int i=0;
    char bin[0]="";
    while(recognition(number)!= 0 || recognition(number)==1)
    {   
        if (recognition(number)<number)
            {
                number-recognition(number);
                bin[i]="1";
                i++;
            }
        else{
            
        }
    }

    
}
int pow(int number,int power)
{   int a=1;
    if(power==0)
        return 1;
    for(int i=0;i<power;i++)
    {   
        a*=number;
    }
    return a;
}
int recognition(int number)
{int i=0;
    // printf("\npow:%d\n",pow(2,3));
    while(pow(2,i)<number)
    {
        i++;
        printf("\ni : %d ,pow : %d\n",i,pow(2,i));
    }
    return pow(2,i-1);

}
