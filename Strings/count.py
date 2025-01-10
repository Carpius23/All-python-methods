class Count_method():
    def __init__(self, chain):
            self.chain = chain
    def Count( self, sub_chain, start_index = 0, end_index = None):
        end_index = end_index if end_index is not None else len(self.chain)
        times = 0
        if isinstance(self.chain, (list, tuple)):
            for key in range(start_index, end_index):
                if self.chain[key] == sub_chain:
                    times += 1
        elif isinstance(self.chain, str):
            replaced = self.chain.replace(sub_chain, "🐯")
            replaced = list(replaced)
            for key in range(start_index, min(end_index, len(replaced))):
                if replaced[key] == "🐯":
                    times += 1
        return times
my_chain = Count_method("Hello hello Hello HelloWorld")
print(my_chain.Count("Hello"))
