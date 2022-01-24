from typing import Optional

import httpx
from yarl import URL

import logging

class UserClient:

    def __init__(self, url: URL) -> None:
        self.url = url

    def add_user(self, uid, name):
        data = {"uid":uid, "name":name}

        url = self.url / 'api/v1/users/'
        try:
            req = httpx.post(str(url), json=data)#.json()
            req.raise_for_status()
            logging.debug(f'Добавили юзера {uid} в БД')
        except httpx.HTTPError as er:
            logging.warning(er)
            logging.warning(f'Видимо, юзер %s уже существует', uid)


    def subscrbe_user_to_rss(self, uid, feed_id):
        """добавить rss в подписки юзера"""
        logging.debug('подисываем юзера на фид %s %s', uid, feed_id)

        logging.warning('подисываем юзера %s на фид %s', uid, feed_id )
        data = {"feed_id": feed_id}
        url = self.url / 'api/v1/users/' / str(uid) / 'feeds/'

        try:
            req = httpx.post(str(url), json=data, follow_redirects=True)
            logging.debug('обновленные подписки юзера --- %s', req.json()['updated_feeds'])
            req.raise_for_status()

        except httpx.HTTPError as er:
            logging.warning(er)


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
            req = httpx.get(str(url), follow_redirects=True)
            logging.debug('получили фиды от юзера --- %s', req.json())

            req.raise_for_status()

            return req.json()

        except httpx.HTTPError as er:
            logger.warning(er)


