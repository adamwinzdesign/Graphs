class Graph:
  def __init__(self):
    self.verticies = {}
  
  def add_vertex(self, vertex_id):
    self.verticies[vertex_id] = set()

  def add_edge(self, v1, v2):
    if v1 in self.verticies and v2 in self.verticies:
      self.verticies[v1].add(v2)
    else:
      raise IndexError('At least one of the given verticies does not exist in this graph!')

  def get_neighbors(self, vertex_id):
    return self.verticies[vertex_id]

mygraph = Graph()
mygraph.add_vertex('bro')
mygraph.add_vertex('brah')
mygraph.add_vertex('homie')
mygraph.add_edge('bro', 'brah')
mygraph.add_edge('brah', 'bro')
mygraph.add_edge('homie', 'bro')
mygraph.add_edge('homie', 'brah')

print(mygraph.get_neighbors('bro'))
print(mygraph.get_neighbors('brah'))
print(mygraph.get_neighbors('homie'))
