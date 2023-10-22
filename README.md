# Ettoday-News-helper
For 梅竹黑客松, Topic:Ettoday, Group:積少成多多綠    
This is AI tool that can help to produce news brief and recommend news to user
# Demo
![image](https://github.com/Maisiechiu/Ettoday-News-helper/blob/master/demo.gif)

We want to use large language model to complete the following function
1. News content parser
2. News parser
3. Image and text similarity compare


# How to use?
## get the txt file of news brief
1. First you need to replace your openai api key at news_brief.py
run main.py
````
main.py --keyword {replace your keyword here}
````

## get the similarity between texts and images

```
cd Transformer-MM-Explainability
python main.py
```

# Reference    
[1] Sparks of Artificial General Intelligence: Early experiments with GPT-4    
[2] Learning Transferable Visual Models From Natural Language Supervision
