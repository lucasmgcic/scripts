.separator ' '
.mode list
.output /home/lucas/research/AINA20/imagens/tNumericoIdeal/54Mbps/t_10_256.dat
SELECT p,t, max(ganho) FROM versusFDMAC54 WHERE n='10' AND frame='256' GROUP BY p,n,frame;
.output /home/lucas/research/AINA20/imagens/tNumericoIdeal/54Mbps/t_50_256.dat
SELECT p,t, max(ganho) FROM versusFDMAC54 WHERE n='50' AND frame='256' GROUP BY p,n,frame;
.output /home/lucas/research/AINA20/imagens/tNumericoIdeal/54Mbps/t_100_256.dat
SELECT p,t, max(ganho) FROM versusFDMAC54 WHERE n='100' AND frame='256' GROUP BY p,n,frame;
.output /home/lucas/research/AINA20/imagens/tNumericoIdeal/54Mbps/t_10_512.dat
SELECT p,t, max(ganho) FROM versusFDMAC54 WHERE n='10' AND frame='512' GROUP BY p,n,frame;
.output /home/lucas/research/AINA20/imagens/tNumericoIdeal/54Mbps/t_50_512.dat
SELECT p,t, max(ganho) FROM versusFDMAC54 WHERE n='50' AND frame='512' GROUP BY p,n,frame;
.output /home/lucas/research/AINA20/imagens/tNumericoIdeal/54Mbps/t_100_512.dat
SELECT p,t, max(ganho) FROM versusFDMAC54 WHERE n='100' AND frame='512' GROUP BY p,n,frame;
.output /home/lucas/research/AINA20/imagens/tNumericoIdeal/54Mbps/t_10_1024.dat
SELECT p,t, max(ganho) FROM versusFDMAC54 WHERE n='10' AND frame='1024' GROUP BY p,n,frame;
.output /home/lucas/research/AINA20/imagens/tNumericoIdeal/54Mbps/t_50_1024.dat
SELECT p,t, max(ganho) FROM versusFDMAC54 WHERE n='50' AND frame='1024' GROUP BY p,n,frame;
.output /home/lucas/research/AINA20/imagens/tNumericoIdeal/54Mbps/t_100_1024.dat
SELECT p,t, max(ganho) FROM versusFDMAC54 WHERE n='100' AND frame='1024' GROUP BY p,n,frame;

