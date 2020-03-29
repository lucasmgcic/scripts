# -*- coding: utf-8 -*-

import scipy
import scipy.optimize
import numpy
import sys

import math

#valoresP=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
valoresP=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
#valoresP=[0.1]
#valoresNo=[10,25,50,75,100]
valoresNo=[10,50,100]
valoresFrame1=[256, 512, 1024]
valoresLogFrame1=[8,9,10]
#valoresFrame1=[1024]
#valoresFrame1=[256, 512, 1024, 1492]
##valoresFrame1=[1024]
valoresQtdAlvos = [2, 3, 4, 5, 6, 7, 8, 9, 10]

tamanhoJanela = 3
syncTime = 5

for c in range (len(valoresP)):
	for b in range (len(valoresQtdAlvos)):
		tamanhoJanela = valoresQtdAlvos[b]
		for a in range (len(valoresFrame1)):

			for i in range (len(valoresNo)):
			    
			    FRAME1=valoresFrame1[a]

			    #if(i==0):
				    #print '\nFrame', FRAME1
		     		    #print 'nós', 'Denominador_Normal(Db)', 'Denominador_Normal_RTR(Da)'
		     		    #print 'p', 'Vazao_RI', 'Vazao_FD-MAC, Ganho'

			    n = valoresNo[i]
			    p=valoresP[c]

			    K = 1
	
			    RATE = 54
			    T_FRAME1    = 20 + 4 * math.ceil ((16 + 6 + 8 * (34 + FRAME1))/(RATE * 4.0))
			    T_FRAME 	= T_FRAME1
			    T_FRAME_Min	= T_FRAME1

			    RTR        = 20 + 4 * math.ceil ((16 + 6 + 8 * (20 + 6*(tamanhoJanela-1)))/(RATE * 4.0))
			    ACK        = syncTime
			    RTS        = syncTime 
			    CTS        = valoresLogFrame1[a] + syncTime + syncTime
			    MINI       = ((1-p) ** (tamanhoJanela-1)) * tamanhoJanela * syncTime
			    idSomatorio = 1
			    while idSomatorio < tamanhoJanela:
			    	parcial = ( (1-p) ** (idSomatorio-1) ) * ( p * idSomatorio * syncTime )
				MINI = MINI + parcial
				idSomatorio += 1

			
	
			    ACK_ORIG   = 20 + 4 * math.ceil ((16 + 6 + 8 * 14)/(RATE * 4.0))
			    RTS_ORIG   = 20 + 4 * math.ceil ((16 + 6 + 8 * 20)/(RATE * 4.0))
			    CTS_ORIG   = 20 + 4 * math.ceil ((16 + 6 + 8 * 14)/(RATE * 4.0))

			    DELTA      = 0 		##ver se a propagacao sera considerada ou nao
			    SLOT_TIME  = 9.0		
			    SIFS       = 16
			    DIFS       = 34
	
			    W          = 16
			    R          = 7


			    Ts_Normal = RTS_ORIG + SIFS + DELTA + CTS_ORIG + SIFS + DELTA + CTS_ORIG + SIFS + DELTA + T_FRAME + SIFS + DELTA + ACK_ORIG + DIFS + DELTA
			    Tc = RTS_ORIG + SIFS + ACK + DIFS + DELTA

			    Ts_Normal = (Ts_Normal * (W/(W-1))) + SLOT_TIME
			    Tc = Tc + SLOT_TIME


			    Ts_RI = RTR + SIFS + DELTA + CTS + SIFS + DELTA + T_FRAME_Min + SIFS + DELTA + ACK + DIFS + DELTA
			    Tc_RI = RTR + SIFS + ACK + DIFS + DELTA

			    Ts_RI = (Ts_RI * (W/(W-1))) + SLOT_TIME
			    Tc_RI = Tc_RI + SLOT_TIME

			    #Considerando k=1 da mesma forma que o Cheng para os calculos do FULL DUPLEX -- entender o k e ver como encaixá-lo no modelo...

			    def get_tau():
				    f = lambda x : 1.0 - (1-x)**(n-1)
				    g = lambda x : 1/(1 + ((1-x)/(2*(1-x**(R+1)))) * ((x**0 * (2**0 * W - 1) - (1-(x**(R+1)))) + (x**1 * (2**1 * W - 1) - (1-(x**(R+1)))) + (x**2 * (2**2 * W - 1) - (1-(x**(R+1)))) + (x**3 * (2**3 * W - 1) - (1-(x**(R+1)))) + (x**4 * (2**4 * W - 1) - (1-(x**(R+1)))) + (x**5 * (2**5 * W - 1) - (1-(x**(R+1)))) + (x**6 * (2**6 * W - 1) - (1-(x**(R+1)))) + (x**7 * (2**7 * W - 1) - (1-(x**(R+1))))) )
				    return scipy.optimize.fsolve(lambda x: x - g(f(x)), 0)[0]


			    tau = get_tau()

			    pb = 1.0 - (1.0-tau)**n
			    ps = n*tau*((1.0-tau)**(n-1))

			    mean_slot_time = SLOT_TIME*(1- pb) + ps*Ts_Normal + (pb-ps)*Tc
			    mean_slot_time_RI = SLOT_TIME*(1- pb) + ps*Ts_RI + (pb-ps)*Tc_RI

			    print n, mean_slot_time, mean_slot_time_RI

			    ####Aqui multiplica-se o frame por 2 devido ao full duplex - ha  2 FRAME_EXPECTED sendo transmitidos
			    ####OBS: ISSO se for considerado os frames como sendo mesmo tamanho, pois senao a vazao tem que ser a media aritmetica dos 2 tamanhos de pacote.
			    FRAME_EXPECTED = (1+p)*FRAME1*8
			    FRAME_EXPECTED = (FRAME_EXPECTED * (W/(W-1)))

			    DESCONTO = math.ceil(5/8.0 * RATE)
			    FRAME_EXPECTED_RI = (1-((1-p)**tamanhoJanela))*(FRAME1-DESCONTO)*8 + FRAME1*8
			    FRAME_EXPECTED_RI = (FRAME_EXPECTED_RI * (W/(W-1)))
    
			    S = (ps*(FRAME_EXPECTED)) / mean_slot_time
			    S_RI = (ps*(FRAME_EXPECTED_RI)) / mean_slot_time_RI

			    #Vazao nova/Vazao Antiga
			    Ganho = S_RI / S
			    print p,S_RI, S, Ganho ##, tau

			    nombreArquivo = 'db_%dMbps.csv' % (RATE)
			    arq  = open(nombreArquivo, "a")
			    line2write = str(n) + "," + str(FRAME1) + "," + str(p) + "," + str(tamanhoJanela) + "," + str(Ganho) + "\n" 
			    arq.write(line2write)
			    arq.close


#### Db = mean_slot_time
#### Pszb = FRAME_EXPECTED
#### Da = mean_slot_time_RI
#### Psza = FRAME_EXPECTED_RI

