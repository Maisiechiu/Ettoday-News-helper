from bs4 import BeautifulSoup
import pandas as pd
import os 


def filter_keyword_csv(keyword):
    df = pd.read_csv('ettoday_news.tsv', delimiter='\t')
    filtered_df = df[df['tags'].str.contains(keyword, case=False, na=False)]
    temp = pd.concat([filtered_df['title'], filtered_df['tags']], axis=1) 
    temp = pd.concat([temp, filtered_df['publish_datetime']], axis=1) 
    temp = pd.concat([temp, filtered_df['content']], axis=1) 
    temp = temp.sort_values(by='publish_datetime')
    temp.to_csv('{}.csv'.format(keyword), index=False, encoding='utf-8-sig')


def read_keyword_csv_file(csv_file_path):
    csv_file = csv_file_path
    filtered_df= pd.read_csv(csv_file)
    filtered_df = pd.DataFrame(filtered_df)


    temp = pd.concat([filtered_df['title'], filtered_df['tags']], axis=1) 
    temp = pd.concat([temp, filtered_df['publish_datetime']], axis=1) 
    temp = pd.concat([temp, filtered_df['content']], axis=1) 
    filtered_df = temp.sort_values(by='publish_datetime')
    
    return filtered_df


def extract_plain_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.text



def extract_keyword_news(keyword):
    ##如果檔案存在, 就不用再爬一次
    print("過濾出所有{}事件的新聞".format(keyword))
    if os.path.exists("{}.csv".format(keyword)):
        filtered_df =  read_keyword_csv_file("{}.csv".format(keyword))
    else:
        filter_keyword_csv(keyword)
        filtered_df = read_keyword_csv_file("{}.csv".format(keyword))
    
    filtered_df['plain_text'] = filtered_df['content'].apply(extract_plain_text)
    
    print("過濾完成".format(keyword))
    print("=========================================")

    return filtered_df