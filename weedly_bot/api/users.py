from typing import Optional

import httpx
from yarl import URL

import logging

logger = logging.getLogger(__name__)

class UserClient:

    def __init__(self, url: URL) -> None:
        self.url = url

    def add_user(self, uid, name):
        data = {"uid":uid, "name":name}

        url = self.url / 'api/v1/users/'
        try:
            req = httpx.post(str(url), json=data)#.json()
            req.raise_for_status()
            logger.debug(f'Добавили юзера {uid} в БД')
        except httpx.HTTPError as er:
            logger.warning(er)
            logger.warning(f'Видимо, юзер %s уже существует', uid)


    def subscrbe_user_to_rss(self, uid, feed_id):
        """добавить rss в подписки юзера"""
        data = {"feed_id": feed_id}
        url = self.url / 'api/v1/users/' / str(uid) / 'feeds'

        try:
            req = httpx.put(str(url), json=data)
            req.raise_for_status()
            logger.debug('обновленные подписки юзера --- ', req.json()['updated_feeds'])

        except httpx.HTTPError as er:
            logger.warning(er)


    def get_user_feeds(self, uid):
        '''[
            {
                "category": null,
                "is_rss": true,
                "name": "vc.ru",
                "uid": 4,
                "url": "https://vc.ru/rss?ref=vc.ru"
            },'''

        url = self.url / 'api/v1/users/' / str(uid) / 'feeds'

        try:
            req = httpx.get(str(url))
            req.raise_for_status()
            # print(req.json())
            # logger.debug('получили подписки юзера --- %s', str(req.json()))
            return req.json()

        except httpx.HTTPError as er:
            logger.warning(er)


