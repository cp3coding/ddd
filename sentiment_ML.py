'''
Sentiment of a newspaper article
'''


from textblob import TextBlob
import nltk
from newspaper import Article

url = 'https://www.poynter.org/tech-tools/2017/text-only-news-sites-are-slowly-making-a-comeback-heres-why/'
article =Article(url)

article.download()
article.parse()
nltk.download('punkt')
article.nlp()

text = article.text

print(text)

obj = TextBlob(text)

sentiment =obj.sentiment.polarity

print(sentiment)

