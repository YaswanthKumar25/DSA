class Solution:
    def isomorphicString(self, s : str, t : str) -> bool:
        hash={}
        hash2={}
        for i in range(len(s)):
            if s[i] in hash:
                if hash[s[i]] == t[i]:
                    hash[s[i]]=t[i]
                else:
                    return False
            else:
                hash[s[i]]=t[i]
              
            if t[i] in hash2:
                if hash2[t[i]] == s[i]:
                    hash2[t[i]]=s[i]
                else:
                    return False
            else:
                hash2[t[i]]=s[i]
        return True