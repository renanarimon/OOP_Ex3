# OOP EX3 -  Directed Weighted Graph Python 

this asssinment has written by [Taliya Shitreet](https://github.com/taliyashitreet "Profile") and  [Renana Rimon](https://github.com/renanarimon "Profile") <br />
main classes:

## DiGraph implement GraphInterface:
#### The class represents a basic graph structure, and allows:

- add node
- remove node
- remove edge
- add edge
- get all v (returns the whole nodes at the graph)
- e size (amount of edges)
- v size (amount of nodes)
### The Digraph hold  3 dictionaries: 
- nodes 
- childern : all edges going out
- perants : all edges inter in

## DiGraphAlgo implements GraphAlgoInterface:
- isConnected(): check if graph is strongly connected.
- shortestPath(): find shortest path between 2 nodes. (using Dijkstra algorithm) [Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- center(): find center node in graph
  [Graph_center](https://en.wikipedia.org/wiki/Graph_center)
- tsp():Computes a list of consecutive nodes which go over all the nodes in cities. 
  [Travelling_salesman_problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
  - save(): save the Graph as Json file
  - load(): allowing to load a Json file
  
  ## After runing chack1() we get the folow plot:<br />
 ![image](https://user-images.githubusercontent.com/77111035/147135522-b2850adc-269f-48d9-9a96-cdb085f1b3e5.png)

  ## After runing chack2() we get the folow plot:<br />
  ![image](https://user-images.githubusercontent.com/77111035/147135054-3aea24a6-5dd5-4a65-8ef7-3ec05250c188.png)

  ## After runing chack3() we get the folow plot:<br />
  ![image](https://user-images.githubusercontent.com/77111035/147135096-3500a474-bc67-4203-ace8-c6ed5a5113c9.png)

  
  

