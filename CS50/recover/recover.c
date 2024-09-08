#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Error\n");
        return 1;
    }

    char *file = argv[1];
    FILE *raw_file = fopen(file, "r");
    if (raw_file == NULL)
    {
        printf("Could Not Open %s\n", file);
        return 1;
    }

    bool found_jpg = false;
    int count = 0;
    uint8_t buffer[BLOCK_SIZE];
    char jpg_name[8];
    FILE *outptr = NULL;

    while(fread(buffer, BLOCK_SIZE, 1, raw_file) == 1)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (found_jpg)
            {
                fclose(outptr);
            }
            else
            {
                found_jpg = true;
            }
        sprintf(jpg_name, "%03d.jpg", count);

        outptr = fopen(jpg_name, "w");

        if (outptr == NULL)
        {
            fclose(raw_file);
            printf("Could not create %s\n", jpg_name);
            return 1;
        }
        count++;
        }
        if (found_jpg)
        {
            fwrite(buffer, BLOCK_SIZE, 1, outptr);
        }
    }

    fclose(raw_file);
    if (found_jpg)
    {
        fclose(outptr);
    }
    return 0;
}