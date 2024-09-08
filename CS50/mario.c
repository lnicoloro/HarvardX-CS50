#include <stdio.h>
#include <cs50.h>

//////////////////// horizontal
// int main(void)
// {
//     for (int i = 0; i < 4; i++)
//     {
//         printf("#");
//     }
//     printf("\n");
// }

//////////////////// veritcal
// int main(void)
// {
//     for (int i = 0; i < 4; i++)
//     {
//         printf("#\n");
//     }
// }

//////////////////// rectanlge
// int main(void)
// {
//     for (int i = 0; i < 4; i++)         /////vertical
//     {
//         for (int j = 0; j < 15; j++)     ////horizontal
//         {
//             printf("#");
//         }
//         printf("\n");
//     }
// }

//////////////////// square
// int main(void)
// {
//     const int n = 4;                    /////const will make n always be what it is equal to in that line
//     for (int i = 0; i < n; i++)
//     {
//         for (int j = 0; j < n; j++)
//         {
//             printf("#");
//         }
//         printf("\n");
//     }
// }

//////////////////// do while loop
// int main(void)
// {
//     // Get size of grid
//     int n;
//     do
//     {
//         n = get_int("Size: ");
//     }
//     while (n < 0);

//     // Print grid of bricks
//     for (int i = 0; i < n; i++)
//     {
//         for (int j = 0; j < n; j++)
//         {
//             printf("#");
//         }
//         printf("\n");
//     }
// }





// FUNCTIONS BB


// int get_size(void);             ////// alerts compiler to look further down code for these functions
// void print_grid(int size);

// int main (void)
// {
//     // Get sieze of grid
//     int n = get_size();

//     // Print grid
//     print_grid(n);
// }



// //////////////////// function that will get user input for square size
// int get_size(void) /////// FUNCTION( OOUTPUT: int,  NAME: get_size, INPUT: (void) means no input)
// {
//     int n;
//     do
//     {
//         n = get_int("Size: ");
//     }
//     while (n < 1);
//     return n;
// }


// //////////////////// function that will print the input from the previous function
// void print_grid(int size)       //// function has no outpuit and input is 'size'
// {
//     for (int i = 0; i < size; i++)
//     {
//         for (int j = 0; j < size; j++)
//         {
//             printf("#");
//         }
//         printf("\n");
//     }
// }
