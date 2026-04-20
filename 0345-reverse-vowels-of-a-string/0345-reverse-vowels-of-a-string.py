class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']

        char = list(s)

        n = len(char)

        i= 0
        j= n - 1

        while i < j:
            if char[i] not in vowels:
                i+=1
            elif char[j] not in vowels:
                j-=1
            elif char[i] in vowels and char[j] in vowels:
                    char[i],char[j] = char[j],char[i]
                    i+=1
                    j-=1
        
        return "".join(char)
