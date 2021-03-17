class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:  # NodeManagement
    def __init__(self, head):
        self.head = head  # root node

    def insert(self, value):
        # 항상 처음 시작하는 검색 노드 값은 head(root node) 값
        self.current_node = self.head

        while True:
            # 값 < 현재 검색 노드 값
            if value < self.current_node.value:
                if self.current_node.left is not None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node = Node(value)
                    break

            # 값 > 현재 검색 노드 값
            else:
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

