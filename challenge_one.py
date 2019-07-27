# The w+ file mode truncates the file to 0 bytes, but allows you to
# write and then read the data that you have written.
# The following example opens a file called myfile.txt. If it doesn't exist,
# the file will be created. If it does exist, then its contents will be truncated
# to 0 bytes - essentially, the file will be completely overwritten.
# We write 'Hello, World' and a new line, and then move the file cursor to the
# beginning of the file to read what we just wrote.

with open('myfile.txt', 'w+') as f:
    f.write('Hello, World\n')
    f.seek(0)
    data = f.read()
