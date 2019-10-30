class Node(object):
  def __init__(self, keys=[], children=[], isleaf=True, max_keys):
        self.keys = keys
        self.children = children
        self.isleaf = isleaf
        if max_keys < 3:  # max_num_keys must be odd and greater or equal to 3
            max_mkeys = 3
        if max_keys % 2 == 0:  # max_num_keys must be odd and greater or equal to 3
            max_keys += 1
        self.max_keys = max_keys

  def is_full(self):
      return len(self.keys) >= self.max_num_keys
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
    def BTsearch(self,node,key):
        if node is None:
            node = self.root
        if key in node.keys:
            return node
        if node.isleaft:
            return None
        return self.BTreeSplit(key,node.children[self.find])    
    def BTreeSplit(self,node):
        if node is None:
            node = self.root
        middle = node.maxnumkeys//2
        if node.isleaf:
            leftC = Node(node.keys[:middle],maxnumkeys = node.maxnumkeys)
            rigthC = Node(node.keys[middle + 1:],maxnumkeys = node.maxnumkeys)
        else:
            leftC = Node(node.keys[:middle],node.children[:middle + 1],node.isleaft,maxnumkeys = node.maxnumkeys)
            rigthC = Node(node.keys[middle + 1:],node.keys[middle + 1:],maxnumkeys = node.maxnumkeys)
        return node.keys[middle], leftC, rigthC   

