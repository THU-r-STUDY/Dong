# linkedlist class init
class linkedlist:
    def __init__(self, value):
        self.value = value
        self.next = None
#printNode method init
def printNode(node):
    n = node
    while n.next is not None:
        print(n.value)
        n = n.next
    else:
        print(n.value)

rootnode = linkedlist(1)                    #rootnode
rootnode.next = linkedlist(2)               #rootnode connect secondnode
rootnode.next.next = linkedlist(3)          #secondnode connect thirdnode
rootnode.next.next.next = linkedlist(4)     #thirdnode connect fourthnode

printNode(rootnode)                         #print Node Value