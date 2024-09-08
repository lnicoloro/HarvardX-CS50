#include <stdio.h>
#include <cs50.h>
#include <string.h>


/////////////////// find int
// int main(void)
// {
//     int numbers[] = {20, 500, 10, 5, 100, 1, 50};

//     int n = get_int("Number: ");
//     for (int i = 0; i < 7; i++)
//     {
//         if (numbers[i] == n)
//         {
//             printf("found\n");
//             return 0;
//         }
//     }
//     printf("Not found\n");
//     return 1;
// }

///////////////////// find string
// int main(void)
// {
//     string strings[] = {"battleship", "boot", "cannon", "iron", "thimble", "tophat"};

//     string s = get_string("String: ");
//     for (int i = 0; i < 6; i++)
//     {
//         if (strcmp(strings[i], s) == 0)
//         {
//             printf("found\n");
//             return 0;
//         }
//     }
//     printf("Not found\n");
//     return 1;
// }


///////////////////////phonebook
// int main(void)
// {
//     string names[] = {"carter", "David"};
//     string numbers[] = {"+1-617-495-1000", "+1-949-468-2750"};

//     string name = get_string("Name: ");
//     for (int i = 0; i < 2; i++)
//     {
//         if (strcmp(names[i], name) == 0)
//         {
//             printf("%s\n", numbers[i]);
//             return 0;
//         }
//     }
//     printf("Not found\n");
//     return 1;
// }


///////////////make your own data type
typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    person people[2];

    people[0].name = "Carter";
    people[0].number = "+1-617-495-1000";

    people[1].name = "David";
    people[1].number = "+1-949-468-2750";

    string name = get_string("Name: ");
    for (int i = 0; i < 2; i++)
    {
        if (strcmp(people[i].name, name) == 0)
        {
            printf("%s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
