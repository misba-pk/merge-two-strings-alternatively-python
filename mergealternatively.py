class Solution(object):   
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
    def mergeAlternatively(self):
        for i in range(max(len(self.word1),len(self.word2))):
          if i in range(len(self.word1)):
             print(self.word1[i])
          if i in range(len(self.word2)):
             print(self.word2[i])
               
        

w1=input("enter word1:")
w2=input('enter word2:')
obj= Solution(w1,w2)
obj.mergeAlternatively()