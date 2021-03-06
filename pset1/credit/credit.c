#include <stdio.h>



int len(long long n)
{
    int i = 0;
    while (n > 0)
    {
        n = n / 10;
        i++;
    }
    return i;
}

int calc(long long n)
{
    int sum1 = 0;
    int sum2 = 0;
    long long x = n;
    int total = 0;
    int mod1;
    int mod2;
    int d1;
    int d2;
    do
    {
        // Remove last digit and add to sum1
        mod1 = x % 10;
        x = x / 10;
        sum1 = sum1 + mod1;
        // Remove second last digit
        mod2 = x % 10;
        x = x / 10;
        // Double second last digit and add digits to sum2
        mod2 = mod2 * 2;
        d1 = mod2 % 10;
        d2 = mod2 / 10;
        sum2 = sum2 + d1 + d2;
    }
    while (x > 0);
    total = sum1 + sum2;
    return total;
}

const char *check(long long num)
{
    //Getting starting digits
    long long start = num;
    do
    {
        start = start / 10;
    }
    while (start > 100);

    // Next check starting digits for card type
    if ((start / 10 == 5) && (0 < start % 10 && start % 10 < 6))
    {
        return ("MASTERCARD\n");
    }
    else if ((start / 10 == 3) && (start % 10 == 4 || start % 10 == 7))
    {
        return ("AMEX\n");
    }
    else if (start / 10 == 4)
    {
        return ("VISA\n");
    }
    else
    {
        return ("INVALID\n");
    }

}

int main(void)
{
    long long num = 0;
    printf("Number: ");
    scanf("%lld", &num);
    int total = 0;
    // Check if length is valid
    int i = len(num);
    if (i != 13 && i != 15 && i != 16)
    {
        printf("INVALID\n");
        return 0;
    }
    total = calc(num);
    if (total % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    printf("%s", check(num));

}