class DisjointSet:

  parent = {}
  rank = {}

  def makeSet(self, universe):
    for i in universe:
      self.parent[i] = i
      self.rank[i] = 0
  
  def Find(self, k):
    #if 'k' is not root
    if self.parent[k] != k:
      #path compression
      self.parent[k] = self.Find(self.parent[k])
    return self.parent[k]
  
  def Union(self, a, b):
    x = self.Find(a)
    y = self.Find(b)

    if x == y:
      return
    
    #always attach a smaller depth tree under root of deeper tree
    if self.rank[x] > self.rank[y]:
      self.parent[y] = x
    elif self.rank[x] < self.rank[y]:
      self.parent[x] = y
    else:
      self.parent[x] = y
      self.rank[y] = self.rank[y] + 1

def printSets(universe, ds):
    print([ds.Find(i) for i in universe])
 
 
if __name__ == '__main__':
 
    # universe of items
    universe = [1, 2, 3, 4, 5]
 
    # initialize `DisjointSet` class
    ds = DisjointSet()
 
    # create a singleton set for each element of the universe
    ds.makeSet(universe)
    printSets(universe, ds)
 
    ds.Union(4, 3)        # 4 and 3 are in the same set
    printSets(universe, ds)
 
    ds.Union(2, 1)        # 1 and 2 are in the same set
    printSets(universe, ds)
 
    ds.Union(1, 3)        # 1, 2, 3, 4 are in the same set
    printSets(universe, ds)