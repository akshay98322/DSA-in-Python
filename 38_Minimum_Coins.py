class Solution:
    def findMin(self, n: int) -> int:
       # code here 
       coins = 0
       denominations = [1, 2, 5, 10]
       
       for d in reversed(denominations):
           coins += (n // d)
           n %= d
       return coins
               
            
# Example usage:
solution = Solution()
min_coins = solution.findMin(28)
print(f"Minimum coins required: {min_coins}")