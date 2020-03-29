# -*- coding: utf-8 -*-

import scipy
import scipy.optimize

import math

valoresNo=[10,50,100,150,200,250]
valoresK=[1,0.95,0.9,0.85,0.8,0.75]	###Parametro de atenuacao de self-interference

####FRAME1     = 256 # Do tipo 1 Bidirecional de 2 nos -- VER COM O BORDIM esse tamanho
####FRAME2     = 512 # Do tipo 2 Unidirecional de 3 nos -- VER COM O BORDIM esse tamanho



valoresFrame1=[256, 512, 1024, 2048, 4096]
valoresFrame2=[512, 1024, 2048, 4096, 8184]
valoresLog1=[8, 9, 10, 11, 12]
valoresLog2=[9, 10, 11, 12, 13]

for a in range (len(valoresFrame1)):
	for b in range (len(valoresFrame2)):
		if(b<a):
			continue		
		print 'nós', 'Vazão Normal', 'Vazão Escalonada', 'Ganho'

		nomeArquivo = "/home/lucas/research/tese/figuras/cap5/bianchiUniformMode/resultado802_11a_F1_" + str(valoresFrame1[a]) + "_F2_" + str(valoresFrame2[b]) + ".txt"
		file = open(nomeArquivo,"w") 

		for i in range (len(valoresNo)):
		
		    FRAME1=valoresFrame1[a]
		    FRAME2=valoresFrame2[b]
		    if(i==0):
			    print 'Frame 1', 'Frame 2'
			    print FRAME1, FRAME2

		    n = valoresNo[i]

		    K = 1
		
		    RATE = 6
		    T_FRAME1    = 20 + 4 * math.ceil ((16 + 6 + 8 * (34 + FRAME1))/(RATE * 4.0))
		    T_FRAME2    = 20 + 4 * math.ceil ((16 + 6 + 8 * (34 + FRAME2))/(RATE * 4.0))
		    T_FRAME 	= max(T_FRAME1, T_FRAME2)
		    T_FRAME_Min	= min(T_FRAME1, T_FRAME2)

		    ACK        = 5 
		    RTS        = valoresLog2[b] + 5 + 5
		    CTS        = valoresLog2[b] + 5 + 5
		
		    DELTA      = 0 		##ver se a propagacao sera considerada ou nao
		    SLOT_TIME  = 9.0		
		    SIFS       = 16
		    DIFS       = 34
		
		    W          = 16
		    m          = 3


		    Ts_Bidirecional = RTS + SIFS + DELTA + CTS + SIFS + DELTA + 0.5*(CTS + SIFS + DELTA) + T_FRAME + SIFS + DELTA + ACK + DIFS + DELTA
		    Ts_Unidirecional = RTS + SIFS + DELTA + CTS + SIFS + DELTA + 0.5*(CTS + SIFS + DELTA) + CTS + SIFS + DELTA + T_FRAME + SIFS + DELTA + ACK + DIFS + DELTA

		    Tc = RTS + DIFS + DELTA

		    RTS        = valoresLog1[a] + 5 + 5
		    CTS        = valoresLog1[a] + 5 + 5


		    Ts_Bidirecional_Min = RTS + SIFS + DELTA + CTS + SIFS + DELTA + 0.5*(CTS + SIFS + DELTA) + T_FRAME_Min + SIFS + DELTA + ACK + DIFS + DELTA
		    Ts_Unidirecional_Min = RTS + SIFS + DELTA + CTS + SIFS + DELTA + 0.5*(CTS + SIFS + DELTA) + CTS + SIFS + DELTA + T_FRAME_Min + SIFS + DELTA + ACK + DIFS + DELTA
		    Tc_Min = RTS + DIFS + DELTA

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
		    TsMin = (Ts_Bidirecional_Min*beta + Ts_Unidirecional_Min*(1-beta))

		    mean_slot_time = SLOT_TIME*(1- ptr) + ptr*ps*Ts + ptr*(1-ps)*Tc
		    mean_slot_time_Min = SLOT_TIME*(1- ptr) + ptr*ps*TsMin + ptr*(1-ps)*Tc_Min


		    ####Aqui multiplica-se o frame por 2 devido ao full duplex - ha  2 FRAME_EXPECTED sendo transmitidos
		    ####OBS: ISSO se for considerado os frames como sendo mesmo tamanho, pois senao a vazao tem que ser a media aritmetica dos 2 tamanhos de pacote.
		    FRAME_EXPECTED = (beta*K*8*(FRAME1+FRAME2)) + (1-beta)*K*K*8*(FRAME1+FRAME2)
		    FRAME_EXPECTED_MIN = beta*K*8*2*min(FRAME1,FRAME2) + (1-beta)*K*K*8*2*min(FRAME1,FRAME2)


		    S = (ps*ptr*(FRAME_EXPECTED)) / mean_slot_time
		    S_MIN = (ps*ptr*(FRAME_EXPECTED_MIN)) / mean_slot_time_Min

		    #Número de nós, vazão e relacao
		    Ganho = S_MIN / S
		    print n, S, S_MIN, Ganho ##, tau
		    file.write(str(n) + " " + str(Ganho) + "\n") 
		file.close()


