#2520
# class Solution(object):
#     def countDigits(self, num):
#         temp=num
#         ans=0
#         while temp>0:
#             r=temp%10
#             if num%r==0:
#                 ans+=1
#             temp//=10   
#         return ans    
                
#9
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        temp=x
        rev =0
        while temp>0:
            r=temp%10
            rev=rev*10+r
            temp//=10
        return rev==x       

