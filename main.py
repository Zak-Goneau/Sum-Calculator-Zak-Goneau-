#Introduction
print ("This program will calculate the sum of all integers up to the integer you input")

#ask user for positive integer
user_int = int(input("Please enter a positive integer: "))

#Initialize counter for integers
int_counter = 1

#calculates sum for all integers until user integer
sum = 0
while sum < user_int:
  sum + int_counter
  int_counter + 1

#state the sum
print ("The sum is " + format(sum))