import heapq
class Node:
    def __init__(self, x, char=None):
        self.data = x
        self.char = char
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.data < other.data

def preOrder(root, ans, curr):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        ans[root.char] = curr if curr else '0' 
        return
    if root.left:
        preOrder(root.left, ans, curr + '0')
    if root.right:
        preOrder(root.right, ans, curr + '1')

def huffmanCodes(s, freq):
    n = len(s)
    if n == 1:
        root = Node(freq[0], s[0])
        return root, {s[0]: '0'}
    
    arr = []
    for i in range(n):
        temp = Node(freq[i], s[i])
        heapq.heappush(arr, temp)
       
    while len(arr) > 1: 
        left = heapq.heappop(arr)
        right = heapq.heappop(arr)
        newNode = Node(left.data + right.data)
        newNode.left = left
        newNode.right = right
        
        heapq.heappush(arr, newNode)
    root = arr[0]
    ans = {}
    preOrder(root, ans, "")
    
    return root, ans

s = "abcdef"
freq = [5, 9, 10, 3, 23, 19]

def print_tree_structure(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + f"Data={node.data}" + 
              (f", Char='{node.char}'" if node.char else ""))
        if node.left or node.right:
            if node.left:
                print_tree_structure(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree_structure(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

if __name__ == "__main__":
    root, codes = huffmanCodes(s, freq)
    
    print("Huffman Codes:")
    for char, code in codes.items():
        print(f"'{char}': {code}")
    
    print(f"\nTotal characters: {len(s)}")
    print(f"Characters: {list(s)}")
    print(f"Frequencies: {freq}")
    
    print("\nTree Structure:")
    print_tree_structure(root)
    
    original_bits = len(s) * 8  
    compressed_bits = sum(freq[i] * len(codes[s[i]]) for i in range(len(s)))
    print(f"\nCompression Analysis:")
    print(f"Original size (8 bits/char): {original_bits} bits")
    print(f"Huffman encoded size: {compressed_bits} bits")
    print(f"Compression ratio: {compressed_bits/original_bits:.2%}")
