f = open('files/relative_data.txt', 'r') # Relative path
# f = open('D:/Desktop/codeInst/Python/file_io/files/relative_data.txt', 'r') # absolute path

# lines = f.readlines() Will print it on one line with the \n after each line

lines = f.read()
f.close()
print(lines)
