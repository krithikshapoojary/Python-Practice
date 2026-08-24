import re
text="python123"
result=re.search(r"\w+",text)
print(result.group())