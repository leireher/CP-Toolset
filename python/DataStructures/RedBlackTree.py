class RBNode:
    def __init__(self, item):
        self.item = item
        # 0 -> Parent, 1 -> Left, 2 -> Right
        self.pointers = [None, None, None]
        self.color = 1  # 0 -> Black, 1 -> Red


class RBTree:
    def __init__(self):
        self.TNULL = RBNode(0)
        self.TNULL.color = 0
        self.TNULL.pointers[1] = None
        self.TNULL.pointers[2] = None
        self.root = self.TNULL

    def _rb_transplant(self, u, v):
        if u.pointers[0] is None:
            self.root = v
        elif u == u.pointers[0].pointers[1]:
            u.pointers[0].pointers[1] = v
        else:
            u.pointers[0].pointers[2] = v
        v.pointers[0] = u.pointers[0]

    def _rotate_helper(self, x, i, j):
        y = x.pointers[i]
        x.pointers[i] = y.pointers[j]
        if y.pointers[j] != self.TNULL:
            y.pointers[j].pointers[0] = x

        y.pointers[0] = x.pointers[0]
        if x.pointers[0] is None:
            self.root = y
        elif x == x.pointers[0].pointers[j]:
            x.pointers[0].pointers[j] = y
        else:
            x.pointers[0].pointers[i] = y
        y.pointers[j] = x
        x.pointers[0] = y

    def _search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.item:
            return node

        if key < node.item:
            return self._search_tree_helper(node.pointers[1], key)
        return self._search_tree_helper(node.pointers[2], key)

    def _delete_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.pointers[2]
            else:
                node = node.pointers[1]

        # Key not in the tree
        if z == self.TNULL:
            return

        y = z
        y_original_color = y.color
        if z.pointers[1] == self.TNULL:
            x = z.pointers[2]
            self._rb_transplant(z, z.pointers[2])
        elif z.pointers[2] == self.TNULL:
            x = z.pointers[1]
            self._rb_transplant(z, z.pointers[1])
        else:
            y = self.minimum(z.pointers[2])
            y_original_color = y.color
            x = y.pointers[2]
            if y.pointers[0] == z:
                x.pointers[0] = y
            else:
                self._rb_transplant(y, y.pointers[2])
                y.pointers[2] = z.pointers[2]
                y.pointers[2].pointers[0] = y

            self._rb_transplant(z, y)
            y.pointers[1] = z.pointers[1]
            y.pointers[1].pointers[0] = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    def _min_max_helper(self, node, i):
        while node.pointers[i] != self.TNULL:
            node = node.pointers[i]
        return node

    def _predecessor_successor_helper(self, x, i, func):
        if x.pointers[i] != self.TNULL:
            return func(x.pointers[i])

        y = x.pointers[0]
        while y != self.TNULL and x == y.pointers[i]:
            x = y
            y = y.pointers[0]
        return y

    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.pointers[0].pointers[1]:
                s = x.pointers[0].pointers[2]
                if s.color == 1:
                    s.color = 0
                    x.pointers[0].color = 1
                    self.left_rotate(x.pointers[0])
                    s = x.pointers[0].pointers[2]

                if s.pointers[1].color == 0 and s.pointers[2].color == 0:
                    s.color = 1
                    x = x.pointers[0]
                else:
                    if s.pointers[2].color == 0:
                        s.pointers[1].color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.pointers[0].pointers[2]

                    s.color = x.pointers[0].color
                    x.pointers[0].color = 0
                    s.pointers[2].color = 0
                    self.left_rotate(x.pointers[0])
                    x = self.root
            else:
                s = x.pointers[0].pointers[1]
                if s.color == 1:
                    s.color = 0
                    x.pointers[0].color = 1
                    self.right_rotate(x.pointers[0])
                    s = x.pointers[0].pointers[1]

                if s.pointers[2].color == 0 and s.pointers[2].color == 0:
                    s.color = 1
                    x = x.pointers[0]
                else:
                    if s.pointers[1].color == 0:
                        s.pointers[2].color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.pointers[0].pointers[1]

                    s.color = x.pointers[0].color
                    x.pointers[0].color = 0
                    s.pointers[1].color = 0
                    self.right_rotate(x.pointers[0])
                    x = self.root
        x.color = 0

    def insert_fix(self, k):
        while k.pointers[0].color == 1:
            if k.pointers[0] == k.pointers[0].pointers[0].pointers[2]:
                u = k.pointers[0].pointers[0].pointers[1]
                if u.color == 1:
                    u.color = 0
                    k.pointers[0].color = 0
                    k.pointers[0].pointers[0].color = 1
                    k = k.pointers[0].pointers[0]
                else:
                    if k == k.pointers[0].pointers[1]:
                        k = k.pointers[0]
                        self.right_rotate(k)
                    k.pointers[0].color = 0
                    k.pointers[0].pointers[0].color = 1
                    self.left_rotate(k.pointers[0].pointers[0])
            else:
                u = k.pointers[0].pointers[0].pointers[2]

                if u.color == 1:
                    u.color = 0
                    k.pointers[0].color = 0
                    k.pointers[0].pointers[0].color = 1
                    k = k.pointers[0].pointers[0]
                else:
                    if k == k.pointers[0].pointers[2]:
                        k = k.pointers[0]
                        self.left_rotate(k)
                    k.pointers[0].color = 0
                    k.pointers[0].pointers[0].color = 1
                    self.right_rotate(k.pointers[0].pointers[0])
            if k == self.root:
                break
        self.root.color = 0

    def minimum(self, node):
        return self._min_max_helper(node, 1)

    def maximum(self, node):
        return self._min_max_helper(node, 2)

    def successor(self, x):
        return self._predecessor_successor_helper(x, 2, self.minimum)

    def predecessor(self, x):
        return self._predecessor_successor_helper(x, 1, self.maximum)

    def left_rotate(self, x):
        self._rotate_helper(x, 2, 1)

    def right_rotate(self, x):
        self._rotate_helper(x, 1, 2)

    def search_tree(self, k):
        return self._search_tree_helper(self.root, k)

    def insert(self, key):
        node = RBNode(key)
        node.pointers[0] = None
        node.item = key
        node.pointers[1] = self.TNULL
        node.pointers[2] = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.pointers[1]
            else:
                x = x.pointers[2]

        node.pointers[0] = y
        if y is None:
            self.root = node
        elif node.item < y.item:
            y.pointers[1] = node
        else:
            y.pointers[2] = node

        if node.pointers[0] is None:
            node.color = 0
            return

        if node.pointers[0].pointers[0] is None:
            return

        self.insert_fix(node)

    def delete(self, item):
        self._delete_helper(self.root, item)

    @classmethod
    def from_collection(cls, values):
        tree = RBTree()
        for v in values:
            tree.insert(v)
        return tree
