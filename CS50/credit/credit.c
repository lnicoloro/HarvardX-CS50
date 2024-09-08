#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long credit;

    int credit_1, credit_2, credit_3, credit_4, credit_5, credit_6, credit_7,
    credit_8, credit_9, credit_10, credit_11, credit_12, credit_13, credit_14, credit_15,
    credit_16, credit_2_sum, credit_4_sum, credit_6_sum, credit_8_sum, credit_10_sum, credit_12_sum,
    credit_14_sum, credit_16_sum, luhn_sum;

    do
    {
      credit = get_long("Number: ");
    }
    while (credit < 0);

    credit_1 = (credit % 10);
    credit_2 = (credit % 100)/10;
    credit_3 = (credit % 1000)/100;
    credit_4 = (credit % 10000)/1000;
    credit_5 = (credit % 100000)/10000;
    credit_6 = (credit % 1000000)/10000;
    credit_7 = (credit % 10000000)/1000000;
    credit_8 = (credit % 100000000)/10000000;
    credit_9 = (credit % 1000000000)/100000000;
    credit_10 = (credit % 10000000000)/1000000000;
    credit_11 = (credit % 100000000000)/10000000000;
    credit_12 = (credit % 1000000000000)/100000000000;
    credit_13 = (credit % 10000000000000)/1000000000000;
    credit_14 = (credit % 100000000000000)/10000000000000;
    credit_15 = (credit % 1000000000000000)/100000000000000;
    credit_16 = (credit % 10000000000000000)/1000000000000000;

    credit_2_sum = ((credit_2 * 2) % 10) + (((credit_2 * 2) % 100) /10);
    credit_4_sum = ((credit_4 * 2) % 10) + (((credit_4 * 2) % 100) /10);
    credit_6_sum = ((credit_6 * 2) % 10) + (((credit_6 * 2) % 100) /10);
    credit_8_sum = ((credit_8 * 2) % 10) + (((credit_8 * 2) % 100) /10);
    credit_10_sum = ((credit_10 * 2) % 10) + (((credit_10 * 2) % 100) /10);
    credit_12_sum = ((credit_12 * 2) % 10) + (((credit_12 * 2) % 100) /10);
    credit_14_sum = ((credit_14 * 2) % 10) + (((credit_14 * 2) % 100) /10);
    credit_16_sum = ((credit_16 * 2) % 10) + (((credit_16 * 2) % 100) /10);

    luhn_sum = credit_2_sum + credit_4_sum + credit_6_sum + credit_8_sum + credit_10_sum + credit_12_sum + credit_14_sum + credit_16_sum
    + credit_1 + credit_3 + credit_5 + credit_7 + credit_9 + credit_11 + credit_13 + credit_15 ;

    printf("%i ", luhn_sum);

    if (luhn_sum % 10 != 0)
    {
        printf("INVALID\n");
    }

    else if (credit_16 == 5)
    {
        if (credit_15 == 1 || credit_15 == 2 || credit_15 == 3 || credit_15 == 4 || credit_15 == 5)
        {
            printf("MASTERCARD\n");
        }
    }

    else if (credit_15 == 3)
    {
        if (credit_14 == 4 || credit_14 == 7)
        {
            printf("AMERICAN EXPRESS\n");
        }

    else if (credit_13 == 4)
    {
        printf("VISA\n");
    }

    else if(credit_16 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID2\n");
    }
    }
}

// Convert input long into a list of integers
int* ConvertCreditNumberToDigitList(long num)
{

    int digits[15];
    int i = 0;
    while (num != 0)
    {
        // do something
    }

    return digits;
}