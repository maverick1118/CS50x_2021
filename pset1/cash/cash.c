#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float total;
    int coins = 0;

    do
    {
        total = get_float("Change owed: ");
    }
    while (total < 0);
    total = round(total * 100);


    for (int i = 0; total >= 25; i++)
    {
        total = total - 25;
        coins++;
    }
    for (int i = 0; total >= 10; i++)
    {
        total = total - 10;
        coins++;
    }
    for (int i = 0; total >= 5; i++)
    {
        total = total - 5;
        coins++;
    }
    for (int i = 0; total >= 1; i++)
    {
        total = total - 1;
        coins++;
    }


    printf("%i\n", coins);

}
