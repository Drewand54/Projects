#include <cs50.h>
#include <stdio.h>

int length(long number);

int main(void)
{
    int temp1;
    int temp2;
    long multiplier = 1;
    int sum = 0;
    long number;
    do
    {
        number = get_long("Number: ");
    }
    while (length(number) != 13 && length(number) != 16 && length(number) != 15);

    for (int i = 0; i < length(number); i++)
    {

        temp1 = ((number / multiplier) % 10);
        multiplier *= 10;
        number = number - temp1;
        temp2 = ((number / multiplier) % 10) * 2;
        number = number - temp2;
        sum += (temp1 + (temp2 % 10) + (temp2 / 10 % 10));
        multiplier *= 10;
    }

    if (sum % 10 == 0)
    {
        // printf("%d\n",length(number));
        if (length(number) == 15 && ((((number / 100000000000000 % 10) * 10) + ((number / 10000000000000) % 10) == 34)))
        {
            printf("AMEX\n");
        }
        else if (length(number) == 15 && ((((number / 100000000000000 % 10) * 10) + ((number / 10000000000000) % 10) == 37)))
        {
            printf("AMEX\n");
        }
        else if (length(number) == 16 && (((number / 1000000000000000 % 10) * 10) + ((number / 100000000000000) % 10) == 51))
        {
            printf("MASTERCARD\n");
        }
        else if (length(number) == 16 && (((number / 1000000000000000 % 10) * 10) + ((number / 100000000000000) % 10) == 52))
        {
            printf("MASTERCARD\n");
        }
        else if (length(number) == 16 && (((number / 1000000000000000 % 10) * 10) + ((number / 100000000000000) % 10) == 53))
        {
            printf("MASTERCARD\n");
        }
        else if (length(number) == 16 && (((number / 1000000000000000 % 10) * 10) + ((number / 100000000000000) % 10) == 54))
        {
            printf("MASTERCARD\n");
        }
        else if (length(number) == 16 && (((number / 1000000000000000 % 10) * 10) + ((number / 100000000000000) % 10) == 55))
        {
            printf("MASTERCARD\n");
        }
        else if (((length(number) == 13 || length(number) == 16) &&
                  (((number / 1000000000000) % 10) == 4 || ((number / 1000000000000000) % 10) == 4)))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int length(long number)
{
    if (number < 10000000000000)
    {
        return 13;
    }
    if (number < 1000000000000000)
    {
        return 15;
    }
    if (number < 10000000000000000)
    {
        return 16;
    }
    else
    {
        return 1;
    }
}