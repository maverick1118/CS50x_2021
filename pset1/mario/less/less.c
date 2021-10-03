#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;   //Declaration of number of columns of pyramid
    
    //To check input is between 1 and 8
    do
    {
        n  = get_int("Height: ");
    }
    while ((n < 1) || (n > 8));
    
    for (int i = 0; i < n; i++)
    {
        for (int j = n; j > i + 1; j--)//Inserting spaces
        {
            printf(" ");
        }
        for (int k = 0; k <= i; k++)//Making righ-aligned traingle
        {
            printf("#");
        }
        printf("\n");
    }
}