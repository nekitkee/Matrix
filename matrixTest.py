from matrixClass import MyMatrix

#Метод исключения Гаусса с ведущим элементом и метод прогонки

squareMatrixFile = 'squareMatrix.json'
squareMatrixOut = 'squareMatrixOut.json'
tridiagMatrixOut = 'tridiagMatrixOut.json'
tridiagMatrixFile = 'tridiagMatrix.json'


print("Tridiagonal matrix")
matrixTr = MyMatrix.load(tridiagMatrixFile)
matrixTr.print()

matrixTr.tridiagonalSysSolve()
matrixTr.printResult()


print("Gaussian Elimination")
matrixSq = MyMatrix.load(squareMatrixFile)
matrixSq.print()


#cond
print("cond: ", matrixSq.cond())

matrixSq.gaussianElim()
matrixSq.printResult()


#savematrix
matrixSq.save(squareMatrixOut)
matrixTr.save(tridiagMatrixOut)


























