from dataclasses import dataclass


@dataclass
class TDocument:
    Url: str
    PubDate: int
    FetchTime: int
    Text: str
    FirstFetchTime: int | None

    def pk(self):
        return self.Url
