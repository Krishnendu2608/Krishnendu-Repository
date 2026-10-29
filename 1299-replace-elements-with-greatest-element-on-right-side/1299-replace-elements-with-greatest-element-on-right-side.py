class Solution(object):
    def replaceElements(self, arr):
        max_el=-1
        new_arr=[]
        for i in arr[::-1]:
            new_arr.append(max_el)
            if i>max_el:
                max_el=i
        return new_arr[::-1]

        