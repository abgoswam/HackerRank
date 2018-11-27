
class Node:
    def __init__(self, name, content):
        self.name = name
        self.dep_nodes = []
        self.visited = False
        self.content = content


graph_nodes = {}


class ModuleBuilder:

    def add_module(self, name, deps, content):
        if name in graph_nodes:
            node_name = graph_nodes[name]
            node_name.content = content
        else:
            node_name = Node(name, content)
            graph_nodes[name] = node_name

        for dep in deps:
            if dep in graph_nodes:
                node_dep = graph_nodes[dep]
            else:
                node_dep = Node(dep, None)
                graph_nodes[dep] = node_dep

            node_name.dep_nodes.append(node_dep)

    def depth_first(self, node):
        node.visited = True

        for neigh in node.dep_nodes:
            if not neigh.visited:
                self.depth_first(neigh)

        print(node.content)

    def query_module(self, sourceModule):
        # pass
        node = graph_nodes[sourceModule]
        self.depth_first(node)


mb = ModuleBuilder()

mb.add_module("a", ["b", "c"], "b() c()")
mb.add_module("b", ["c", "d", "e"], "c() d() e()")
mb.add_module("c", ["d", "e"], "d() e()")
mb.add_module("d", [], "NA (d)")
mb.add_module("e", [], "NA (e)")
mb.add_module("f", ["g"], "g()")
mb.add_module("g", [], "NA")

print("View a:")
mb.query_module("a")

print("View f:")
mb.query_module("f")
