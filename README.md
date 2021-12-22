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
  ![image](https://user-images.githubusercontent.com/77111035/147135743-61e123e5-af20-4bb2-ae1a-398d659a681a.png)
  ## After runing chack2() we get the folow plot:<br />
 ![image](https://user-images.githubusercontent.com/77111035/147135784-e396edf5-756a-42f5-bbc3-3a4f8fc09c82.png)

  ## After runing chack3() we get the folow plot:<br />
  ![image](https://user-images.githubusercontent.com/77111035/147135807-fc354638-b43b-4371-afe7-c08a3afa133b.png)

  
  

