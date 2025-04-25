text = input("Enter your text: ")
new_text = ""
for char in text:
    new_text = char + new_text   #last char becomes first

print(new_text)