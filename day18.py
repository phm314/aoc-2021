import sys

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.left}, {self.right}]"

    def insert(self, value):
        """ sets left then right """
        if self.left is None:
            self.left = value
        elif self.right is None:
            self.right = value
        else:
            print("? insert")

    def p_flat(self):
        """ recurseive flatten generator """
        for elem in self.left, self.right:
            if isinstance(elem, int):
                yield elem
            else:
                yield from elem.p_flat()

def make_tree(arr):
    pair = Node()
    for elem in arr:
        if isinstance(elem, list):
            pair.insert(make_tree(elem))
        else:
            pair.insert(elem)
    return pair

def reduce(pair):
    while (instr := _reduce(pair)) is not None:
        print("i", instr)

def _reduce(pair, depth=0):
    #print("d", depth, "p", pair)
    if depth == 4:
        print("explode:", pair)
        return "explode", pair
    for elem in pair.left, pair.right:
        if isinstance(elem, Node):
            if (tmp := _reduce(elem, depth+1)) is not None:
                if tmp[0] == "explode":
                    # recursively return and search for closest
                    return tmp
                return tmp
        elif isinstance(elem, int) and elem >= 10:
            print("split")
            if not elem % 2:
                n1, n2 = elem // 2, elem // 2
            else:
                n1, n2 = elem // 2, elem // 2 + 1
            new = Node(n1, n2)
            if elem is pair.left:
                pair.left = new
            else:
                pair.right = new
            return "split"
    return None

def _add(pair, num, direction=0):
    """ searches directionmost closest number """
    if direction == 0:
        return
        

with open(sys.argv[1]) as raw_data:
    while (line := raw_data.readline().strip()):
        # lines come formatted as lists
        ln = eval(line)
        tree = make_tree(ln)
        #print("t", tree.left, tree.right)
        reduce(tree)
        #print("f", *tree.p_flat())
        break
