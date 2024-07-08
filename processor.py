from db import DB
from tdocument import TDocument


class Processor:
    """Required Processor"""

    def __init__(self):
        self.db = DB()

    def Process(self, doc: TDocument) -> tuple[TDocument | None, str | None]:
        """Processes the document

        Args:
            doc (TDocument): input document

        Returns:
            tuple[TDocument | None, str | None]: output document and error
        """
        if not doc.Url or doc.FetchTime == 0:
            return None, "Invalid input document"

        existing = self.db.select(doc.Url)
        if existing is None:
            doc.FirstFetchTime = doc.FetchTime
            self.db.insert(doc)
        else:
            if doc.FetchTime < existing.FirstFetchTime:
                doc.FirstFetchTime = doc.FetchTime
            else:
                doc.FirstFetchTime = existing.FirstFetchTime
                doc.PubDate = existing.PubDate
            if doc.FetchTime < existing.FetchTime:
                doc.FetchTime = existing.FetchTime
                doc.Text = existing.Text
            self.db.update(doc)

        return doc, None
