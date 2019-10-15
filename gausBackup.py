#
# try:
#     n = len(matrix.a)
#     for k in range(n) :
#         max = k
#         #locate bigest in column
#         for j in range(k+1, n):
#             if abs(matrix.a[max][k])<abs(matrix.a[j][k]):
#                 max=j
#
#         #pickup row
#         matrix.a.insert(k, matrix.a.pop(max))
#         matrix.b.insert(k, matrix.b.pop(max))
#
#
#         #coef substraction in j-column
#         temp1 = matrix.a[k][k]
#         matrix.a[k][k] = 1
#         for j in range (k+1 , n):
#
#             matrix.a[k][j]= matrix.a[k][j] / temp1
#         matrix.b[k] = matrix.b[k] / temp1
#
#         for I in range(k+1, n):
#             temp2=matrix.a[I][k]
#             matrix.a[I][k]=0
#             if(temp2!=0):
#                 for j in range(k+1 , n):
#                     matrix.a[I][j] = matrix.a[I][j] - temp2 * matrix.a[k][j]
#                 matrix.b[I]= matrix.b[I] - temp2 * matrix.b[k]
#
#     # reverse
#     #find all x
#
#     matrix.x[n-1] = matrix.b[n-1]/matrix.a[n-1][n-1]
#     for i in reversed(range(n-1)):
#         for k in range(i , n):
#             matrix.b[i] = matrix.b[i] - matrix.x[k]*matrix.a[i][k]
#         matrix.x[i]= matrix.b[i]/matrix.a[i][i]
#
#     matrix.printResult()
#
# except ZeroDivisionError:
#     print("Zero division error")