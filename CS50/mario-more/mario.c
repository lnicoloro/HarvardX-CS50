#include <cs50.h>
#include <stdio.h>
#include <string.h>

void PrintLevel(int step, int height)
{
    if (step == height) return;

    // step is 0 base
    int white_space = height - step - 1;
    // printf("%i", white_space);
    // add white space to enter
    for (int _ = 0; _ < white_space; _++) printf("%c", ' ');

    // left step
    for (int _ = 0; _ < step + 1; _++) printf("%c", '#');

    // middle
    printf("%s", "  ");

    // right step
    for (int _ = 0; _ < step + 1; _++) printf("%c", '#');

    printf("\n");
    // PrintLevel(step + 1, height);
}

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height <= 0 || height > 8);

    // PrintLevel(0, height);

    for (int row = 0; row < height; row++)
    {
        PrintLevel(row, height);
        // for (int space = 0; space < height - row - 1; space++)
        // {
        //     printf(" ");
        // }

        // for (int column = 0; column <= row; column++)
        // {
        //     printf("#");
        // }

        // printf("  ");

        // for (int column = 0; column <= row; column++)
        // {
        //     printf("#");
        // }

        // printf("\n");

    }
}

