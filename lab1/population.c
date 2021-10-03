#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start, end = 0;
    // TODO: Prompt for start size
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);


    // TODO: Prompt for end size
    do
    {
        end = get_int("End size: ");
    }
    while (start > end);

    // TODO: Calculate number of years until we reach threshold
    int total = start;
    int years;
    for (years = 0; total < end; years++)
    {
        int born = total / 3;
        int dead = total / 4;
        total = total + born - dead;

    }
    // TODO: Print number of years
    printf("Years: %i \n", years);
}