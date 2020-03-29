# -*- coding: utf-8 -*-

import math

valoresBanda=[6.0, 12.0, 54.0]
valoresPayload=[256.0,512.0,1024.0]
valoresPayload2=[256.0,256.0,512.0]
logValorBanda=[8,9,10]
logValorBanda2=[8,8,9]

for j in range (len(valoresPayload)):
	FRAME1 = valoresPayload[j]
	FRAME2 = valoresPayload2[j]
	for i in range (len(valoresBanda)):
	     
	    RATE = valoresBanda[i]
	   
	    #FRAME      = 8184.0
	    #####Nao estou contando os 28 bytes de header do IP + UDP junto aos 34 do MAC
	    T_FRAME    = 20 + 4 * math.ceil ((16 + 6 + 8 * (34 + FRAME1))/(RATE * 4.0))

	    ACK        = 5
	    RTS        = 5 + logValorBanda[i] + 5
	    CTS        = 5 + logValorBanda2[i] + 5
		
	    DELTA      = 0 		##ver se a propagacao sera considerada ou nao
	    SLOT_TIME  = 9.0		
	    SIFS       = 16
	    DIFS       = 34
		
	    W          = 16

	    Tbo = (W-1)*SLOT_TIME/2

	    Ts_Bidirecional = Tbo + RTS + SIFS + DELTA + CTS + SIFS + DELTA + T_FRAME + SIFS + DELTA + ACK + DIFS + DELTA

	    Ttot = Ts_Bidirecional

	    S = ((FRAME1 + FRAME2)*8) / Ttot


	    #Considerando k=1 para o TMT considerando nesse caso que nao ha perdas

	    print RATE, j+1, S, Ttot##, tau


