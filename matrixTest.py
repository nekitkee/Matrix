from matrixClass import MyMatrix
filename = 'data.json'
filenameRes = 'result.json'


matrix = MyMatrix.load(filename)
#matrix.print()

#cond
print("cond: " , matrix.cond())

#Метод исключения Гаусса с ведущим элементом
#matrix.solve()


#matrix.print()


#savematrix
matrix.save(filenameRes)


























