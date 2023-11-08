
with open("artifact.txt","r") as f:
    text=f.read()

with open("artifact.txt","w") as f:
    text=f.write(text + " and updated.")

print(text)
print("it is a end of stage 3")

