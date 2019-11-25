import jsonpickle
import copy


class MyMatrix:

    a = []
    b = []
    x = []

    def __init__(self,n = 0):
        self.x=[0]*n

    def gaussianElim(self):

        a = self.a
        b = self.b
        x = self.x

        n = len(self.a)

        for k in range(n):
            max = k
            # locate bigest in column
            for j in range(k + 1, n):
                if abs(self.a[max][k]) < abs(self.a[j][k]):
                    max = j

            # pickup row
            self.a.insert(k, self.a.pop(max))
            self.b.insert(k, self.b.pop(max))

            # coef substraction in j-column
            temp1 = self.a[k][k]
            self.a[k][k] = 1
            for j in range(k + 1, n):
                self.a[k][j] = self.a[k][j] / temp1
            self.b[k] = self.b[k] / temp1

            for I in range(k + 1, n):
                temp2 = self.a[I][k]
                self.a[I][k] = 0
                if (temp2 != 0):
                    for j in range(k + 1, n):
                        self.a[I][j] = self.a[I][j] - temp2 * self.a[k][j]
                    self.b[I] = self.b[I] - temp2 * self.b[k]

        # RETURN STEP
        # find all x

        self.x[n - 1] = self.b[n - 1] / self.a[n - 1][n - 1]
        for i in reversed(range(n - 1)):
            for k in range(i, n):
                self.b[i] = self.b[i] - self.x[k] * self.a[i][k]
            self.x[i] = self.b[i] / self.a[i][i]


    def tridiagonalSysSolve(self):
        alpha =[]
        beta =[]
        n = len(self.b)
        a=self.a
        b=self.b
        x=self.x

        alpha.append(a[0][1]/a[0][0])
        beta.append(b[0]/a[0][0])

        for i in range(1,n-1):

            alpha.append( a[i][i+1]/(a[i][i]-a[i][i-1]*alpha[i-1]) )
            beta.append( (b[i]-a[i][i-1]*beta[i-1])/(a[i][i]-a[i][i-1]*alpha[i-1]) )

        k=n-1
        x[k]= ( b[k] - a[k][k-1] *beta[k-1])/(a[k][k] - a[k][k-1] * alpha[k-1])

        for i in reversed(range(n-1)):
            x[i] = beta[i] - alpha[i]*x[i+1]


    @classmethod
    def detReqursive(self, matrix, total=0):

        indices = list(range(len(matrix)))

        if len(matrix) == 2 and len(matrix[0]) == 2:
            val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return val


        for fc in indices:
            subMatrix = copy.deepcopy(matrix)
            subMatrix = subMatrix[1:]
            height = len(subMatrix)

            for i in range(height):
                subMatrix[i] = subMatrix[i][0:fc] + subMatrix[i][fc + 1:]
            sign = (-1) ** (fc % 2)
            sub_det = MyMatrix.detReqursive(subMatrix)
            total += sign * matrix[0][fc] * sub_det

        return total

    def det(self):
        a = copy.deepcopy(self.a)
        return MyMatrix.detReqursive(a)

    def print(self):
        print("MATRIX A")
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                print("%.3f" % (self.a[i][j]), end="   ")
            print()
        print("MATRIX B")
        print(self.b)
        print()

    def copy(self):
        newMx = MyMatrix()
        newMx.a = copy.deepcopy(self.a)
        newMx.b = copy.deepcopy(self.b)
        newMx.x = copy.deepcopy(self.x)
        return newMx

    def printResult(self):
        print("RESULT: ")
        for i in range(len(self.x)):
            print("x[{}] = {}".format(i+1 , self.x[i]))
        print()

    @classmethod
    def load(self, filename):
        file = open(filename)
        jsnstr = file.read()
        mx = jsonpickle.decode(jsnstr)
        mx.x=[0]*len(mx.b)

        file.close()
        return mx

    def save ( self, filename):
        file = open(filename, 'w')
        jsnstr = jsonpickle.encode(self)
        file.write(jsnstr)
        file.close()


    @classmethod
    def norm(self,vector):
        sum = 0
        for i in range(len(vector)):
            sum = sum+ abs(vector[i])
        return sum


    def modify(self):
        #var1: right last el
        # self.b[len(self.b) - 1] += self.b[len(self.b) - 1] * 0.01

        #var2: biggest right el
        max= 0
        for j in range(len(self.b)):
            if abs(self.b[max]) < abs(self.b[j]):
                max = j
        self.b[max] += self.b[max]*0.01


    @classmethod
    def diff(self ,vector , vector_m):

        difvect = []
        for i in range(len(vector)):
            difvect.append(vector[i] - vector_m[i])
        return difvect



    def cond (self):

        #if det = 0 / cond = inf
        if(self.det() == 0):
            return  float('Inf')

        matrix = self.copy()
        matrix_mod = self.copy()
        matrix_mod.modify()
        dB = MyMatrix.diff(matrix.b , matrix_mod.b)

        NB = MyMatrix.norm(matrix.b)
        matrix.gaussianElim()
        matrix.print()
        matrix_mod.gaussianElim()

        dX = MyMatrix.diff(matrix.x , matrix_mod.x)
        NX = MyMatrix.norm(matrix.x)

        NdX = MyMatrix.norm(dX)
        NdB = MyMatrix.norm(dB)
        cond = NdX/NX * NB/NdB

        print("db ", dB)
        print("dX ", dX)
        print("NX  ", NX)
        print('b',matrix.b)
        print("NB ", NB)
        print("NdX ", NdX)
        print("NdB ", NdB)
        print("cond " , cond)

        return cond





