import random

dict = {"title" : ["프활1급", "프활2급"]}
dict_title = dict['title']

for iter in range(0, 5):
    title = random.choice(dict_title)
    print(title)