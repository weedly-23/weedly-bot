import feedparser
import re
from pprint import pprint
import validators


def get_name_from_url(url):
    '''взяли из ура только название ресусра, чтобы написать юзеру, что на него подписались'''

    if 'www' in url:
        name =  re.findall(pattern='\.[a-z-]*\.', string= url)

        return name[0].strip('.')
    name = re.findall(pattern='[a-z]*\.', string= url)
    return name[0].strip('.')



def check_if_rss_is_working(url):
    '''пробуем парсить фид, если нет ошибки и есть статьи отдаем True'''
    feed = feedparser.parse(url)
    if feed['bozo']:
        print('ошибка подключени к rss')
        print(feed['bozo_exception'])
        return False

    if not feed['entries']:
        print('подключились к фиду, но в нем пусто')
        pprint(feed)
        return False

    return True


def check_if_valid_rss_url(url):
    '''Проверяем ок ли rss и добавляем в БД, если все ок'''
    url = url.strip()
    if not validators.url(url):
        return {'res': False,
                'msg': 'Неверный формат ссылки. Адрес должен быть таким -- https://meduza.io/rss/podcasts/tekst-nedeli'}

    elif not check_if_rss_is_working(url):
        return {'res': False,
                'msg':'Не удается подключиться к этому rss фиду. Проверьте правильность написания или попробуйте позже'}
    else:

        source_name = get_name_from_url(url)
        return  {'res': True,
                 'msg': f'Работает! Добавили {source_name} в подписки!. '
                        f'Через пару минут статьи появятся в разделе "Читать подписки"'}



