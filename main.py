import news_parser
import news_brief
import argparse

def args_func():
    parser = argparse.ArgumentParser()
    parser.add_argument('--keyword', type=str, help='keyword', default='登革熱')
    args = parser.parse_args()
    return args

def main(keyword):
    news_data = news_parser.extract_keyword_news(keyword)
    news_brief.news_brief(keyword,news_data)

if __name__ == "__main__":
    args = args_func()
    keyword = args.keyword
    main(keyword)