import json
from collections import OrderedDict
import json


json_list = []
json_open = open('output.json', 'r')
json_load = json.load(json_open)
count = 1
t = []
s = []
for i in range(len(json_load)):
    data = OrderedDict()
    j = json_load[i]['word']
    t.append(j)
    if len(j) <= 5:
        if t[i-1][0:2] != t[i][0:2]:
            s.append(t[i])
            # print(t[i-1][0:3],t[i][0:3])
            count += 1
            data["word"] = t[i]
            json_list.append(data)
# print(s)
print(count)

output_name = './modify.json'
with open(output_name, 'w') as file:
    json.dump(json_list, file, indent=4, ensure_ascii=False)
