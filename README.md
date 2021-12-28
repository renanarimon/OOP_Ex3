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

  ## After runing chack0() we get the folow plot:<br />
  ![image](https://user-images.githubusercontent.com/77155986/147467181-a152ac5c-d46b-40f1-9013-9b7b7115366c.png)  
  ## After runing chack1() we get the folow plot:<br />
  ![image](https://user-images.githubusercontent.com/77155986/147466445-0ddb8b3f-f310-439a-9bb3-025242032cba.png)
  ## After runing chack2() we get the folow plot:<br />
  ![image](https://user-images.githubusercontent.com/77155986/147466486-bf5bab57-7722-4623-afaf-6f1fc910ad2f.png)

  
  ## TSP of A1.json on cities: [3, 8, 2, 9]:  
  ![image](https://user-images.githubusercontent.com/77155986/147466829-4980e4fa-205a-44db-ba83-b5f941c9d7c3.png)

  ## CENTER of A1.json:  
  ![image](https://user-images.githubusercontent.com/77155986/147466868-994b803b-9986-4f55-afb9-ce5446dede89.png)
  
  ## SHORTEST PATH of A1.json from 5 to 10: 
  ![image](https://user-images.githubusercontent.com/77155986/147466915-755ad505-c81f-40a1-963a-f8c7d8f3bbcc.png)


  # How to run the program : 
  in the main.py: go to main and create a AlgoGraph on this way:<br />
     - g_algo = GraphAlgo() <br />
     - file = '../data/A5.json' (enter a jason file you wuold like to load) <br />
     - g_algo.load_from_json(file) <br />
     - g_algo.plot_graph

  
  

