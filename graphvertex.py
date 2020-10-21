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