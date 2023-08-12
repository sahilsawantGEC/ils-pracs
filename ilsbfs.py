import networkx as nx
import matplotlib.pyplot as plt
import math

g = nx.Graph()
g.add_nodes_from(['davorlim',  'arlem','raia', 'curtorim', 'rachol', 'comorlim', 'borim', 'curli', 'quela', 'gec'])
g.add_edges_from([('davorlim','arlem'),('davorlim','curtorim'),
                  ('arlem','raia'), ('curtorim','rachol') ,
                  ('raia','comorlim'),   ('rachol','comorlim'),
                  ('comorlim','borim'), ('borim','quela'),
                  ('borim','curli'),
                  ('quela','gec'),('curli','gec')])
g_pos = nx.spring_layout(g)
nx.draw(g, pos = g_pos, with_labels=True)
heuristicDict = {}

plt.savefig('bfsgraph_original.png')
plt.clf()

class BreadthFirstSearch:
    def performBFS(self, graph, startNode, goalNode):
        if graph.has_node(startNode):
            __wasFound = False
            __close = list()
            __open = list()
            __open.append(startNode)
            __itNo = 0
            while (len(__close) != graph.number_of_nodes()):
                __itNo += 1
                if __open.__getitem__(0) == goalNode:
                    __wasFound = True
                    __close.append(__open.pop(0))
                    break
                if len(graph[__open.__getitem__(0)]) != 0:
                    for neighbourNode in graph.neighbors(__open.__getitem__(0)):
                        if neighbourNode not in __close:
                            __open.append(neighbourNode)
                __close.append(__open.pop(0))
                node_col = ["red" if not node in __close else "green" for node in graph.nodes()]
                edge_col = ["green" if u in __close and v in __close else "black" for u, v in graph.edges()]
                nx.draw(g, pos=g_pos, with_labels=True, node_color=node_col, edge_color=edge_col)
                plt.savefig('graph_bfs_it' + str(__itNo) + '.png')
                plt.clf()
            print(__close)
            if __wasFound:
                print("goal node was found")
                node_col = ["red" if not node in __close else "green" for node in graph.nodes()]
                edge_col = ["green" if u in __close and v in __close else "black" for u, v in graph.edges()]
                nx.draw(g, pos=g_pos, with_labels=True, node_color=node_col, edge_color=edge_col)
                plt.savefig('graph_bfs_it' + str(__itNo) + '.png')
            else:
                print("goal node was not found")

class DepthFirstSearch:

    def performDFS(self, graph, startNode, goalNode):
        if graph.has_node(startNode):
            __wasFound = False
            __close = list()
            __open = list()
            __open.append(startNode)
            __itNo = 0
            current = startNode
            while (len(__close) != graph.number_of_nodes()):
                current = __open[0]
                __itNo += 1
                if current == goalNode:
                    __wasFound = True
                    __close.append(current)
                    __open.remove(current)
                    break
                if len(graph[current]) != 0:
                    for neighbourNode in graph.neighbors(current):
                        if neighbourNode not in __close:
                            __open.insert(0, neighbourNode)
                __close.append(current)
                __open.remove(current)
                node_col = ["red" if not node in __close else "green" for node in graph.nodes()]
                edge_col = ["green" if u in __close and v in __close else "black" for u, v in graph.edges()]
                nx.draw(g, pos=g_pos, with_labels=True, node_color=node_col, edge_color=edge_col)
                plt.savefig('graph_dfs_it' + str(__itNo) + '.png')
                plt.clf()
            print(__close)
            if __wasFound:
                print("goal node was found")
                node_col = ["red" if not node in __close else "green" for node in graph.nodes()]
                edge_col = ["green" if u in __close and v in __close else "black" for u, v in graph.edges()]
                nx.draw(g, pos=g_pos, with_labels=True, node_color=node_col, edge_color=edge_col)
                plt.savefig('graph_dfs_it' + str(__itNo) + '.png')
            else:
                print("goal node was not found")


class BestFirstSearch:

    def calculateHeuristic(self, goal, start, graph):
        heuristicDict.clear
        heuristicDict[goal] = 0
        paths = list(nx.all_simple_paths(graph, goal, start))
        for onePath in paths:
            for oneNode in onePath:
                if not (heuristicDict.__contains__(oneNode)):
                    heuristicDict[oneNode] = math.sqrt(
                        ((g_pos[oneNode][0] - g_pos[goal][0]) ** 2) + ((g_pos[oneNode][1] - g_pos[goal][1]) ** 2)) * 100
        while len(heuristicDict) != graph.number_of_nodes():
            for n in graph:
                highest = 0
                if (heuristicDict.__contains__(n)):
                    highest = heuristicDict[n]
                for x in graph.neighbors(n):
                    if (heuristicDict.__contains__(x) and heuristicDict[x] > highest):
                        highest = heuristicDict[x]
                for x in graph.neighbors(n):
                    if not (heuristicDict.__contains__(x)):
                        heuristicDict[x] = highest + (math.sqrt(
                            ((g_pos[x][0] - g_pos[n][0]) ** 2) + ((g_pos[x][1] - g_pos[n][1]) ** 2)) * 100)
        print('Heuristic values')
        print(heuristicDict)

    def calculateBestFS(self, graph, start, goal):
        self.calculateHeuristic(goal, start, graph)
        __closeList = list()
        current = start
        wasGoalFound = False
        counter = 0
        while (len(__closeList) != graph.number_of_nodes()):
            counter = counter + 1
            if current == goal:
                __closeList.append(current)
                wasGoalFound = True
                break
            else:
                lowest = heuristicDict.get(current)
                lowestIndex = 0
                for i in graph[current]:
                    if heuristicDict.get(i) < lowest:
                        lowest = heuristicDict.get(i)
                        lowestIndex = i
                __closeList.append(current)
                current = lowestIndex
                node_col = ["red" if not node in __closeList else "green" for node in graph.nodes()]
                edge_col = ["green" if u in __closeList and v in __closeList else "black" for u, v in graph.edges()]
                nx.draw(graph, pos=g_pos, with_labels=True, node_color=node_col, edge_color=edge_col)
                plt.savefig('intermed' + str(counter) + '.png')
                plt.clf()
        if wasGoalFound:
            print('Goal was found')
            print('Traversal:')
            print(__closeList)
            node_col = ["red" if not node in __closeList else "green" for node in graph.nodes()]
            edge_col = ["green" if u in __closeList and v in __closeList else "black" for u, v in graph.edges()]
            nx.draw(graph, pos=g_pos, with_labels=True, node_color=node_col, edge_color=edge_col)
            plt.savefig('final.png')
        else:
            print('Goal was not found')


while True:
    print("1.Breadth first Search")
    print("2.Depth First Search")
    print("3.Best First Search")
    print("4.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
         BreadthFirstSearch().performBFS(g, 'davorlim', 'gec')
    elif choice == 2:
         DepthFirstSearch().performDFS(g, 'davorlim', 'gec')
    elif choice == 3:
        BestFirstSearch().calculateBestFS(g, 'davorlim', 'gec')
    elif choice == 4:
        break

    else:
        print("Wrong Choice")

