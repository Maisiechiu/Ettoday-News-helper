import requests

def call_gpt_one_news(API_KEY , news):
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        },
        json={
            'model': 'gpt-4',
            'messages': [{"role": "user", "content": "幫我以繁體中文總結以下文字內容到100字: {}".format(news)}],
        }
    )
    response = response.json()
    #print(response)
    response = response['choices'][0]['message']['content']
    return response

def call_gpt_all_news(API_KEY , topic , news):

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        },
        json={
            'model': 'gpt-4',
            'messages': [{"role": "user", "content": "{}\n , 以上是{}事件新聞，請產生四個問題，並回答那四個問題，以總結重點 ".format(news,topic )}],
        }
    )
    #print(response)
    response = response.json()
    response = response['choices'][0]['message']['content']
    
    return response

def call_gpt_give_summarize(API_KEY , topic , news):

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        },
        json={
            'model': 'gpt-4',
            'messages': [{"role": "user", "content": "{}\n , 以上是{}事件新聞，根據上面的內容以30字繁體中文總結這個事件 ".format(news, topic)}],
        }
    )
    
    #print(response)
    response = response.json()
    response = response['choices'][0]['message']['content']
    
    return response



def news_brief(keyword , news_data):
    content = ""
    APIKey = "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"
    with open('{}.txt'.format(keyword), 'w') as f:

        for i in range(0, 5):
            news_content = news_data['plain_text'][i]
            temp_news_summarize = "第{}篇新聞:{}".format(i+1 , call_gpt_one_news(APIKey , news_content))
            print(temp_news_summarize)
            f.write("{}\n".format(temp_news_summarize))
            print("=========================================")
            content +=temp_news_summarize
            
        print("問：什麼是{}".format(keyword))
        f.write("問：什麼是{}\n".format(keyword))
        
        first_summarize = call_gpt_give_summarize(APIKey, keyword ,content)
        print(first_summarize)
        f.write("{}\n".format(first_summarize))

        all_summarize = call_gpt_all_news(APIKey, keyword ,content)
        print(all_summarize)
        f.write("{}\n".format(all_summarize))
