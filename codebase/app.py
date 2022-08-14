from env_vars.env_vars import ENV_VARS
from newsapi import NewsApiClient
from textblob import TextBlob
# import time

ENVIRONMENT_VARIABLES = ENV_VARS()
newsapi = NewsApiClient(api_key=ENVIRONMENT_VARIABLES["NEWS_API"])

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(language='en', sources='reuters,associated-press')
print('Status\t\t:\t', top_headlines['status'])
print('Result count\t:\t', top_headlines['totalResults'])
for article in top_headlines['articles']:
    print('------------------------------------------------------------------')
    print('Source\t\t:\t', article['source']['name'])
    print('Description\t:\t', article['title'])
    description = article['title']
    blob = TextBlob(description)
    # print(blob.tags)
    print(blob.noun_phrases)
    for sentence in blob.sentences:
        print(sentence.sentiment)