import urllib.request
import json
from .models import Sources, Articles
api_url = None

api_key = None
base_url = None


# def configure_request(app):
#     global api_key, base_url, api_url


def configure_request(app):
    global api_key, base_url, api_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    api_url = app.config['NEWS_API_ARTICLES']


article_base_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'


def get_news():

    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        sources_results = None

        if get_news_response['sources']:
            sources_results_list = get_news_response['sources']
            sources_results = process_results1(sources_results_list)

    return sources_results


def process_results1(sources_list):

    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        news_object = Sources(id, name, description, url, category)
        sources_results.append(news_object)

    return sources_results


def get_articles(id):

    get_news_url = article_base_url.format(id, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        articles_results = None

        if get_news_response['articles']:
            articles_results_list = get_news_response['articles']
            articles_results = process_results(articles_results_list)

    return articles_results


def process_results(articles_list):

    articles_results = []

    for articles_item in articles_list:
        name = articles_item.get('name')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        article_object = Articles(
            name, author, title, description, url, urlToImage)
        articles_results.append(article_object)

    return articles_results
