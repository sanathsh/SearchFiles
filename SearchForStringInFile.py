import sys


search_string = input("Enter File Search String : ")
Filename = input("Enter the Filename:")


# Open the file in read mode
with open(r'C:\Users\sanat\Python\SearchFile.py', 'r') as file:
  # Read each line in the file
  for line in file:
    # If the string is in the line, print it
    if 'python' in line:
      print(line)

print('test123')