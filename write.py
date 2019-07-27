# 'w' (for write) it writes the word in the file and overrides old words
f = open('newfile.txt', 'a')
# 'a' (for append) means append and it appends the word to the end (does not override earlier words)
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
text = '\n'.join(lines) #adds a new line after each word, \t \n
f.writelines(text)
f.close()
