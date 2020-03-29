# -*- coding: utf-8 -*-

import scipy
import scipy.optimize

valoresNo=[10,100,200,300,500,1000]
valoresK=[1,0.95,0.9,0.85,0.8,0.75]	###Parametro de atenuacao de self-interference

for j in range (len(valoresK)):
	K = valoresK[j]
	for i in range (len(valoresNo)):
    
	    n = valoresNo[i]
	   
	    FRAME      = 8184
	    MAC_HEADER = 272
	    PHY_HEADER = 128
	    HEADERS    = MAC_HEADER + PHY_HEADER

	    ACK        = 112 + PHY_HEADER
	    RTS        = 160 + PHY_HEADER
	    CTS        = 112 + PHY_HEADER
		
	    DELTA      = 0 		##ver se a propagacao sera considerada ou nao
	    SLOT_TIME  = 50		
	    SIFS       = 28.0
	    DIFS       = 128
		
	    W          = 32
	    m          = 3

	    Ts = RTS + SIFS + DELTA + CTS + SIFS + DELTA + CTS + SIFS + DELTA + HEADERS + FRAME + SIFS + DELTA + ACK + DIFS + DELTA
	    Tc = RTS + DIFS + DELTA

	    #Considerando k=1 da mesma forma que o Cheng para os calculos do FULL DUPLEX -- entender o k e ver como encaixá-lo no modelo...


	    def get_tau():
		f = lambda x : 1.0 - (1-x)**(n-1)
		g = lambda x : 2.0*(1-2.0*x)/((1.0-2.0*x)*(W+1) + x*W*(1.0- (2.0*x)**m ) )
		return scipy.optimize.fsolve(lambda x: x - g(f(x)), 0)[0]


	    tau = get_tau()

	    ptr = 1.0 - (1.0-tau)**n
	    ps = K*(n*tau*((1.0-tau)**(n-1)))/ptr

	    mean_slot_time = SLOT_TIME*(1- ptr) + ptr*ps*Ts + ptr*(1-ps)*Tc

	    beta = 0.5
	    FRAME_EXPECTED = (beta*K*FRAME + (1-beta)*K*K*FRAME)

	    S = (ps*ptr*FRAME_EXPECTED*2) / mean_slot_time ####Aqui multiplica-se o frame por 2 devido ao full duplex

	    #SelfInterference,Número de nós, vazão e tau - probab de um no querer transmitir
	    print K,n, S##, tau


