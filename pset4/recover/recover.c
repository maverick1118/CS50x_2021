#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>


typedef uint8_t BYTE;
const int BUFFER_SIZE = 512;

 
int main(int argc, char *argv[])
{
    //Checks the number of arguments
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    
    //Checks wether the file is valid or not
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 2;
    }
    
    
    //Variables declared
    BYTE buffer[BUFFER_SIZE];
    int counter = 0;
    char filename[8];
    FILE *output = NULL;
    bool jpeg_found = false;
    
    
    //Condition to iterate till the end of memory card
    while (fread(&buffer, sizeof(BYTE), 512, input) == 512)
    {
        //Check for jpg header in each 512 byte block
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {        
            //To check weather jpg is already found or not
            if (jpeg_found == false)
            {
                sprintf(filename, "%03i.jpg", counter);
                output = fopen(filename, "w");
                fwrite(&buffer, sizeof(BYTE), 512, output);
                counter++;
                jpeg_found = true;
            }
            
            
            else if (jpeg_found == true)
            {
                fclose(output);
                sprintf(filename, "%03i.jpg", counter);
                output = fopen(filename, "w");
                fwrite(&buffer, sizeof(BYTE), 512, output);
                counter++;

            }
        }
    
        else if (jpeg_found == true)
        {

            fwrite(&buffer, sizeof(BYTE), 512, output);

        }
    }
    
    //Close all the remaining files
    fclose(input);
    fclose(output);
        

}