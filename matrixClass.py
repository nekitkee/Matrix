import jsonpickle
import copy
class MyMatrix:

    a = []
    b = []
    x = []

    def solve(self):
        try:
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

            # reverse
            # find all x

            self.x[n - 1] = self.b[n - 1] / self.a[n - 1][n - 1]
            for i in reversed(range(n - 1)):
                for k in range(i, n):
                    self.b[i] = self.b[i] - self.x[k] * self.a[i][k]
                self.x[i] = self.b[i] / self.a[i][i]

        except ZeroDivisionError:
            print("Zero division error")





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

    
    def load(filename):
        file = open(filename)
        jsnstr = file.read()
        mx = jsonpickle.decode(jsnstr)

        #fill x-array with 0
        for K in range(len(mx.b)):
         mx.x.insert(0,0)

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
        self.b[len(self.b) - 1] += self.b[len(self.b) - 1] * 0.01


    @classmethod
    def diff(self ,vector , vector_m):

        difvect = []
        for i in range(len(vector)):
            difvect.append(vector[i] - vector_m[i])
        return difvect



    def cond (self):

        #if det = 0 / cond = inf

        matrix = self.copy()
        matrix_mod = self.copy()
        matrix_mod.modify()
        dB = MyMatrix.diff(matrix.b , matrix_mod.b)
        matrix.solve()
        matrix_mod.solve()

        dX = MyMatrix.diff(matrix.x , matrix_mod.x)
        NX = MyMatrix.norm(matrix.x)
        NB = MyMatrix.norm(matrix.b)
        NdX = MyMatrix.norm(dX)
        NdB = MyMatrix.norm(dB)
        cond = NdX/NX * NB/NdB

        return cond





