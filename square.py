#Write a Python program to square the elements of a list using map() function.
#Sample List: [4, 5, 2, 9]
#Square the elements of the list:
#[16, 25, 4, 81]
def square_fnc(num):
    square= int(num) * int(num)
    return square
user_input = input('Enter the numbers : ').split(',')
result= map(square_fnc,user_input)
print('Square of all the elements of a list : ',list(result))



