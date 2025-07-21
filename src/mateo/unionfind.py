class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    def find(self, x):
        if(self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if(root_x == root_y):
            return False
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
        return True
u = UnionFind(10)

print(u.union(1, 2))  # True
print(u.union(2, 3))  # True
print(u.union(1, 3))  # False
print(u.find(1)) 
print(u.find(2))  
