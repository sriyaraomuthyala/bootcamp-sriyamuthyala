import json

class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

node1 = Node("A")
node2 = Node("B")
node1.ref = node2
node2.ref = node1  # Cyclic reference

# Custom serialization to avoid recursion errors
def custom_serializer(obj):
    if isinstance(obj, Node):
        return {"value": obj.value, "ref": obj.ref.value if obj.ref else None}
    raise TypeError("Type not serializable")

json_data = json.dumps(node1, default=custom_serializer)
print(json_data)
