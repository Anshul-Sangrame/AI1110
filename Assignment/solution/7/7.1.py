import numpy as np
import mpmath as mp
from matplotlib import pyplot as plt
import scipy

bv = np.loadtxt('ber.dat', dtype='double')
nv = np.loadtxt('gau.dat', dtype='double')

# gamma in dB
def error(gamma):
    av = np.loadtxt('./ral_data/'+str(int(2*gamma)), dtype='double')
    sig = av*bv + nv
    n0 = np.count_nonzero(bv > 0)
    #n1 = np.count_nonzero(bv < 0)
    e0 = np.count_nonzero((sig < 0) & (bv > 0)) 
    #e1 = np.count_nonzero((sig > 0) & (bv < 0))
    return e0/n0

err_vec = scipy.vectorize(error, otypes=['double'])

def expected_err(g):
    g_new = 10**(g/10.0)
    return 0.5*(1 - ((g_new/(g_new+2))**(0.5)))

exp_err_vec = scipy.vectorize(expected_err, otypes=['double'])

G = np.linspace(0, 10, 21)
A = np.linspace(0,10,1000)
plt.plot(G, err_vec(G), '.')
plt.plot(A, exp_err_vec(A))
plt.grid()
plt.xlabel('$\gamma$')
plt.ylabel('$P_e(\gamma)$')
plt.legend(["Simulation", "Analysis"])
plt.savefig('../figs/7_1.pdf')
plt.show()

plt.semilogy(G, err_vec(G), '.')
plt.semilogy(A, exp_err_vec(A))
plt.grid()
plt.xlabel('$\gamma$')
plt.ylabel('$P_e(\gamma)$')
plt.legend(["Simulation", "Analysis"])
plt.savefig('../figs/7_1_semilog.pdf')
plt.show()