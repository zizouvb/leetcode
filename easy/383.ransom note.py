class Solution:
    def canConstruct(self, ransomNote, magazine):
        available_letters = {}
        for l in magazine:
            if (l in available_letters): available_letters[l]+=1
            else: available_letters[l]=1
        for l in ransomNote:
            if l not in available_letters: return False
            if available_letters[l]==0: return False
            available_letters[l]-=1
        return True



print(Solution().canConstruct("aa","ab"))
        