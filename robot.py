import sys
import urllib.request
from typing import Optional

class Robot:
    def __init__(self, url: str):
        self.url: str = url
        self.dict_headers: dict[str, str] = {}
        self.request: Optional[urllib.request.urlopen] = None

    def retrieve(self) -> None:
        self.request = urllib.request.urlopen(self.url)

    def headers(self) -> None:
        if self.request is None:
            self.retrieve()

        self.dict_headers = dict(self.request.getheaders())

    def show(self) -> None:
        print(f"Headers for {self.url}:")
        for k,v in self.dict_headers.items():
            print(f"{k}: {v}")