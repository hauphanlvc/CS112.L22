import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.stdin = open("InputSortedArraytoBalanceBST.txt","r")
sys.stdout = open("OutputSortedArraytoBalanceBST.txt","w")
sys.setrecursionlimit(150000)
class Node:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x
def Xuli(a):
    if not a:
        return None 
    mid = len(a)//2
    root = Node(a[mid])
    root.left= Xuli(a[:mid])
    root.right= Xuli(a[mid+1:])
    return root
def PrintLRN(node):
    if not node : 
        return
    PrintLRN(node.left)
    PrintLRN(node.right)
    print(node.val)
Array = list()
while True:
    try:
        x = int(input())
        Array.append(x)
    except:
        # root = Xuli(Array)
        PrintLRN(Xuli(Array))
        break