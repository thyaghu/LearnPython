num_list=[0,1,2,3,4,5,6,7,8,9]
print(num_list[0])
#Negative index start the other way. Negative index of 9 is -1
print(num_list[-1])
#list[start:end:step], the end index is not inclusive
print(num_list[0:6])
#to print upto the last value of the list do not give the end index
print(num_list[1:])
#Step function skips the character. Below is to print even numbers
print(num_list[::2])
#Using negative index to reverse the list
print(num_list[::-1])
