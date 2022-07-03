#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void)
{
printf("mean is %lf\n",mean("uni.dat"));
printf("variance is %lf\n",var("uni.dat"));
return 0;
}
