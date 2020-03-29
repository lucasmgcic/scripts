SELECT p,max(ganho) FROM dadosBrutosOFDMA54 WHERE n='10' AND frame='256' AND t='5' GROUP BY t,n,frame;
