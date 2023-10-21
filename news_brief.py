import requests

def call_gpt_one_news(news):
    API_KEY = "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"

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        },
        json={
            'model': 'gpt-4',
            'messages': [{"role": "user", "content": "幫我總結以下文字內容到100字: {}".format(news)}],
        }
    )
    response = response.json()
    print(response)
    response = response['choices'][0]['message']['content']
    return response

def call_gpt_all_news(topic , news):
    API_KEY = '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'

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        },
        json={
            'model': 'gpt-4',
            'messages': [{"role": "user", "content": "{}\n , 以上是{}事件新聞請以四個問答式總結重點 ".format(topic, news)}],
        }
    )
    print(response)
    response = response.json()
    response = response['choices'][0]['message']['content']
    
    return response

def call_gpt_give_summarize(topic , news):
    API_KEY = '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'

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        },
        json={
            'model': 'gpt-4',
            'messages': [{"role": "user", "content": "{}\n , 根據上面的內容30字說明什麼是{}事件 ".format(topic, news)}],
        }
    )
    
    print(response)
    response = response.json()
    response = response['choices'][0]['message']['content']
    
    return response



def news_brief(news_data):
    content = ""
    for i in range(0, len(news_data)):
        news_content = news_data['plain_text'][i]
        print("=========================================")
        content +="第{}篇新聞".format(i)+call_gpt_one_news( news_content)

    
    print("問：什麼是以巴衝突")
    print(call_gpt_give_summarize("以巴衝突" ,content))
    print(call_gpt_all_news("以巴衝突" ,content))

