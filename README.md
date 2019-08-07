

# Classes

* Geometry: 
  * Point: Represent a cell location or robot location
  * Vector: Represent direction to move and unit
* Cardinals:
  * WindRose: Represent Vector get from a clockwise or anti_clockwise rotation
* Grid: set of cells
* Simulator / Robot

Since computer cannot represent infinite matrix data structure (grid), 
I decided to build incrementally the cells the robot is flipping while moving

At each step we build up a dictionary of [Position -> Cell]
Since we must flip cell from White <-> Black we must be able to retrieve a cell where the robot has already be in.

I mentionned I used a python dictionary. Average complexity is O(1) and worst case is O(N).
Means this algorithm at the moment is in average O(n) and in worst O(n^2)


To apply rotation we just need to make a modulo 4 operations on the class WindRose where CardinalPoints are stored in an array of Vectors.


```
curl -XPUT http://127.0.0.1:5000/simulator/1000
```

can download the output file through endpoint: /downloads/filename

```
curl http://127.0.0.1:5000/downloads/simulation-6b7728e6-b8a6-11e9-babf-3c6aa789774f
```


# Improvement

output file is a sparse matrix. We could look on how manage them