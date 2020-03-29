# scripts
Scripts python desenvolvidos para cálculos de vazão em modelos matemáticos estendidos de Bianchi e Tinnirello para comunicações full-duplex.

FDT_MAC

	- Bianchi

		- Scripts utilizados para o cálcula da vazão de saturação segundo o modelo de Bianchi estendido para comunicações full-duplex, com variação de fator de auto-interferência (self-interference), para FDT_MAC, FD_MAC e HD_MAC (802.11), tanto para parâmetros do 802.11a quanto para os do 802.11b.

	- TMT
		- Scripts utilizados para cálculo da vazão máxima teórica (TMT) para FDT_MAC, FD_MAC e HD_MAC (802.11), tanto para parâmetros do 802.11a quanto para os do 802.11b. Há ainda o cálculo do TMT quando o FDT-MAC considera a supressão de tom (tone suppression).

	- UniformMode
		- Bianchi
			- Scripts usados para comparar o FDT_MAC com modo uniforme e sem modo uniforme. A saída do cálculo é o quociente entre as vazões de saturação, segundo o modelo de Bianchi estendido. Novamente, o cálculo é feito considerando parâmeros da camada física do 802.11a e do 802.11b.

		- TMT
			- Scripts utilizados para cálculo da vazão máxima teórica (TMT) para FDT_MAC e FD_MAC e HD_MAC (802.11), tanto para parâmetros do 802.11a quanto para os do 802.11b em um exemplo de dois fluxos (pacote de 512 seguido de pacote de 1024).

FDMR_MAC
	
	- psiIdeal

		- Scripts usados para o cálculo do psi ideal do FDMR-MAC em relação a obter maior ganho possível sobre o FD-MAC. O script python gera várias saídas que devem ser carregadas em um banco de dados e através dos scripts da pasta sql se obtém o gráfico de psi ideal. ALERTA: Na pasta sql, há alguns caminhos hard-coded, como explicado no readme da referida pasta

	- Tinnirello

		- Scripts utilizados para o comparar o FDMR-MAC com o FDT-MAC, em termos de vazão de saturação, segundo o modelo estendido de Tinnirello. A análise é feita para 6Mbps e 54Mpbs, usando em ambos os casos o IEEE 802.11a.
