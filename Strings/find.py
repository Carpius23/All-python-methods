class FindMethod():
    def __init__(self, chain):
        self.chain = chain
    
    def Find(self, searched, start_index = 0, end_index = None):
        end_index = end_index if end_index is not None else len(self.chain)
        if isinstance(self.chain, str):
            if isinstance(searched, str) and len(searched):
                chain_l = list(self.chain)
                searched_l = list(searched)
                for i in range(start_index, len(chain_l)):
                    if searched_l[0] !=  chain_l[i]:
                        continue
                    elif searched_l[0] ==  chain_l[i]:
                        index = i
                        sliced = chain_l[index:]
                        if len(searched_l) > len(sliced):
                            return -1
                        elif len(searched_l) <= len(sliced):
                            counter = 0
                            for j in range(len(searched_l)):
                                if searched_l[j] == sliced[j]:
                                    counter += 1
                                else:
                                    break
                            if counter == len(searched):
                                return index
                return -1
            else:
                return -1
            
                            
                            
            

word = FindMethod("Hello Hi boy")
print(word.Find("b",start_index=6))
                    
            
        
