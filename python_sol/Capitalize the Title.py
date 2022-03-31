class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        lst=[]
        #capitalized_words = [w.capitalize() for w in words]
        #return " ".join(capitalized_words)
        for w in words:
            if(len(w)<3):
                capitalized_words = w.lower()
                lst.append(capitalized_words)
            else:
                capitalized_words = w.capitalize()
                lst.append(capitalized_words)
        return " ".join(lst)
                