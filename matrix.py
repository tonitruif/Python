
def get_char(index_i, index_j, string, matrix, n, m):
	if index_j+1 < m and index_i < n: 
		string += get_char(index_i, index_j + 1, string, matrix, n, m)
		string += get_char(index_i + 1, index_j, string, matrix, n, m)
	elif index_i+1 < n:
		string += get_char(index_i + 1, index_j, string, matrix, n, m)
	elif index_j+1 < m: 
		string += get_char(index_i, index_j + 1, string, matrix, n, m)
	else: 
		return string
	return matrix[index_i][index_j]



n, m = map(int, input().split())
matrix = [[0 for x in range(m)] for y in range(n)]
for i in range(n):
	input_string = str(input())
	if len(input_string) == m:
		for j in range(m):
			matrix[i][j] = input_string[j]
	else:
		print(' wrong length ')
		break
		

result = get_char(0,0,'',matrix, n ,m)
print(result)
print(matrix)




