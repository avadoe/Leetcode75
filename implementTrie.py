import collections

class TrieNode:
  def __init__(self):
    self.children = collections.defaultdict(TrieNode)
    self.isWord = False


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node: TrieNode = self.root
    for c in word:
      if c not in node.children:
        node.children[c] = TrieNode()
      node = node.children[c]
    node.isWord = True

  def search(self, word):
    node: TrieNode = self._find(word)
    return node and node.isWord

  def startsWith(self, prefix: str) -> bool:
    return self._find(prefix)

  def _find(self, prefix):
    node: TrieNode = self.root
    for c in prefix:
      if c not in node.children:
        return None
      node = node.children[c]
    return node
