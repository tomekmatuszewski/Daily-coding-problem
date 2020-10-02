class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(tree):
    values = []

    def serializer(node):
        if not node:
            values.append('x')
        else:
            values.append(str(node.val))
            serializer(node.left)
            serializer(node.right)

    serializer(tree)

    return ' '.join(values)


def deserialize(serialized_string):
    elements = iter(serialized_string.split(' '))

    def deserializer():
        element = next(elements)

        if element == 'x':
            return None
        else:
            node = Node(element)
            node.left = deserializer()
            node.right = deserializer()
            return node

    return deserializer()