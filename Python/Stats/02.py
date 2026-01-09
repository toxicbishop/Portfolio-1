text = "hello world"
print(text.upper())
print(text.title())


text="Hello World"
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#split & joining substring
text = "apple,banana,cherry"
fruits=text.split(",")
print(fruits)

new_text=" and ".join(fruits)
print(new_text)
#Regular Expression
#Search
import re
text="My email is eg@example.com"
match=re.search(r"\S+@\S+",text)
if match:
    print("Found email:",match.group())
else:
    print("Not Found")


text="Contact us at support@example.com or sales@example.com"
emails=re.findall(r"\S+@\S+",text)
print("Found email:",emails)
                  


text='My phone number is 123-456-7890'
new_text=re.sub(r"\d{3}-\d{3}-\d{4}","XXX-XXX-XXXX",text)
print(new_text)



#validating
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern,email) is not None
print(is_valid_email("test@eg.com"))
print(is_valid_email("invalid-email"))


#Output:
#HELLO WORLD
#Hello World
#Hello World
#Hello World
#Hello World

#['apple', 'banana', 'cherry']
#apple and banana and cherry

#Found email: eg@example.com
#Found email: ['support@example.com', 'sales@example.com']
#My phone number is XXX-XXX-XXXX
#True
#False