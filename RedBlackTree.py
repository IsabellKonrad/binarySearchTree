import numpy as np
import matplotlib.pyplot as plt




class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'
    
    def maximum(self):
        x = self
        while x.right.key != 'nil':
            x=x.right
        return x
    
    def minimum(self):
        x = self
        while x.left.key != 'nil':
            x=x.left
        return x
    
    def predecessor(self):
        x = self
        if x.left.key != 'nil':
            return x.left.maximum()
        y = x.parent
        while y.key != 'nil' and x == y.left:
            x = y
            y = y.parent
        return y
        
        
        
        
        

class tree:
    def __init__(self,root):
        self.root = root
        self.root.color = 'black'
        self.nil = node('nil')
        self.nil.color = 'black'
        self.root.left = self.nil
        self.root.right = self.nil
        self.root.parent = self.nil
        
        
        
    def leftrotate(self,anode):
        y = anode.right
        anode.right = y.left
        if y.left != self.nil:
            y.left.parent = anode
        y.parent = anode.parent
        if anode.parent == self.nil:
            self.root = y
            y.parent = self.nil
        elif anode == anode.parent.left:
            anode.parent.left = y
        else:
		anode.parent.right = y
        y.left = anode
        anode.parent = y
    
    
    def rightrotate(self,anode):
        y = anode.left
        anode.left = y.right
        if y.right != self.nil:
            y.right.parent = anode
        y.parent = anode.parent
        if anode.parent == self.nil:
            self.root = y
            y.parent = self.nil
        elif anode == anode.parent.right:
            anode.parent.right = y
        else:
            anode.parent.left = y
        y.right = anode
        anode.parent = y

        
    def insertfixup(self,anode):
        z = anode
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.leftrotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.rightrotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rightrotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.leftrotate(z.parent.parent)
        self.root.color = 'black'
    
    
    def insert(self,z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 'red'
        self.insertfixup(z)
    
                
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
        nodecolor = anode.color
        ax.text(xparent,yparent, item, fontsize=15, color=nodecolor)
        
        if anode.left.key != 'nil':
            xleft = xparent - axx/2**height
            yleft = yparent - 0.4
            ax.plot([xparent, xleft],[yparent, yleft],color='blue')
            plotchildren(anode.left,height+1,xleft,yleft)
            
        
        if anode.right.key != 'nil':
            xright = xparent + axx/2**height
            yright = yparent - 0.4
            plotchildren(anode.right,height+1,xright,yright)
            ax.plot([xparent, xright],[yparent, yright],color='blue')
        
        
    height = 1
    number = 1
    xparent = axx/2
    yparent = axy
    plotchildren(tree.root,height,xparent,yparent)
    
 
        


