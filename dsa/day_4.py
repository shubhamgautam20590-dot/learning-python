#1281
# class Solution(object):
#     def subtractProductAndSum(self, n):
#         temp =n
#         add =0
#         product=1
#         while temp>0:
#             r=temp%10
#             temp//=10
#             add+=r
#             product*=r
#         return product-add

#1431
# class Solution(object):
#     def kidsWithCandies(self, candies, extraCandies):
#         ans=[]
#         maxCandies=max(candies)
        
#         for i in candies:
#             if(i+extraCandies)>=maxCandies:
#                 ans.append(True)
#             else:
#                 ans.append(False)
#         return ans

