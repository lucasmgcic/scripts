# -*- coding: utf-8 -*-

valoresBanda=[1, 2, 11]
valoresPayload=[256.0,512.0,1024.0,8184.0]	

for j in range (len(valoresPayload)):
	FRAME = valoresPayload[j]
	for i in range (len(valoresBanda)):
	     
	    RATE = valoresBanda[i]
	   
	    #FRAME      = 8184.0
	    T_FRAME    = (FRAME*8.0)/RATE
	    MAC_HEADER = 272 ###+ 28*8###(MACHEADER = 34by) nao vou considerar os headers das camadas de cima 20by ip e 8by udp
	    PHY_HEADER = 192
	    HEADERS    = MAC_HEADER/RATE + PHY_HEADER

	    ACK        = 112/RATE + PHY_HEADER
	    RTS        = 160/RATE + PHY_HEADER
	    CTS        = 112/RATE + PHY_HEADER
		
	    DELTA      = 0 		##ver se a propagacao sera considerada ou nao
	    SLOT_TIME  = 20		
	    SIFS       = 10
	    DIFS       = 50
		
	    W          = 32

	    Tbo = (W-1)*SLOT_TIME/2

	    Ttot = Tbo + RTS + SIFS + DELTA + CTS + SIFS + DELTA + CTS + SIFS + DELTA + HEADERS + T_FRAME + SIFS + DELTA + ACK + DIFS + DELTA

	    S = 2*(FRAME*8) / Ttot

	    #Considerando k=1 para o TMT considerando nesse caso que nao ha perdas

	    print RATE, FRAME, S, Ttot##, tau


