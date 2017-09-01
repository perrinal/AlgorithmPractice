import unittest
class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

    def __str__(self):
        output = self.label + "{" + str(self.color) + "}["
        for neighbor in self.neighbors:
            output += neighbor.label +"{" +str(neighbor.color) + "}"+  ","
        return output + "]"

class Graph:
    def __init__(self):
        self.graph = list();

    def addGraphNode(self, GNode):
        self.graph.append(GNode)

    def colorGraph(self):
        availableColors = set(range(0,self.getGraphDegree()));
        print (availableColors);
        for Node in self.graph:
            print (Node)
            illegal_color = set([n.color for n in Node.neighbors])
            print (illegal_color)
            legal_colors = list (availableColors - illegal_color)
            print (legal_colors)
            Node.color = legal_colors[0]
            
    def __str__(self):
        output = ""
        for Node in self.graph:
             output += str(Node) + "\n"
        return output

    def getGraphDegree(self):
        maxConnexion = 0
        for GNode in self.graph:
            if len(GNode.neighbors) > maxConnexion:
                maxConnexion = len(GNode.neighbors)
        return maxConnexion
        
        



#class TestGraphNode(unittest.TestCase):
    
    #def setUp(self):
graph = Graph();
a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')

a.neighbors.add(b)
a.neighbors.add(c)
a.neighbors.add(d)
a.neighbors.add(e)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(a)
c.neighbors.add(b)
d.neighbors.add(a)
e.neighbors.add(a)

 
graph.addGraphNode(a)
graph.addGraphNode(b)
graph.addGraphNode(c)
graph.addGraphNode(d)
graph.addGraphNode(e)
graph.colorGraph()
print(graph)
        


#if __name__ == '__main__':
 #   unittest.main()
