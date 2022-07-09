#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "../coeffs.h"

int  main(void) //main function begins
{
int sz = 1000000;
double **b = loadtxt("ber.dat", sz, 1);
double **g = loadtxt("gau.dat", sz, 1);
FILE *fp = fopen("ber_gau.dat", "w");
for (int i = 0; i < sz; i++) { 
fprintf(fp, "%lf\n", pow(10,0.5)*b[i][0] + g[i][0]);
}
fclose(fp);
return 0;
}