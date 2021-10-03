#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>




int main(int argc, string argv[])
{
    int letters[26];
    if (argc == 2 && strlen(argv[1]) == 26)
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (argv[1][i] == letters[j])
                {
                    printf("Key must not contain repeated letters.\n");
                    return 1;
                }
                
                else if (!((argv[1][i] >= 'a' && argv[1][i] <= 'z') || (argv[1][i] >= 'A' && argv[1][i] <= 'Z')))
                {
                    printf("Key must contain only letters.\n");
                    return 1;
                }
            }
            
            letters[i] = argv[1][i];
        }
   
   
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");
        for (int i = 0, n = strlen(plaintext); i < n; i++)
        {
            int c = plaintext[i];
            if (isupper(plaintext[i]))
            {   
                c -= 65;
                c = argv[1][c];
                char k = (char)c;
                printf("%c", toupper(k));
            }
            else if (islower(plaintext[i]))
            {   
                c -= 97;
                c = argv[1][c];
                char k = (char)c;
                printf("%c", tolower(k));
            }
            else
            {
                char k = (char)c;
                printf("%c", k);
            }
        }
        printf("\n");
        return 0;
    }
    else if (argc == 2 && strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    
    
    
}

