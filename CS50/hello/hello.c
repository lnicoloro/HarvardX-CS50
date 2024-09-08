#include <stdio.h>
#include <cs50.h>

int main(void)
{
    printf("hello, world\n");
    string first = get_string("What's your first name? ");
    // string last = get_string("what's your last name? ");
    printf("hello, %s\n", first);
}
