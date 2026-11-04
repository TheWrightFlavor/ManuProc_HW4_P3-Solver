from math import pi, sqrt, log
from matplotlib import pyplot as plt

D_o = 50 #[mm]
h_o = 35 #[mm]
h_f = 15 #[mm]
K = 300 #[MPa]
n = 0.12
mu = 0.1

def solve(h):
    ep = log(h_o / h)
    Y_f = K * ep**n
    D = D_o * sqrt(h_o / h)
    K_f = 1 + (mu * D) / (1.5 * h)
    A = (pi * D**2) / 4
    F = K_f * Y_f * A
    f = F / 1000
    return [h, ep, Y_f, D, K_f, A, F, f]
    
entries = []
for h in range(h_f, h_o+1):
    entries.append(solve(h))
    
entries.reverse()
    
with open('output.csv','w') as file:

    text = 'h, Epsilon, Y_f[MPa], Diam[mm], K_f, A[mm^2], F[N], F[KN]\n'

    for i in entries:
        
        text += f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]}\n'
        
    file.write(text)
    
x = []
y = []
for i in entries[1:]:
    x.append(i[0]-h_o)
    y.append(i[7])

plt.xlabel('Height (h-h_o) [mm]')
plt.ylabel('Force [KN]')
plt.plot(x, y)
plt.show()