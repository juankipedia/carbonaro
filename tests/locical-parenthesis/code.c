#include <stdio.h>
int main(void)
{
    float a;
    float b;
    float c;
    float d;
    a = 0;
    b = 1;
    c = (((a && b) || a) && b);
    d = (a && b) || (c && d);
    return 0;
}
