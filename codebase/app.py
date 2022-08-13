from newsapi import NewsApiClient
from env_vars.env_vars import ENV_VARS
import time

# Init
ENVIRONMENT_VARIABLES = ENV_VARS()
newsapi = NewsApiClient(api_key=ENVIRONMENT_VARIABLES["NEWS_API"])

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='India', language='en', country='in')
print (top_headlines)
time.sleep(10)

# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin', sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com', from_param='2022-08-01', to='2022-08-12', language='en', sort_by='relevancy', page=2)
# print (all_articles)
# time.sleep(10)

# # /v2/top-headlines/sources
# sources = newsapi.get_sources()
# print (sources)
# time.sleep(10)
