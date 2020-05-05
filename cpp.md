interesting cout format:
http://faculty.cs.niu.edu/~mcmahon/CS241/c241man/node83.html


find sth wrong
https://blog.csdn.net/B_Nemo/article/details/80578006

typedef union
{
    long i;
    int k[5];
    char c;
} uni;
uni max;  
printf("%d",sizeof(max)); >> 24???? why