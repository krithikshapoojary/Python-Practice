import re
text = "my age is 20"
result = re.search(r"\d",text)
print(result.group())