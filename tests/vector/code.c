#include <stdio.h>
int main(void)
{
    float m11;
    float m12;
    float m13;
    float m14;
    float m21;
    float m22;
    float m23;
    float m24;
    float m31;
    float m32;
    float m33;
    float m34;
    float m41;
    float m42;
    float m43;
    float m44;
    float v1;
    float v2;
    float v3;
    float v4;
    float result1;
    float result2;
    float result3;
    float result4;
    printf("Transform a vector by a matrix.\n");
    m11 = 0;
    m12 = 0;
    m13 = 0;
    m14 = 0;
    m21 = 0;
    m22 = 0;
    m23 = 0;
    m24 = 0;
    m31 = 0;
    m32 = 0;
    m33 = 0;
    m34 = 0;
    m41 = 0;
    m42 = 0;
    m43 = 0;
    m44 = 0;
    printf("Enter 16 matrix values: \n");
    if (0 == scanf("%f", &m11))
    {
        m11 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m12))
    {
        m12 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m13))
    {
        m13 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m14))
    {
        m14 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m21))
    {
        m21 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m22))
    {
        m22 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m23))
    {
        m23 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m24))
    {
        m24 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m31))
    {
        m31 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m32))
    {
        m32 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m33))
    {
        m33 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m34))
    {
        m34 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m41))
    {
        m41 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m42))
    {
        m42 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m43))
    {
        m43 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &m44))
    {
        m44 = 0;
        scanf("%*s");
    }
    v1 = 0;
    v2 = 0;
    v3 = 0;
    v4 = 0;
    printf("Enter 4 vector values: \n");
    if (0 == scanf("%f", &v1))
    {
        v1 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &v2))
    {
        v2 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &v3))
    {
        v3 = 0;
        scanf("%*s");
    }
    if (0 == scanf("%f", &v4))
    {
        v4 = 0;
        scanf("%*s");
    }
    result1 = m11 * v1 + m12 * v2 + m13 * v3 + m14 * v4;
    result2 = m21 * v1 + m22 * v2 + m23 * v3 + m24 * v4;
    result3 = m31 * v1 + m32 * v2 + m33 * v3 + m34 * v4;
    result4 = m41 * v1 + m42 * v2 + m43 * v3 + m44 * v4;
    printf("%.2f\n", (float)(result1));
    printf("%.2f\n", (float)(result2));
    printf("%.2f\n", (float)(result3));
    printf("%.2f\n", (float)(result4));
    return 0;
}
