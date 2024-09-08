// 4! = 4*3*2*1 = 4*3!  the 3! is a recursive call
// 3! = 3*2*1   = 3*2!
// 2! = 2*1     = 2*1!
// 1! = 1       = 1
// callstack


#include <stdio.h>
#include <cs50.h>

int factorial(int number);

int main(void)
{
    int n = get_int("Enter: ");

    printf("%i\n", factorial(n));
}


int factorial(int number)
{
    if (number == 1)     // base case which will stop infinite recursion
    {
        return 1;
    }

    return number * factorial(number-1);
}