# import httpx
# import feedparser
#
# url = 'https://www.the-village.ru/api/spaces/4/rss.xml'
# url = 'https://meduza.io/rss/all'
# base = 'http://127.0.0.1:5000'
# rss = httpx.get(f'{base}/api/v1/feeds/?rss-only=1').json()
# rss = [e['url'] for e in rss]
#
# for url in rss:
#     for e in feedparser.parse(url)['entries']:
#         data =  {
#             "title": e['title'] ,
#             "url": e['link'],
#             "published": "2021-12-12 10:00:00",
#             "feed_id": 2,
#             "author_name": "дефолтный автор"
#
#         }
#         print('заг---',e['title'])
#         print('источник --- ', e['link'])
#         r = httpx.post('http://127.0.0.1:5000/api/v1/articles/', json=data)
#         print(r)
#
#
