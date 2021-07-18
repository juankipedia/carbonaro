#include <stdio.h>
int main(void)
{
    float minsofar;
    float maxsofar;
    float sum;
    float num;
    float i;
    float c;
    minsofar = 0;
    maxsofar = 0;
    sum = 0;
    num = 0;
    printf("Enter number of inputs: \n");
    if (0 == scanf("%f", &num))
    {
        num = 0;
        scanf("%*s");
    }
    i = 0;
    c = 0;
    while (i < num)
    {
        if (0 == scanf("%f", &c))
        {
            c = 0;
            scanf("%*s");
        }
        if (i == 0)
        {
            minsofar = c;
            maxsofar = c;
        }
        if (i != 0)
        {
            if (c < minsofar)
            {
                minsofar = c;
            }
            if (c > maxsofar)
            {
                maxsofar = c;
            }
        }
        sum = sum + c;
        i = i + 1;
    }
    printf("Min: \n");
    printf("%.2f\n", (float)(minsofar));
    printf("Max: \n");
    printf("%.2f\n", (float)(maxsofar));
    printf("Sum: \n");
    printf("%.2f\n", (float)(sum));
    printf("Avg: \n");
    printf("%.2f\n", (float)(sum / num));
    return 0;
}
