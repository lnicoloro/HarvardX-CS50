#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

string plaintext;
char ciphertext;

int main(int argc, string argv[])
{
    // check for two arguments
    if ( argc != 2)
    {
        printf("Usage: ./caeser key\n");
        return 1;
    }

    // check second aRGUMENT IS A NUMBER
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if  (! isdigit(argv[1][i]))
        {
            printf("Usage: ./caeser key\n");
            return 1;
        }
    }

    // convert key from string to int
    int key = atoi(argv[1]);

    //get plaintext from user
    plaintext = get_string("plaintext: ");

    //conversion form plaintext to ciphertext
    printf("ciphertext: ");

    for (int n = 0; n < strlen(plaintext); n++)
    {
        if (isupper(plaintext[n]))
        {
            ciphertext = (plaintext[n] - 65 + key) % 26 + 65;
            printf("%c", ciphertext);
        }

        else if (islower(plaintext[n]))
        {
            ciphertext = (plaintext[n] - 97 + key) % 26 + 97;
            printf("%c", ciphertext);
        }

        else
        {
            printf("%c", plaintext[n]);
        }
    }

    printf("\n");
}

