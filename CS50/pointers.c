#include <stdio.h>

/////////////////////pointer arithmatic
// int main(void)
// {
//     char *s = "Hi";
//     printf("%c\n", *s);
//     printf("%c\n", *s+1);
// }


// int main(void)
// {
//     char *s = "Hi!";
//     printf("%s\n", s);
//     printf("%s\n", s+1);
//     printf("%s\n", s+2);
// }

/////////////////// copy a string   can instead just use
// strcpy(s, t);

#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

// int main(void)
// {
//     char *s = get_string("s: ");
//     if (s == NULL)
//     {
//         return 1;   //something went wrong
//     }
//     // char *t = s;   // will assign s and t the same memory address
//     char *t = malloc(strlen(s) + 1); // t is now a pointer to some free memory sapce the +1 is for null at the end of a sting
//     if (t == NULL)
//     {
//         return 1;       //something went wrong
//     }

//     for (int i = 0, n = strlen(s) + 1; i < n; i++)
//     {
//         t[i] = s[i];
//     }

//     if (strlen(t) > 0)
//     {
//         t[0] = toupper(t[0]);
//     }

//     printf("%s\n", s);
//     printf("%s\n", t);

//     free(t); // whenever allocating memory with malloc you must free it at the end of the program
//     //free lets the computer know you are done with that chunck of memory and it can be used for something else now

//     return 0;       //everything worked
// }


///////////////// swap values locations

// void swap(int *a, int *b);

// int main(void)
// {
//     int x = 1;
//     int y = 2;

//     printf("x = %i, y = %i\n", x, y);
//     swap(&x, &y);
//     printf("x = %i, y = %i\n", x, y);
// }

// void swap(int *a, int *b)
// {
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }





///////////re-creating get_int

// int main(void)
// {
//     int x;
//     printf("x: ");
//     scanf("%i", &x);
//     printf("x: %i\n", x);
// }

////////////// re-creating get_string

int main(void)
{
    char s[5];      //will only work for 5 char get_string uses malloc for every new character typed
    printf("s: ");
    scanf("%s", s);      // dont need & because for string s is already an address
    printf("s: %s\n", s);
}