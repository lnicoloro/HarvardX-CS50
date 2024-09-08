# include <stdio.h>
#include <cs50.h>

// const int n = 3;

// float average(int array[]);

// int main (void)
// {
//     //array
//     int scores[n];

//     // scores[0] = get_int("Score: ");
//     // scores[1] = get_int("Score: ");
//     // scores[2] = get_int("Score: ");

//     // use loop instead
//     for (int i=0; i < 3; i++)
//     {
//         scores[i] = get_int("Score: ");
//     }

//     printf("Average: %f\n",average(scores));
// }


// float average(int array[])
// {
//     int sum = 0;
//     for (int i = 0; i < n; i++)
//     {
//         sum += array[i];
//     }
//     return sum / (float) n;
// }




// //////////////// STRINGS ARE BASICALLY ARRAYS
// int main(void)
// {
//     // string s = "HI!";
//     // printf("%c%c%c\n", s[0], s[1], s[2]);
//     // printf("%i %i %i\n", s[0], s[1], s[2]);

//     // string in array

//     string words[2];
//     words[0] = "HI";
//     words[1] = "BYE";
//     printf("%c%c%c\n", words[0][0], words[0][1], words[0][2]);
//     printf("%c%c%c\n", words[1][0], words[1][1], words[1][2]);
// }


#include <string.h>

////////// length of a sting

// int main(void)
// {
//     string name = get_string("Whats your name? ");

//     int n = 0;
//     while (name[n] != '\0')
//     {
//         n++;
//     }
//     printf("%i\n", n);

//     //// or

//     int m = strlen(name);
//     printf("%i\n", m);
// }



/////////// upper case and lower case

#include <ctype.h>

// int main(void)
// {
//     string s = get_string("Before: ");
//     printf("After: ");
//     for (int i= 0, n = strlen(s); i < n; i++)
//     {
//     //     if (s[i] >= 'a' && s[i] <= 'z')
//     //     {
//     //         // upper case to lower case is +/- 32
//     //         printf("%c", s[i] - 32);
//     //     }
//     //     else
//     //     {
//     //         printf("%c", s[i]);
//     //     }
//     // }

//     ///// or


//     printf("%c", toupper(s[i]));
//     }
//     printf("\n");
// }



///argv is arrray of strings all of the words typed
///argc is count of arguyments aka lenght

int main(int argc, string argv[])
{
    if (argc == 2) /// if something is typed after ./score
    {
     printf("hello, %s\n", argv[1]); /// name can be typed in after ./score (./score is [1])
    }
    else
    {
        printf("hello world\n");
    }

}