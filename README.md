AI-program that solves the 8-puzzle   
8 pieces scattered initially in 3x3 shape, 1 piece is an empty spot where neighboring pieces can move. The goal is to assemble them in a certain order. 
In my case: 
0 1 2  
3 4 5  
6 7 8  

Implemented with 2 versions of A* search
One uses Manhattan distance heuristic function, the other simple displacement

Input8PuzzleCases.txt contains 100 test cases

Examples:

Specific solutions can be viewed showing each move:  
![alt text](https://github.com/LuckyKot/Astar/blob/eef7c607c5454add923c0f637ea76805b26f47bf/example1.png)

Until it reaches the final desired state:  
![alt text](https://github.com/LuckyKot/Astar/blob/eef7c607c5454add923c0f637ea76805b26f47bf/example2.png)

Solution of 100 cases begins:  
![alt text](https://github.com/LuckyKot/Astar/blob/eef7c607c5454add923c0f637ea76805b26f47bf/example3.png)

Stats at the end of 100 cases:  
![alt text](https://github.com/LuckyKot/Astar/blob/eef7c607c5454add923c0f637ea76805b26f47bf/example4.png)
