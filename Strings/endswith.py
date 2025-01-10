class EndsWithFunciton():
    def __init__(self, chain):
        self.chain = chain
    def EndsWith(self, suffix, start_index = 0, end_index = None):
        end_index = end_index if end_index is not None else len(self.chain)
        if isinstance(self.chain, str):
            replaced = self.chain.replace(suffix, "🐯")
            replaced = list(replaced)
            last_one = len(replaced) - 1
            if replaced[last_one] == "🐯":
                return True
            else:
                return False
        else:
            print("A string was expected")
        
word = EndsWithFunciton("hola.txt.txt")
print(word.EndsWith("txt"))

