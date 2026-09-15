class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        left=0
        right=len(skill)-1
        target=skill[left]+skill[right]
        chemistry=0
        while left<right:
            current_sum=skill[left]+skill[right]
            if current_sum != target:
                return -1
            chemistry +=skill[left]*skill[right]
            left=left+1
            right=right-1
        return chemistry
        