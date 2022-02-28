

#         0 1 2 3 4 5 6 7
arena = [[2,0,2,0,2,0,2,0],
		 [0,2,0,2,0,2,0,2],
		 [2,0,2,0,2,0,2,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [1,0,1,0,1,0,1,0],
		 [0,1,0,1,0,1,0,1],
		 [1,0,1,0,1,0,1,0],
]


# 1 jogador branco
# 2 jogador preto
# 0 nulo

# x é a linha
# y posição


print("   0  1  2  3  4  5  6  7")
for n in range(0,len(arena)):
	print(n,arena[n])


def mudar(arena,jogador, X_inicial, Y_inicial, X_final, Y_final):
	if jogador == 2:
		jogador = [2,1,1]
	elif jogador == 1:
		jogador = [1,-1,2]
	else:
		return 0

	if arena[X_inicial][Y_inicial] == jogador[0]:
		if Y_inicial+jogador[1] == Y_final :
			if arena[X_final][Y_final] != jogador[0] and arena[X_final][Y_final] != 0:
				if arena[X_final][Y_final] == jogador[2]:
					if arena[X_final+1][Y_final+jogador[1]] == 0:
						arena[X_final+1][Y_final+jogador[1]] = jogador[0]
						arena[X_final][Y_final] = 0
					elif arena[X_final-1][Y_final+jogador[1]] == 0:
						arena[X_final-1][Y_final+jogador[1]] = jogador[0]
						arena[X_final][Y_final] = 0

					else:
						return 0



