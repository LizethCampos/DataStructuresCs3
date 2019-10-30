class Node(object):
  def __init__(self, keys=[], children=[], isleaf=True, max_keys):
        self.keys = keys
        self.children = children
        self.isleaf = isleaf
        if max_keys < 3:  
            max_mkeys = 3
        if max_keys % 2 == 0: 
            max_keys += 1
        self.max_keys = max_keys

  def is_full(self):
      return len(self.keys) >= self.max_keys
class B_Trees:
    def __init__(self, root=None):
        self.root = root
    def Child(self,key,node):
        if node is None:
            node = self.root
        for i in range(len(node.key)):
            if key < node.keys[i]:
                return i
        return len(node.key)    
    def search(self,node,key):
        if node is None:
            node = self.root
        if key in node.keys:
            return node
        if node.isleaf:
            return None
        return self.Split(key,node.children[self.find])    
    def Split(self,node):
        if node is None:
            node = self.root
        middle = node.max_keys//2
        if node.isleaf:
            left = Node(node.keys[:middle],max_keys = node.max_keys)
            rigth = Node(node.keys[middle + 1:],max_keys = node.max_keys)
        else:
            left = Node(node.keys[:middle],node.children[:middle + 1],node.isleaf,maxnumkeys = node.max_keys)
            rigth = Node(node.keys[middle + 1:],node.keys[middle + 1:],max_keys = node.max_keys)
        return node.keys[middle], left, rigth   

