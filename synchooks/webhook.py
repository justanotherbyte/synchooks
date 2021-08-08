import requests

from typing import Optional, List

from .embed import Embed

class Webhook:
    def __init__(
        self,
        url: str,
        *,
        session: Optional[requests.Session] = None
    ):
        self.session = session or requests.Session()
        self.url = url

    
    def send(self, content = None, *, embed: Optional[Embed] = None, embeds: Optional[List[Embed]] = None) -> requests.Response:
        content = str(content)
        if embeds is not None and len(embeds) == 1:
            embed = embeds[0]
            embeds = None
        
        embed_data = []
        if embed and not embeds:
            embed_data = [embed]
        elif embeds and not embed:
            embed_data = embeds
        elif not embed and not embeds:
            pass
        else:
            raise ValueError("embed and embeds cannot both be passed")

        embed_data = [e.to_dict() for e in embed_data]
        
        payload = {
            "content": content,
            "embeds": embed_data
        }
        resp = self.session.post(self.url, json = payload)
        return resp

        