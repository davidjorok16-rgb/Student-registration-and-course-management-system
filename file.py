# file= open("note.txt", "w")
# file.write("Today is a good day.\n ")
# file.write("The enemy has been defeated.\n")
# file.write("Peace has been restored to our lands.\n")
# file.write("Go and secure your lands.\n")
# file.close()

# file= open("note.txt", "r")
# content= file.read()
# print(content)
# file.close()

# file= open("note.txt", "a")
# file.write("\n I am tired of destruction of lives.")
# file.close()

# file= open("note.txt", "w")
# file.write("The cat is out of the bag.")
# file.close()

try:
    file= open("WEB.txt", "r")
    content= file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("FileNotFoundError. File does not exist.")
