import pandas as pd
with open('./data/train.jsonl') as f:
    data=f.read()
data=data.split('\n')
dic={}
for i in data:
    temp_dic=eval(i)
    for j in temp_dic.keys():
        if j not in dic.keys():
            dic[j]=[temp_dic[j]]
        else:
            dic[j].append(temp_dic[j])
df=pd.DataFrame.from_dict(dic)
df.to_csv("train_data.csv")
