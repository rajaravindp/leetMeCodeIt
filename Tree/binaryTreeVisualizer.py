import matplotlib.pyplot as plt
import numpy as np

class TreeVisualizer:
    def __init__(self, root):
        self.root = root
        
    def _get_tree_height(self, node):
        if not node:
            return 0
        return 1 + max(self._get_tree_height(node.left), self._get_tree_height(node.right))
    
    def _get_tree_width(self, node):
        if not node:
            return 0
        return 1 + self._get_tree_width(node.left) + self._get_tree_width(node.right)
    
    def _plot_node(self, node, x, y, dx, dy):
        if not node:
            return
            
        # Plot current node
        circle = plt.Circle((x, y), 0.3, color='lightblue', fill=True)
        plt.gca().add_patch(circle)
        plt.text(x, y, str(node.val), horizontalalignment='center', verticalalignment='center')
        
        # Plot left child
        if node.left:
            next_x = x - dx
            next_y = y - dy
            plt.plot([x, next_x], [y, next_y], 'k-')
            self._plot_node(node.left, next_x, next_y, dx/2, dy)
            
        # Plot right child
        if node.right:
            next_x = x + dx
            next_y = y - dy
            plt.plot([x, next_x], [y, next_y], 'k-')
            self._plot_node(node.right, next_x, next_y, dx/2, dy)
    
    def plot_tree(self):
        if not self.root:
            return
            
        height = self._get_tree_height(self.root)
        width = self._get_tree_width(self.root)
        
        # Create a new figure with a larger size
        plt.figure(figsize=(width*2, height*2))
        
        # Create axis with equal aspect ratio
        plt.gca().set_aspect('equal')
        
        # Initial position and spacing
        start_x = 0
        start_y = height
        dx = width/2
        dy = 1
        
        # Plot the tree
        self._plot_node(self.root, start_x, start_y, dx, dy)
        
        # Set the plot limits
        plt.xlim(-width, width)
        plt.ylim(0, height+1)
        
        # Remove axes
        plt.axis('off')
        
        # Show the plot
        plt.show()