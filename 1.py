# def linearSearch(arr,x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
        
#     return -1


# arr = [20,45,47,55,67,75,88,90]
# print("this is your index no", linearSearch(arr,55))
#time complexity 0(n)
#space complexity constant



# def Binary_Search(arr,x,left,right):
#     if arr[mid] == x:
#         return arr[mid]
#     elif arr[mid] < x:
#         Binary_Search(arr,4,7)
#     elif arr[mid] > x :
#         Binary_Search(arr,2,0)
#     else :
#         return -1
    
# arr = [20,30,40,50,60,70,80,90]
# mid = 3
# x = 50
# print(Binary_Search(arr,0,7))



#Binary Search Algorithm


# def BinarySearch(arr,x,i,j):
#     while i <= j :
#         mid = i+(j-i)//2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x :
#             return BinarySearch(arr,x,mid+1,j)
#         else :
#             return BinarySearch(arr,x,i, mid-1)
#     return -1

   
        


# arr = [20,30,40,50,60,70,80,90]
# x = 30
# i = 0
# j = len(arr)-1
# result = BinarySearch(arr,x,i,j)
# print(result)



# def twopointerApproach(arr,x):
#     l = 0
#     r = len(arr)-1
#     while l<=r:
#         if arr[l]+arr[r] == x:
#             return (l,r)
#         elif arr[l]+arr[r] > x:
#             r = r-1
#         else:
#             l = l+1

# arr = [20,40,60,80,90,120,240]
# result = twopointerApproach(arr,210)
# print(result)


#time complexity o(n)



#Time complexity O(n)

# def findmaxProfit(price):
#     minPrice = float('inf')
#     maxProfit = 0
#     for i in range(len(price)):
#         if price[i] < minPrice:
#             minPrice = price[i]
#         elif price[i] - minPrice > maxProfit:
#             maxProfit = price[i] - minPrice
#     return maxProfit


# price = [7,4,5,3,6,16]
# maxProfit_Value = findmaxProfit(price)
# print('The Maximum profit of buying and selling the stock is:', maxProfit_Value)



#2 Dimensional Arrays
#Search in 2d arrays
#time complexity O(log(m*n))

# def search2DArray(arr, target):
#     m = len(arr)
#     if m == 0:
#         return False
#     n = len(arr[0])
#     left,right = 0, m*n-1

#     while left <= right :
#         mid = left + (right-left)//2
#         mid_element = arr[mid//n] [mid%n]
#         if target == mid_element:
#             return True
#         elif target < mid_element:
#             right = mid - 1
#         else:
#             left = mid + 1

#     return False




# arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 23
# result = search2DArray(arr, target)
# print(result)


























