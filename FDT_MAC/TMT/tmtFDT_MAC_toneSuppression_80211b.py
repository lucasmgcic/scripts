# -*- coding: utf-8 -*-

valoresBanda=[1, 2, 11]
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
	    T_FRAME    = (FRAME1*8.0)/RATE
	    MAC_HEADER = 272 ###+ 28*8###(MACHEADER = 34by) nao vou considerar os headers das camadas de cima 20by ip e 8by udp
	    PHY_HEADER = 192 
	    HEADERS    = MAC_HEADER/RATE + PHY_HEADER

	    ACK        = 5
	    RTS        = 5 + logValorBanda[i] + 5
	    CTS        = 5 + logValorBanda2[i] + 5
		
	    DELTA      = 0 		##ver se a propagacao sera considerada ou nao
	    SLOT_TIME  = 20		
	    SIFS       = 10
	    DIFS       = 50
		
	    W          = 32

	    Tbo = (W-1)*SLOT_TIME/2

	    Ts_Bidirecional = Tbo + RTS + SIFS + DELTA + CTS + SIFS + DELTA + HEADERS + T_FRAME + SIFS + DELTA + ACK + DIFS + DELTA

	    Ttot = Ts_Bidirecional

	    S = ((FRAME1+FRAME2)*8) / Ttot

	    #Considerando k=1 para o TMT considerando nesse caso que nao ha perdas

	    print RATE, j+1 , S, Ttot##, tau


