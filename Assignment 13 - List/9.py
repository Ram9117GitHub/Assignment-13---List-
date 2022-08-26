"""Write a Python script to create a list of city names taken from the user"""
print("-------------------------------------------------------------------------------------------------")
print("How many numbers you want to enter :")
n = int(input())
print("Enter list number:")
List = []
i =0
while i < n:
    List.append(input())
    i+=1
print(List)
print("--------------------------------------------------------------------------------------------------------")
print("Enter list of city name :")
List = eval(input())
print(List)
print("---------------------------------------------------------------------------------------------------------")

"""""""""""""""Output"""""
"""-------------------------------------------------------------------------------------------------
How many numbers you want to enter :
2
Enter list number:
"bihar"
"raj"
['"bihar"', '"raj"']
--------------------------------------------------------------------------------------------------------
Enter list of city name :
["bihar","delhi","rajasthan"]
['bihar', 'delhi', 'rajasthan']
---------------------------------------------------------------------------------------------------------

Process finished with exit code 0
"""


