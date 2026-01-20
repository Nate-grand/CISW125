# nathan macbeth
# 20/1/26
# Files Lab

for i in range(5):
    filename = f"file_lab_output_{i+1}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is file number {i+1}\n")
        file.write("Nathan Macbeth\n")
        file.write("CISW125 - Files Lab\n")
        file.write("Date: 20/1/26\n")