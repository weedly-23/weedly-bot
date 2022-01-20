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
        data = {"uid":uid, "feed_id":feed_id}
        url = self.url / 'api/v1/users/' / str(uid)
        try:
            req = httpx.put(str(url), json=data, follow_redirects=True)
            req.raise_for_status()
            logger.debug('добавили юзеру %s в подписки %s', uid, feed_id)

        except httpx.HTTPError as er:
            logger.warning(er)


    def get_user_feeds(self, uid):
        url = ''