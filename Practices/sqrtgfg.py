# import math as m

# print(m.floor(m.sqrt(5)))

# class Solution:
#     q=10**9+7
#     def power(self,N,R):
#        if R<=0:
#            return 1
#        return (N**(R&1)*self.power(N,R>>1)**2)%self.q

# import math as m

# class Solution:
#     def checkTriplet(self,arr, n):
#         arr.sort()
#         for i in range(n-2):
#             for j in range(i+1,n-1):
#                 if m.sqrt(arr[i]*arr[i] + arr[j]*arr[j]) in arr[j+1:]:
#                     return 'True'
#         return False


N = int(input())
for i in range(N):
    print(" " * (N - i - 1) + "*" * (i + 1))
for j in range(N - 1):
    print(" " * (i + 1) + "*" * (N - i - 1))
