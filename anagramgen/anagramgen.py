from random import randrange

class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word):
        self.__add(self.root, word[0], word[1:])

    def __add(self, node, prefix, suffix):
        if prefix not in node:
            node[prefix] = {}
        if suffix == "":
            node[prefix][suffix] = ""
        else:
            new_prefix = suffix[0]
            new_suffix = suffix[1:]
            self.__add(node[prefix], new_prefix, new_suffix)

    def __contains__(self, word):
        word = list(word)
        index_string = "['" + "']['".join(word) + "']"
        try:
            child_nodes = eval("self.root"+index_string)
            if '' in child_nodes:
                return True
        except KeyError:
            pass
        return False

class AnagramGenerator:
    def __init__(self, corpus):
        self.t = Trie()
        for word in corpus:
            word = word.rstrip()
            self.t.add(word)

    def frequency_dict(self, string):
        f = {}
        for letter in string:
            if letter not in f:
                f[letter] = 0
            f[letter] += 1
        return f

    def generate(self, string):
        string = string.lower()
        for c in string:
            if c not in 'abcdefghijklmnopqrstuvwxyz':
                string = string.replace(c, "")

        anagrams = []
        f = self.frequency_dict(string)
        self.__generate(anagrams, self.t.root, [], "", f)

        return anagrams

    def __generate(self, anagrams, node, partial_anagram, current_word, f):
        if '' in node: # if we have just finished generating a word
            next_partial_anagram = partial_anagram + [current_word]
            if all([f[key] == 0 for key in f]): # if there are no more letters
                anagrams.append(next_partial_anagram) # then this is a full phrase anagram
            else:
                self.__generate(anagrams, self.t.root, next_partial_anagram, "", f) # so loop back to the top of the tree with a new word and add a space to the anagram phrase we are building

        for prefix in f:
            if f[prefix] > 0:
                if prefix in node:
                    new_word = current_word+prefix
                    if len(partial_anagram) == 0 or new_word >= partial_anagram[-1][:len(new_word)]:
                        f[prefix] -= 1 # since f is shared between function calls we need to subtract from it
                        self.__generate(anagrams, node[prefix], partial_anagram, current_word+prefix, f)
                        f[prefix] += 1 # then add back
