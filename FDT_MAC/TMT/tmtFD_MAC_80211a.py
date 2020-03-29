# -*- coding: utf-8 -*-

import math

valoresBanda=[6.0, 12.0, 54.0]
valoresPayload=[256.0,512.0,1024.0,8184.0]
logValorBanda=[8,9,10,13]		

for j in range (len(valoresPayload)):
	FRAME = valoresPayload[j]
	for i in range (len(valoresBanda)):
	     
	    RATE = valoresBanda[i]
	   
	    #FRAME      = 8184.0
	    #####Nao estou contando os 28 bytes de header do IP + UDP junto aos 34 do MAC
	    T_FRAME    = 20 + 4 * math.ceil ((16 + 6 + 8 * (34 + FRAME))/(RATE * 4.0))

	    ACK        = 20 + 4 * math.ceil ((16 + 6 + 8 * 14)/(RATE * 4.0))
	    RTS        = 20 + 4 * math.ceil ((16 + 6 + 8 * 20)/(RATE * 4.0))
	    CTS        = 20 + 4 * math.ceil ((16 + 6 + 8 * 14)/(RATE * 4.0))
		
	    DELTA      = 0 		##ver se a propagacao sera considerada ou nao
	    SLOT_TIME  = 9.0		
	    SIFS       = 16
	    DIFS       = 34
		
	    W          = 16

	    Tbo = (W-1)*SLOT_TIME/2

	    Ttot = Tbo + RTS + SIFS + DELTA + CTS + SIFS + DELTA + CTS + SIFS + DELTA + T_FRAME + SIFS + DELTA + ACK + DIFS + DELTA

	    S = 2*(FRAME*8) / Ttot

	    #Considerando k=1 para o TMT considerando nesse caso que nao ha perdas

	    print RATE, FRAME, S, Ttot##, tau


