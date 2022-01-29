import feedparser
from weedly_bot.utils.youtube import YoutubService
yt = YoutubService()

url = 'https://www.youtube.com/c/moscowdjangoru'
yt_id = yt.extract_channel_id(url)
rss_link = f'https://www.youtube.com/feeds/videos.xml?channel_id={yt_id}'

feed = feedparser.parse(rss_link)
print(feed)
