handle = open("req.txt", "r")

# ctrl+/
# handle.read() -> """
#                 Hello
#                 I'm here """

for line in handle.readlines():
    line = line.strip() 
    print(line)
    
handle.close()