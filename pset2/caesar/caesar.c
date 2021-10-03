#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    
    
    if (argc == 2 && isdigit(*argv[1]))
    {
        int key = atoi(argv[1]);
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");
    
    
        for (int i = 0, n = strlen(plaintext); i < n; i++)
        {
            int c = plaintext[i];
            if (isupper(plaintext[i]))
            {   
                c -= 65;
                c = (c + key) % 26;
                c += 65;
                char k = (char)c;
                printf("%c", k);
            }
            else if (islower(plaintext[i]))
            {   
                c -= 97;
                c = (c + key) % 26;
                c += 97;
                char k = (char)c;
                printf("%c", k);
            }
            else
            {
                char k = (char)c;
                printf("%c", k);
            }
    
        }
        printf("\n");
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}