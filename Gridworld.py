import random


class GreedWorld:

    def __init__(self):
        self.grid = []
        self.number_visits = []
        self.gamma = 0.9

        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0

        for i in range(5):
            row = []
            for j in range(5):
                row.append(0)
            self.grid.append(row)

        for i in range(5):
            row = []
            for j in range(5):
                row.append(0)
            self.number_visits.append(row)

        for k in range(5):
            for j in range(5):
                print(self.grid[k][j], end=" ")
            print("")

    def reword(self, x, y):
        a = []
        xs = []
        ys = []

        if x == 0 and y == 1:

            reword = 10
            a.append(reword + self.gamma * self.grid[4][1])
            a.append(reword + self.gamma * self.grid[4][1])
            a.append(reword + self.gamma * self.grid[4][1])
            a.append(reword + self.gamma * self.grid[4][1])

            xs.append(4)
            xs.append(4)
            xs.append(4)
            xs.append(4)

            ys.append(1)
            ys.append(1)
            ys.append(1)
            ys.append(1)

        elif x == 0 and y == 3:

            reword = 5
            a.append(reword + self.gamma * self.grid[2][3])
            a.append(reword + self.gamma * self.grid[2][3])
            a.append(reword + self.gamma * self.grid[2][3])
            a.append(reword + self.gamma * self.grid[2][3])

            xs.append(2)
            xs.append(2)
            xs.append(2)
            xs.append(2)

            ys.append(3)
            ys.append(3)
            ys.append(3)
            ys.append(3)

        else:

            # North.

            if x > 0:
                reword = 0
                a.append(reword + self.gamma * self.grid[x - 1][y])
                xs.append(x - 1)
                ys.append(y)

            else:
                reword = -1
                a.append(reword + self.gamma * self.grid[x][y])
                xs.append(x)
                ys.append(y)

            # East.

            if y < 4:
                reword = 0
                a.append(reword + self.gamma * self.grid[x][y + 1])
                xs.append(x)
                ys.append(y + 1)

            else:
                reword = -1
                a.append(reword + self.gamma * self.grid[x][y])
                xs.append(x)
                ys.append(y)

            # West.

            if y > 0:
                reword = 0
                a.append(reword + self.gamma * self.grid[x][y - 1])
                xs.append(x)
                ys.append(y - 1)
            else:
                reword = -1
                a.append(reword + self.gamma * self.grid[x][y])
                xs.append(x)
                ys.append(y)

            # South.

            if x < 4:
                reword = 0
                a.append(reword + self.gamma * self.grid[x + 1][y])
                xs.append(x + 1)
                ys.append(y)
            else:
                reword = -1
                a.append(reword + self.gamma * self.grid[x][y])
                xs.append(x)
                ys.append(y)

        return a, xs, ys

    def move(self, x, y):
        #print("x " + str(x) + " y " + str(y))
        self.number_visits[x][y] += 1

        a, xs, ys = self.reword(x, y)

        rand = random.uniform(0, 1)

        if rand < 1:
            new_move = random.randint(0, 3)
            next_x = xs[new_move]
            next_y = ys[new_move]

        else:
            max_index = a.index(max(a))
            new_move = max_index
            next_x = xs[max_index]
            next_y = ys[max_index]

        # North.
        if new_move == 0:
            self.one += 1
            self.grid[x][y] += a[0]


        # East.
        elif new_move == 1:
            self.two += 1
            self.grid[x][y] += a[1]


        # West.
        elif new_move == 2:
            self.three += 1
            self.grid[x][y] += a[2]


        # South.
        elif new_move == 3:
            self.four += 1
            self.grid[x][y] += a[3]


        if self.number_visits[x][y] > 1:
            self.grid[x][y] /= 2

        #print("next x " + str(x) + " next y "+str(y))

        return next_x, next_y

    def simualtor(self):
        x = 0
        y = 0

        for i in range(20000000):
            x, y = self.move(random.randint(0, 4), random.randint(0, 4))

        print("one " + str(self.one) + " two " + str(self.two) + " three " + str(self.three) + " four " + str(self.four))

        for k in range(5):
            for j in range(5):
                print(self.grid[k][j], end=" ")
            print(" ")

        print(" ")
        for k in range(5):
            for j in range(5):
                print(self.number_visits[k][j], end=" ")
            print(" ")






