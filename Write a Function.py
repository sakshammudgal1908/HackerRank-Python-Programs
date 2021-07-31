'''Sample Input 0

1990
Sample Output 0

False
'''
#code
def is_leap(year):
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    else:
        return False
year = int(input())
print(is_leap(year))
