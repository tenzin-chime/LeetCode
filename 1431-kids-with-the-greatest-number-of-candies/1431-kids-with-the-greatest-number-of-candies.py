class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp=0
        output=[]
        maxCandy = max(candies)

        for candy in candies:
            temp=candy + extraCandies
            if temp >= maxCandy:
                output.append(True)
            else:
                output.append(False)

        return output
