GraphTheoryTutor
================
Graph Theory Tutor creates visualizations of various algorithms running on different data structure.
More over the user can also input his/her own code and see it running on the data structure.

### Visualization
Visualization would consist of two parts. One part would be running [PythonTutor](http://pythontutor.com/).
Python Tutor would be showing the value of different variables at each step of execution.
The other part would be having visual representation of the data structures. For example for a linked list
it would consist of circular node connected by lines showing the structure. Visualizations would be created 
by showing various variables pointing to nodes, changing color, facecolor, alpha, size and node style.

### User Input Code
User will have to use some predefined classes like node class. We will be tracking these objects and according 
to the changes in it, the visuals will be created.

### Working
The front-end would send the data structure and the code entered by the user to the backend. In the backend we
will create a json object that would have all the information of each step of the visualization. This would
be sent back to the front-end and using this the front-end will create a visualization.

### Example
##### Normal Linked list traversal 
```python
current_node = head
while current_node != None:
   current_node = current_node.next
```
In this case the visualization would show a pointer named current_node pointing to the head of the linked list and with the execution of each loop the pointer would point to the next node.

Now if we want to create a visualization such that the traversed node has a different color than the non-traversed node.
```python
current_node = head
while current_node != None:
    current_node.color = 'Black'
    current_node = current_node.next
```
