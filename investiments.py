def soma_lista(lista):
	soma = 0
	for i in lista:
		soma+=i
	return soma

print("\n\n SISTEMA DE RECOMENDAÇÃO DE INVESTIMENTOS")


#  Encontrando tma
entrada = int(input("selic ou cmpc?\n1 - selic\n2 - cmpc\n"))
if entrada == 1:
	selic = float(input("Informe a taxa de selic: "))
	tma = selic

elif entrada == 2:
	valores = []
	ks = []

	print("Informe as fontes de capital:")
	
	banco = input("banco?")
	if banco=='sim':
		qnt_banco=int(input("informe a quantidade de bancos: "))
		valores_banco=[]
		dados_banco = {}
		for i in range(qnt_banco):		
			print("Informe o valor do empréstimo para o banco", i+1)
			valor = float(input())
			dados_banco["valor"]=valor
			valores.append(valor)
			
			print("Informe a taxa de juros para o banco", i+1)
			taxa = float(input())
			dados_banco["taxa"]=taxa

			print("Informe o imposto de renda para o banco", i+1, ("porcentagem"))
			imposto_de_renda = float(input())
			dados_banco["imposto de renda"]=imposto_de_renda/100

			kb = taxa*(1 - imposto_de_renda)
			dados_banco["kb"]=kb
			ks.append(kb)


			valores_banco.append(dados_banco) 


	debentures = input("debentures?")
	if debentures=="sim":
		valor_debentures = float(input("Informe o valor: "))
		taxa_debentures = float(input("Informe o valor da taxa: "))
		valores.append(valor_debentures)
		ks.append(taxa_debentures)


	acoes_preferenciais = input("acoes preferenciais?")
	if acoes_preferenciais== 'sim':
		valor_acoes_preferenciais = float(input("Informe o valor das ações preferenciais: "))
		dividendo_acoes_preferenciais = float(input("Informe o dividendo: "))
		preco_acoes_preferenciais = float(input("Informe o preço: "))
		custo_corretagem_acoes_preferenciais = (float(input("Informe o custo de corretagem: ")))/100
		kp = dividendo_acoes_preferenciais/(preco_acoes_preferenciais*(1-custo_corretagem_acoes_preferenciais))
		valores.append(valor_acoes_preferenciais)
		ks.append(kp)

	acoes_ordinarias = input("acoes ordinárias?")
	if acoes_ordinarias== 'sim':
		valor_acoes_ordinarias = float(input("Informe o valor das ações ordinárias: "))
		dividendo_acoes_ordinarias = float(input("Informe o dividendo: "))
		preco_acoes_ordinarias = float(input("Informe o preço: "))
		custo_corretagem_acoes_ordinarias = (float(input("Informe o custo de corretagem: ")))/100
		valor_futuro_acoes_ordinarias = float(input("Informe o valor futuro: "))
		valor_presente_acoes_ordinarias = float(input("Informe o valor presente: "))
		tempo_acoes_ordinarias = float(input("Informe o tempo (em anos): "))
		g_ordinario = ((valor_futuro_acoes_ordinarias/valor_presente_acoes_ordinarias)**(1/tempo_acoes_ordinarias)) - 1
		ko = (dividendo_acoes_ordinarias/(preco_acoes_ordinarias*(1-custo_corretagem_acoes_ordinarias)))+g_ordinario
		valores.append(valor_acoes_ordinarias)
		ks.append(ko)

	lucros_acumulados = input("lucros acumulados?")
	if lucros_acumulados== 'sim':
		valor_lucros_acumulados = float(input("Informe o valor dos lucros acumulados: "))
		dividendo_lucros_acumulados = float(input("Informe o dividendo: "))
		preco_lucros_acumulados = float(input("Informe o preço: "))
		custo_corretagem_lucros_acumulados = (float(input("Informe o custo de corretagem: ")))/100
		valor_futuro_lucros_acumulados= float(input("Informe o valor futuro: "))
		valor_presente_lucros_acumulados = float(input("Informe o valor presente: "))
		tempo_lucros_acumulados = float(input("Informe o tempo (em anos): "))
		g_lucro = ((valor_futuro_lucros_acumulados/valor_presente_lucros_acumulados)**(1/tempo_lucros_acumulados)) - 1
		kl = (dividendo_lucros_acumulados/(preco_lucros_acumulados*(1-custo_corretagem_lucros_acumulados)))+g_lucro
		valores.append(valor_lucros_acumulados)
		ks.append(kl)


	soma_valores = soma_lista(valores)
	wacc = []
	for i in range(len(valores)):
		wacc.append((valores[i]/soma_valores)*ks[i])

	cmpc = soma_lista(wacc)
	tma = cmpc

print('tma: ', tma)



#  Encontrando VPL
print('\nVPL\n')
investimento_inicial = float(input("Informe o investimento inicial: "))
tempo = int(input("Informe o tempo de investimento (em anos): "))
lista_flc=[]
for i in range(tempo):
	print("Informe o fluxo de caixa para o ano", i+1)
	flc = float(input())
	lista_flc.append(flc)

somatorio = 0
for i in range(len(lista_flc)):
	somatorio+=lista_flc[i]/((tma+1)**(i+1))

vpl = (-1)*investimento_inicial + somatorio

print('vpl: ', vpl)


# Encontrando VPLA
print('\nVPLA\n')
vpla = vpl*(tma*((1+tma)**tempo)/((1+tma)**tempo)-1)
print('vpla: ', vpla)

# Encontrando IBC
print('\nIBC\n')
ibc = somatorio/investimento_inicial
print('ibc: ', ibc)
