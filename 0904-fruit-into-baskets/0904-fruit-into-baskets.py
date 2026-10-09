class Solution(object):
    def totalFruit(self, fruits):
        fruit_counter={}
        start=0
        longest=0
        for end in range(0,len(fruits)):
            end_fruit=fruits[end]
            fruit_counter[end_fruit]=fruit_counter.get(end_fruit,0)+1
            while len(fruit_counter)>2:
                start_fruit=fruits[start]
                fruit_counter[start_fruit]-=1
                if fruit_counter[start_fruit]==0:
                    del fruit_counter[start_fruit]
                start+=1
            longest=max(end-start+1,longest)
        return longest

        