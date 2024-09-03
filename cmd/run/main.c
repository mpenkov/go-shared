#include <stdio.h>
#include <time.h>

#include "local.h"


int
main(void)
{
    time_t started = time(NULL);
    time_t finished;
    int i;

    for (i = 0; i < 1000000; ++i)
    {
        cNoop();
        if (i % 100000 == 0)
        {
            printf("%d\n", i);
        }
    }

    finished = time(NULL);
    fprintf(stderr, "made %d calls in %ds\n", i, (int)(finished - started));
}
