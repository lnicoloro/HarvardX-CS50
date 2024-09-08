#include <stdio.h>
#include <stdlib.h>

// int main(void)
// {
//     int *list = malloc(3 * sizeof(int));
//     if (list == NULL)
//     {
//         return 1;
//     }

//     list[0] = 1;
//     list[1] = 2;
//     list[2] = 3;

// // tmp is hardcoded for 4 index
//     int *tmp = malloc(4 * sizeof(int));
//     if (tmp == NULL)
//     {
//         free(list);
//         return 1;
//     }

// // Copy from list into tmp
//     for (int i = 0; i < 3; i++)
//     {
//         tmp[i] = list[i];
//     }
// // add 4 to the last index in the tmp array
//     tmp[3] = 4;

//     free(list);

// //tmp with 1,2,3,4 becomes list
//     list = tmp;

//     for (int i = 0; i < 4; i++)
//     {
//         printf("%i\n", list[i]);
//     }

//     free(list);
//     return 0;
// }

///////////////////can instead us realloc
// int main(void)
// {
//     int *list = malloc(3 * sizeof(int));
//     if (list == NULL)
//     {
//         return 1;
//     }

//     list[0] = 1;
//     list[1] = 2;
//     list[2] = 3;

// // realloc will make and copy into a new array
//     int *tmp = realloc(list, 4 * sizeof(int));
//     if (tmp == NULL)
//     {
//         free(list);
//         return 1;
//     }

//     list = tmp;

// // add 4 to the last index in the tmp array
//     tmp[3] = 4;

//     for (int i = 0; i < 4; i++)
//     {
//         printf("%i\n", list[i]);
//     }

//     free(list);
//     return 0;
// }


///////making a linked list (stack)
typedef struct node
{
    int number;
    struct node *next;
}
node;


int main(int argc, char *argv[])
{
    node *list = NULL;

    for (int i = 1; i < argc; i++)
    {
        int number = atoi(argv[i]); //converts string to number and sets number equal to comand line argument i

        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }

        n->number = number;     // store number
        n->next = NULL;         // prepend to list (stack on the top)

        n->next = list;         // points to current begining of the list ( top of the stack)
        list = n;
    }

    node *ptr = list;            //ptr will temporarily point at the first node in a list
    while (ptr != NULL)
    {
        printf("%i\n", ptr->number);
        ptr = ptr->next;          //ptr will now point at the point on the current node to get the next node allowing iteration through the list
                                // once ptr = NULL the loop will end
    }

    ptr = list;
    while (ptr != NULL)
    {
        node *next = ptr->next;   // temp variable to store ptr
        free(ptr);
        ptr = next;                 // update ptr with the temp variable
    }

}
//////////searching this stack is O(n)
/////////adding to this stack is O(1) constant ti