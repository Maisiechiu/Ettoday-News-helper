import pandas as pd
import json
from collections import Counter

# 指定你的TSV文件的路径
tsv_file_path = "meichuhackathon2023\meichuhackathon2023\log_20230701_000000.tsv"

# 使用read_csv函数读取TSV文件，指定分隔符为制表符（'\t'）
df = pd.read_csv(tsv_file_path, sep='\t')

# 有多少不同的category_id
df['session_id'].unique().__len__()

#取出特定的session_id(代表特定的User)
df2 = df[df['session_id'] == '094d756da2f99fe5f103a20f598bda02']


category_list = []
for i in range(len(df2)):
    if df2['page'].iloc[i] != '{}':
        try:
            temp = df2['page'].iloc[i]
            temp = json.loads(temp)
            if (temp['item']['category_id_list'] != '新聞頁') &(temp['item']['category_id_list'] != 'null'):
                # print(temp['item']['category_id_list'].split('_')[0])
                category_list.append(int(temp['item']['category_id_list'].split('_')[0]))
        except:
            pass

# 使用 Counter 统计元素出现次数
element_counts = Counter(category_list)

# 按出现次数从高到低进行排序
sorted_counts = sorted(element_counts.items(), key=lambda x: x[1], reverse=True)

# 打印按出现次数排序后的结果
for item, count in sorted_counts:
    print(f"{item}: {count}")