with open("/workspaces/gcse-24-27-vigdissanmark/File Handling/practiceRead.txt", "r") as file:
    content = file.read()
    print(content)

with open("/workspaces/gcse-24-27-vigdissanmark/File Handling/practiceRead.txt", "a") as file:
    file.write("\nThis is a new line")