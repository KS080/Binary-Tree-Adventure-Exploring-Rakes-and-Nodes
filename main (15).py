# Necessary imports
import random
import matplotlib.pyplot as plt

#Defining class RNode
class RNode:
  # Initialize the RNode object with default values using __init__ which is magic method and we won't have to call it anywhere it calls itself
  def __init__(self, id=0, has_rake=False):
    self.left = None # making the default values none
    self.right = None # making the default values none
    self.id = id
    self.has_rake = has_rake

  # Generate two new random child nodes (if the current node doesn't have a rake)
  def ask(self):
    if not self.has_rake:
      ids = [self.id]
      # Generate two unique random IDs
      while len(ids) < 3:
        random_id = random.randint(1, 100)
        if random_id not in ids:
            ids.append(random_id)
      # Assign the new random ids to left and right child nodes
      # Check if the id is one of [13, 42, 99] to determine the `has_rake` attribute
      self.left = RNode(ids[1], ids[1] in [13, 42, 99])
      self.right = RNode(ids[2], ids[2] in [13, 42, 99])

  # Recursively generate a binary tree to a specified depth
  def make_tree(self, depth):
    if depth == 0 or self.has_rake:
      return
    self.ask()
    if self.left:
      self.left.make_tree(depth-1)
    if self.right:
      self.right.make_tree(depth-1)

  # Pre-order traversal of the tree
  def pre_traverse(self):
    print(self.id)
    if self.left:
      self.left.pre_traverse() #Using recursion for traversal of the tree
    if self.right:
      self.right.pre_traverse() #Using recursion for traversal of the tree

  # Count unique node IDs in the tree
  def count_unique(self, ids_set=None):
    if ids_set is None:
      ids_set = set()
    ids_set.add(self.id)
    if self.left:
      self.left.count_unique(ids_set) #Using recursion to count
    if self.right:
      self.right.count_unique(ids_set) #Using recursion to count
    return len(ids_set)

  # Plot the tree structure using matplotlib
  def tree_plot(self, *args):
    fig, ax = plt.subplots()
    self._plot(ax, x=0.5, y=1, dx=0.5, dy=0.1, highlighted_ids=args) #specifying its x y dx dy values
    plt.show()

  # Helper function to recursively plot the tree structure
  def _plot(self, ax, x, y, dx, dy, highlighted_ids):
      # Highlight nodes with IDs 13, 42, or 99
    color = 'red' if self.id in highlighted_ids else 'yellow'
    ax.plot(x, y, 'o', color=color)
    ax.text(x, y, str(self.id), ha='center', va='center')
    if self.left:
      ax.plot([x, x-dx], [y, y-dy], color='blue')
      self.left._plot(ax, x-dx, y-dy, dx/2, dy+1, highlighted_ids)
    if self.right:
      ax.plot([x, x+dx], [y, y-dy], color='blue')
      self.right._plot(ax, x+dx, y-dy, dx/2, dy+1, highlighted_ids)

# Create an RNode instance, generate a tree, traverse the tree, count unique IDs and plot the tree
node = RNode()
node.make_tree(5)
node.pre_traverse()
# print("Unique IDs:", node.count_unique())
node.tree_plot(13, 42, 99)