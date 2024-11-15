class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_a_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_a_word = True

    def has_prefix(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def get_words_starts_with(self, prefix):
        def dfs(node, prefix, result):
            if node.is_end_of_a_word:
                result.append(prefix)
            for char, child_node in node.children.items():
                dfs(child_node, prefix + char, result)

        current = self.root
        result = []
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return result
        dfs(current, prefix, result)
        return result

    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_a_word


# tests

# trie = Trie()
# trie.insert('app')
# trie.insert('apple')
# trie.insert('apricot')
# print(trie.has_prefix('ap'))
# print(trie.search('app'))
# print(trie.search('apple'))
# print(trie.search('ap'))
# print(trie.get_words_starts_with('ap'))
# print(trie.get_words_starts_with('app'))

# tests
