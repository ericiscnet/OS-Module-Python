import os
# Create a directory names "aws"
directory_path = 'aws'
os.mkdir(directory_path)

# Create two files named "aws_restart" and "aws_copy"
file1_path = os.path.join(directory_path, "aws_restart.txt")
file2_path = os.path.join(directory_path, "aws_copy.txt")

# Create the files
with open(file1_path, 'w') as file1:
   file1.write(".........Here we find the contents of the file aws_restart.txt")

with open(file2_path, 'w') as file2:
    file2.write("........Now here we find the contents of the second file aws_copy.txt")

# Check files in directory
files_in_directory = os.listdir(directory_path)
print(f"The Files in '{directory_path}' directory we created:")
for file_name in files_in_directory:
    file_path = os.path.join(directory_path, file_name)
    print(file_name)

# Read contents of the files in the directory
with open(file1_path, 'r') as file:
    file_content = file.read()
    print(f"Our contents in {os.path.basename(file1_path)}:\n{file_content}")

with open(file2_path, 'r') as file:
    file_content = file.read()
    print(f"Our contents in {os.path.basename(file2_path)}:\n{file_content}")
