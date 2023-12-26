# Graph is represented in two formats Adjacency List and adjacency matrix

class Graph:
    def __init__(self) -> None:
        self.adj_list={}

    def display_graph(self):
        for v in self.adj_list:
            print(v,":",self.adj_list[v])

    def add_vertex(self,v):
        if v not in self.adj_list.keys():
            self.adj_list[v]=[]
            return True
        return False
    
    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys and v2 in self.adj_list.keys:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def delete_edge(self,v1,v2):
        if v1 in self.adj_list.keys and v2 in self.adj_list.keys:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self,v):
        if v in self.adj_list.keys():
            for other_vertex in self.adj_list[v]:
                self.adj_list[other_vertex].remove(v)
            del self.adj_list[v]
            return True
        return False
    