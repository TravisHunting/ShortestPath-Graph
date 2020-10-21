#!/usr/bin/env python3

class Graph:
  def __init__(self,directed=False):
    #dict with {node.value : node}
    self.nodes = {}
    self.directed = directed

  def add_node(self,node):
    self.nodes[node.value] = node 

  def add_edge(self,from_node,to_node,weight):
    #node dict with {connectednode : weight}
    from_node.add_edge(to_node,weight)
    if not self.directed:
      to_node.add_edge(from_node,weight)


class Vertex:
  def __init__(self, value):
    self.value = value
    #dict with {connectednode : weight}
    self.edges = {}
  
  def add_edge(self,to_node,weight):
    self.edges[to_node] = weight #adding node object : weight


layout = Graph()
a = Vertex("vertex a")
b = Vertex("vertex b")
c = Vertex("vertex c")
d = Vertex("vertex d")
e = Vertex("vertex e")
f = Vertex("vertex f")


layout.add_node(a)
layout.add_node(b)
layout.add_node(c)
layout.add_node(d)
layout.add_node(e)
layout.add_node(f)

layout.add_edge(a,b,3)
layout.add_edge(a,c,2)
layout.add_edge(b,c,2)
layout.add_edge(c,d,2)
layout.add_edge(b,d,3)
layout.add_edge(d,e,1)
layout.add_edge(a,f,3)

#dijkstra implementation below inspired by https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
#main difference is that I wanted to use vertex/node objects instead of tracking superficial 'nodes' in the graph

def dijkstra(graph,from_node,to_node):
	#shortest_paths is a dict {from_node_object: (to_node_object, total path length to reach to_node)}
    shortest_paths = {from_node: (None, 0)}
    current_node = from_node
    visited = set()

    while current_node != to_node:
    	visited.add(current_node)
    	#access current_node edges dict and retrive the keys, which are all the connected node objects
    	destinations = [i for i in current_node.edges.keys()]
    	weight_to_current_node = shortest_paths[current_node][1] #path length to reach current_node so far

    	for next_node in destinations:
    		#add the path length to get to current_node + edge weight to get to next_node
    		weight = current_node.edges[next_node] + weight_to_current_node
    		if next_node not in shortest_paths:
    			#if we haven't scoped out the next_node we need to add it to our shortest_paths dict
    			shortest_paths[next_node] = (current_node,weight)
    		else:
    			current_shortest_weight = shortest_paths[next_node][1]
    			if current_shortest_weight > weight:
    				shortest_paths[next_node] = (current_node,weight)

    	#all the destinations we need to check next, minus nodes we've already visited
    	next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}

    	#implementing pretty printing since our node objects will print like <graphvertex.Vertex object at 0x7f1747318fd0> otherwise
    	shortest_paths_pretty = {}
    	for i in shortest_paths:
    		if shortest_paths[i][0] is None:
    			shortest_paths_pretty[i.value] = (None, shortest_paths[i][1])
    		else:
    			shortest_paths_pretty[i.value] = (shortest_paths[i][0].value, shortest_paths[i][1])

    	#if there are no destinations to check and we stil haven't reached our goal node....
    	if not next_destinations:
    		return f"No path between {from_node.value} and {to_node.value}"
        
        #select the shortest path in the list and explore it
    	current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    #uncomment below to view your dict of shortest paths
    #print(shortest_paths_pretty)

    path = []
    while current_node is not None:
    	#if we have reached the goal node, current_node == goal_node
    	path.append(current_node.value)
    	next_node = shortest_paths[current_node][0]
    	#now we set current_node to the PREVIOUS node visited before goal_node
    	current_node = next_node
    	#repeat until we reach the original from_node, at which point there are no previous nodes

    path = path[::-1]
    #print(shortest_paths[to_node][1])  #this is the path weight
    #print(path) #this is the order of nodes to reach to_node via from_node
    return f"Your shortest path is distance {shortest_paths[to_node][1]}\n\
Your path is: {path}"



print(dijkstra(layout,a,f))
print()
print(dijkstra(layout,f,e))
print()
print(dijkstra(layout,a,e))
