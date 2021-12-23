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

## GraphAlgo implements GraphAlgoInterface:
- isConnected(): check if graph is strongly connected.
- shortestPath(): find shortest path between 2 nodes. (using Dijkstra algorithm) [Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- center(): find center node in graph
  [Graph_center](https://en.wikipedia.org/wiki/Graph_center)
- tsp():Computes a list of consecutive nodes which go over all the nodes in cities. 
  [Travelling_salesman_problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
- save(): save the Graph as Json file
- load(): allowing to load a Json file
  
  ## After runing chack1() we get the folow plot:<br />
  ![image](https://user-images.githubusercontent.com/77111035/147135861-c6e53370-39be-4482-878e-c0245d2cbbc5.png)
  ## After runing chack2() we get the folow plot:<br />
 ![image](https://user-images.githubusercontent.com/77111035/147135784-e396edf5-756a-42f5-bbc3-3a4f8fc09c82.png)

  ## After runing chack3() we get the folow plot:<br />
  ![image](https://user-images.githubusercontent.com/77111035/147135807-fc354638-b43b-4371-afe7-c08a3afa133b.png)
  
  ## How to run the program : 
  in the main.py: go to main and create a AlgoGraph on this way:<br />
  g_algo = GraphAlgo() <br />
  file = '../data/A5.json' (enter a jason file you wuold like to load) <br />
  g_algo.load_from_json(file) <br />
  then run the function "plot_graph" from GraphAlgo- its will ask you about showing the simple graph (like the images above) or Gui with options of runing the algorithms
  like: TSP, Center, Load, Save and Shortest Path - Enjoy!<br />
  
  #### example of TSP of A1.json on cities: [3, 8, 2, 9]:  
  ![image](https://user-images.githubusercontent.com/77155986/147288789-c974c0a0-b5c9-46d6-b0b6-5db8240db75d.png)

  #### example of CENTER of A1.json:  
  ![image](https://user-images.githubusercontent.com/77155986/147288678-c9a78cf6-2f0e-4684-86dd-02725d20f11c.png)
  
  #### example of SHORTEST PATH of A1.json from 5 to 10: 
  ![image](https://user-images.githubusercontent.com/77155986/147288908-68cfe380-341f-48ec-93cb-ea18c6b6bb20.png)


  

  
  

