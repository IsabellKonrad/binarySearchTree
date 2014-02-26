import numpy as np
import matplotlib.pyplot as plt


class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    
    def maximum(self):
        x = self
        while x.right != None:
            x=x.right
        return x
    
    def minimum(self):
        x = self
        while x.left != None:
            x=x.left
        return x
    
    def predecessor(self):
        x = self
        if x.left != None:
            return x.left.maximum()
        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y
        
        
        
        
        

class Tree:
    def __init__(self,root):
        self.root = root
        root.left = None
        root.right = None
        
    def insert(self,z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = None
        z.right = None
            
    def transplant(self,u,v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
            
    def delete(self,z):
        if z.left == None:
            self.transplant(z,z.right)
        elif z.right == None:
            self.transplant(z,z.left)
        else:
            y = z.right.minimum()
            if y.parent != z:
                self.transplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z,y)
            y.left = z.left
            y.left.parent = y   
                
    def maximum(self):
       return self.root.maximum()
    
    def predecessor(self):
        return self.root.predecessor()
       

def treeplot(tree):
    fig, ax = plt.subplots()
    axx = float(4)
    axy = float(4)
    plt.axis('off')
 
    
    def plotchildren(anode,height,xparent,yparent):
        item = str(anode.key)
        ax.text(xparent,yparent, item, fontsize=15, color="black")
        
        if anode.left != None:
            xleft = xparent - axx/2**height
            yleft = yparent - 0.4
            ax.plot([xparent, xleft],[yparent, yleft],color='magenta')
            plotchildren(anode.left,height+1,xleft,yleft)
            
        
        if anode.right != None:
            xright = xparent + axx/2**height
            yright = yparent - 0.4
            plotchildren(anode.right,height+1,xright,yright)
            ax.plot([xparent, xright],[yparent, yright],color='magenta')
        
        
    height = 1
    number = 1
    xparent = axx/2
    yparent = axy
    plotchildren(tree.root,height,xparent,yparent)
    


