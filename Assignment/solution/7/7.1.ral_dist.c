#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "../coeffs.h"

int  main(void) //main function begins
{
double gamma;
double j;
int i;
char file[10];

// ral distribution for 20 different values of gamma
for(i=0;i<21;i++) {
    j = (double)i/2.0;
    gamma = pow(10,j/10.0);
    sprintf(file,"./ral_data/%d",i);
    ral_gamma(file,gamma,1000000);
}

return 0;
}