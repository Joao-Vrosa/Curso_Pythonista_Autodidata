import re

email = 'joao@gmail.com'

# Findall
result = re.findall(r"(@.{1,8}\.)", email)
print(result)

# Search
result = re.search(r"(@.{1,8}\.)", email)
print(result)

# Split
result = re.split(r"(@.{1,8}\.)", email)
print(result)

# Sub
result = re.sub(r"(@.{1,8}\.)", '@gmail', email)
print(result)
