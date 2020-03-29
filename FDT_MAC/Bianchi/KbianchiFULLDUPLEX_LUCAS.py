# -*- coding: utf-8 -*-

import scipy
import scipy.optimize

import math

valoresNo=[10,100,200,300,500,1000]
valoresK=[1,0.95,0.9,0.85,0.8,0.75]	###Parametro de atenuacao de self-interference

for j in range (len(valoresK)):
	K = valoresK[j]
	for i in range (len(valoresNo)):
	     
	    n = valoresNo[i]
		
	    FRAME1     = 8184 # Do tipo 1 Bidirecional de 2 nos -- VER COM O BORDIM esse tamanho
	    FRAME2     = 8184 # Do tipo 2 Unidirecional de 3 nos -- VER COM O BORDIM esse tamanho
	    MAC_HEADER = 272
	    PHY_HEADER = 128
	    HEADERS    = MAC_HEADER + PHY_HEADER

	    ACK        = 5 ########VER COM O BORDIM vou considerar 8184 como o maior... 
	    RTS        = 13 + 5 + 5########VER COM O BORDIM vou considerar 8184 como o maior... 
	    CTS        = 13 + 5 + 5########VER COM O BORDIM vou considerar 8184 como o maior... 
		
	    DELTA      = 0 		##ver se a propagacao sera considerada ou nao
	    SLOT_TIME  = 50		
	    SIFS       = 28.0
	    DIFS       = 128
		
	    W          = 32
	    m          = 3

	    Ts_Bidirecional = RTS + SIFS + DELTA + CTS + SIFS + DELTA + CTS + SIFS + DELTA + HEADERS + FRAME1 + SIFS + DELTA + ACK + DIFS + DELTA
	    Ts_Unidirecional = RTS + SIFS + DELTA + CTS + SIFS + DELTA + CTS + SIFS + DELTA + CTS + SIFS + DELTA + HEADERS + FRAME2 + SIFS + DELTA + ACK + DIFS + DELTA
	    Tc = RTS + DIFS + DELTA

	    #Considerando k=1 da mesma forma que o Cheng para os calculos do FULL DUPLEX -- entender o k e ver como encaixá-lo no modelo...


	    def get_tau():
		f = lambda x : 1.0 - (1-x)**(n-1)
		g = lambda x : 2.0*(1-2.0*x)/((1.0-2.0*x)*(W+1) + x*W*(1.0- (2.0*x)**m ) )
		return scipy.optimize.fsolve(lambda x: x - g(f(x)), 0)[0]


	    tau = get_tau()

	    ptr = 1.0 - (1.0-tau)**n
	    ps = (n*tau*((1.0-tau)**(n-1)))/ptr

	    beta = 0.5; #### Beta eh o percentual de transmissoes do tipo 1 -- bidirecionais envolvendo 2 nos
	    Ts = (Ts_Bidirecional*beta + Ts_Unidirecional*(1-beta))

	    mean_slot_time = SLOT_TIME*(1- ptr) + ptr*ps*Ts + ptr*(1-ps)*Tc


	    ####Aqui multiplica-se o frame por 2 devido ao full duplex - ha  2 FRAME_EXPECTED sendo transmitidos
	    ####OBS: ISSO se for considerado os frames como sendo mesmo tamanho, pois senao a vazao tem que ser a media aritmetica dos 2 tamanhos de pacote.
	    FRAME_EXPECTED = 2*(beta*K*FRAME1 + (1-beta)*K*K*FRAME2)

	    S = (ps*ptr*(FRAME_EXPECTED)) / mean_slot_time 

	    #SelfInterference, Número de nós, vazão e tau - probab de um no querer transmitir
	    print K,n, S##, tau


