import networkx as nx
import matplotlib.pyplot as plt
import math

g=nx.Graph()
g.add_nodes_from(['mapusa','porvorim','panajim','banastari','margao','vasco','verna','queula','gec'])
g.add_edge('mapusa','porvorim',weight=8)
g.add_edge('porvorim','panajim',weight=6)
g.add_edge('panajim','banastari',weight=6)
g.add_edge('banastari','gec',weight=11)
g.add_edge('panajim','margao',weight=24)
g.add_edge('margao','queula',weight=17)
g.add_edge('queula','gec',weight=6)
g.add_edge('vasco','verna',weight=18)
g.add_edge('verna','queula',weight=14)
g.add_edge('panajim','vasco',weight=24)
g_pos=nx.spring_layout(g)
heuristicDict={}
nx.draw(g,pos=g_pos,with_labels=True)
labels=nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,g_pos,edge_labels=labels)
plt.savefig('graph_original.png')
plt.clf

class Astar:

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

    def calculateAstar(self, goal, start, graph):
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
                lowest = 0
                lowestIndex = 0
                for i in graph[current]:
                    if lowest == 0:
                        lowest = heuristicDict.get(i) + graph[current][i]['weight']
                        lowestIndex = i
                    if (heuristicDict.get(i) + graph[current][i]['weight']) < lowest:
                        lowest = heuristicDict.get(i) + graph[current][i]['weight']
                        lowestIndex = i
                __closeList.append(current)
                current = lowestIndex
                node_col = ["white" if not node in __closeList else "green" for node in graph.nodes()]
                edge_col = ["green" if u in __closeList and v in __closeList else "black" for u, v in graph.edges()]
                nx.draw(graph, pos=g_pos, with_labels=True, node_color=node_col, edge_color=edge_col)
                nx.draw_networkx_edge_labels(g, g_pos, edge_labels=labels)
                plt.savefig('intermed' + str(counter) + '.png')
                plt.clf()
        if wasGoalFound:
            print('Goal was found')
            print('Traversal:')
            print(__closeList)
            node_col = ["white" if not node in __closeList else "green" for node in graph.nodes()]
            edge_col = ["green" if u in __closeList and v in __closeList else "black" for u, v in graph.edges()]
            nx.draw(graph, pos=g_pos, with_labels=True, node_color=node_col, edge_color=edge_col)
            nx.draw_networkx_edge_labels(g, g_pos, edge_labels=labels)
            plt.savefig('final.png')
        else:
            print('Goal was not found')

astar = Astar()
astar.calculateAstar('gec', 'mapusa', g)