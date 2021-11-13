m = 5
n = 5
B = matrix(ZZ, m, n)
for i in range(m):
	for j in range(n):
		B[i, j] = ZZ.random_element(1, 10)
n_rows = B.nrows()
n_cols = B.ncols()
x = matrix(ZZ, 1, n_cols, 0)
coef = matrix(ZZ, 1, n_rows, 0 )
[Gram, U]= B.gram_schmidt()
Gram 
U
G = []
for i in range(n_rows):
	G.append(norm(Gram[i]))
BBT = B*B.transpose()
volume = RR(sqrt(abs(BBT.determinant())))

bound = sqrt(n_rows) * volume.nth_root(n_rows)
shortest_vector = copy(B[0])
shortest_coef = matrix(ZZ, 1, n_rows, 0 )
def SVP(n):
	global bound, B, G, shortest_vector, coef, n_rows,U, shortest_coef
	if n == -1:
		temp_vec = matrix(ZZ, 1, n_cols, 0)
	#	print("temp_vec is")
	#	print(temp_vec)
		temp_vec = temp_vec +  coef * B 
	
	#	print("coef is")
	#	print(coef)
		if norm(temp_vec) > 0 and norm(temp_vec) < norm(shortest_vector):
			#bound = norm(temp_vec)
			shortest_vector = temp_vec
			shortest_coef = copy(coef)
		return
	temp_bound = bound 
	temp_coef = 0
	#print("coef is")
#	print(coef)
	#print("n is ", n)
	for i in range(n_rows - 1, n , - 1):
	#	print("i is ", i)
		temp_coef = temp_coef + U[i,n] * coef[0,i]
	#print("temp_coef is ", temp_coef )
	temp_val = (bound / G[n])
	for i in range(floor(-temp_val - temp_coef) , floor(temp_val - temp_coef) +1, 1):
		coef[0, n] = i 
		SVP(n - 1) 
SVP(n_rows - 1)
print(shortest_vector)
print("norm of shortest_vector", RR(norm(shortest_vector)))
short_bkz = B.BKZ()
print("shortest_coef ", shortest_coef)
print(short_bkz[0])
print("BKZ norm",RR(norm(short_bkz[0])))
print(short_bkz * B.inverse())


