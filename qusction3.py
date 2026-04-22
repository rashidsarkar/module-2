import string
with open('./sample_data/data.txt','r') as file:
    content = file.readlines()
    # content = list(map(str.strip,content))
    newContent = " ".join(content)
    newContent = newContent.lower()
    newContent = newContent.translate(str.maketrans('','',string.punctuation))
    newContent = newContent.split()
    result = max(set(newContent),key=newContent.count)
    print(result)