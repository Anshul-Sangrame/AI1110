#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "../coeffs.h"

int  main(void) //main function begins
{
 
// Chi square with degree of freedom = 2 distribution
chi_sq("chi.dat",2,1000000);

return 0;
}