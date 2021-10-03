#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>


int count_letters(string n);
int count_words(string n);
int count_sentence(string s);

int main(void)
{
    string text = get_string("Text : ");
    
    int l = count_letters(text);
    int w = count_words(text);
    int s = count_sentence(text);
    float L = (float)(100 * l) / w;
    float S = (float)(100 * s) / w;
    
    
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = (int) round(index);
    
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}








int count_letters(string s)
{
    int counter = 0;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        int c = (int) tolower(s[i]);
        if (c >= 97 && c <= 122)
        {
            counter++;
        }
        else
        {
            counter += 0;
        }
    }
    return counter;

}

int count_words(string s)
{
    int counter = 0;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        int c = (int) tolower(s[i]);
        if (c == 32)
        {
            counter++;
        }
    }
    return counter + 1;
}

int count_sentence(string s)
{
    int counter = 0;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        int c = (int) tolower(s[i]);
        if (c == 33 || c == 46 || c == 63)
        {
            counter++;
        }
    }
    return counter;
}
