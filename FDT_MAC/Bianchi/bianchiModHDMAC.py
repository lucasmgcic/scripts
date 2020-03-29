# -*- coding: utf-8 -*-

import scipy
import scipy.optimize

valoresNo=[10,100,200,300,500,1000]

##for n in range (1,10):
for i in range (len(valoresNo)):

    n = valoresNo[i]
        
    FRAME      = 8184
    MAC_HEADER = 272
    PHY_HEADER = 128
    HEADERS    = MAC_HEADER + PHY_HEADER

    ACK        = 112 + PHY_HEADER
    RTS        = 160 + PHY_HEADER
    CTS        = 112 + PHY_HEADER
        
    DELTA      = 0
    SLOT_TIME  = 50
    SIFS       = 28.0
    DIFS       = 128
        
    W          = 32
    m          = 3

    Ts = RTS + SIFS + DELTA + CTS + SIFS + DELTA + HEADERS + FRAME + SIFS + DELTA + ACK + DIFS + DELTA
    Tc = RTS + DIFS + DELTA



    def get_tau():
        f = lambda x : 1.0 - (1-x)**(n-1)
        g = lambda x : 2.0*(1-2.0*x)/((1.0-2.0*x)*(W+1) + x*W*(1.0- (2.0*x)**m ) )
        return scipy.optimize.fsolve(lambda x: x - g(f(x)), 0)[0]


    tau = get_tau()

    ptr = 1.0 - (1.0-tau)**n
    ps = (n*tau*((1.0-tau)**(n-1)))/ptr

    mean_slot_time = SLOT_TIME*(1- ptr) + ptr*ps*Ts + ptr*(1-ps)*Tc

    S = (ps*ptr*FRAME) / mean_slot_time

    #Número de nós, vazão e tau
    print n, S##, tau


