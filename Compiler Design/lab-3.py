
user_input = input("Enter a string: ")

# first double quote (")
start_index = user_input.find('"')

# last double quote (")
end_index = user_input.rfind('"')

# Extract the substring within double quotes (")
if start_index != -1 and end_index != -1:
    string = user_input[start_index:end_index+1]
    print("The input contains string:", string)
else:
    print("The input doesn't contain any string!!!")

