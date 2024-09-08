#include <stdio.h>
#include <cs50.h>
#include <stdint.h>


int main(int argc, string argv[])
{
    // check file is included in command
    if (argc != 2)
    {
        printf("Error\n");
        return 1;
    }

    // open the file
    string file_name = argv[1];
    FILE *pdf = fopen(file_name, "r");

    // check if file exsits
    if (pdf == NULL)
    {
        printf("No file found\n");
        return 1;
    }

    uint8_t buffer[4];

    uint8_t signature[] = {37, 80, 68, 70};        //file signature for a pdf

    fread(buffer, 1, 4, pdf);     //reading the first four  1 bytes blocks from pdf
    for (int i = 0; i < 4; i++)
    {
        if (buffer[i] != signature[i])      // check if file matches pdf signature
        {
            printf("not a pdf\n");
            fclose(pdf);
            return 0;
        }
    }
    printf("pdf\n");
    fclose(pdf);
    return 0;
}