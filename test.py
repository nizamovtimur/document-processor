import unittest

from tdocument import TDocument
from processor import Processor


class TestProcessor(unittest.TestCase):
    """Processor testing"""

    p = Processor()

    def test_processor(self):

        url_doc1 = "https://example.com/doc1"

        res, err = self.p.Process(
            TDocument(
                Url=url_doc1,
                PubDate=10,
                FetchTime=1,
                Text="Doc1 ver1",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc1
        assert res.PubDate == 10
        assert res.FetchTime == 1
        assert res.Text == "Doc1 ver1"
        assert res.FirstFetchTime == 1

        res, err = self.p.Process(
            TDocument(
                Url=url_doc1,
                PubDate=20,
                FetchTime=2,
                Text="Doc1 ver2",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc1
        assert res.PubDate == 10
        assert res.FetchTime == 2
        assert res.Text == "Doc1 ver2"
        assert res.FirstFetchTime == 1

        res, err = self.p.Process(
            TDocument(
                Url=url_doc1,
                PubDate=30,
                FetchTime=3,
                Text="Doc1 ver3",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc1
        assert res.PubDate == 10
        assert res.FetchTime == 3
        assert res.Text == "Doc1 ver3"
        assert res.FirstFetchTime == 1

        url_doc2 = "https://example.com/doc2"

        res, err = self.p.Process(
            TDocument(
                Url=url_doc2,
                PubDate=20,
                FetchTime=2,
                Text="Doc2 ver2",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc2
        assert res.PubDate == 20
        assert res.FetchTime == 2
        assert res.Text == "Doc2 ver2"
        assert res.FirstFetchTime == 2

        res, err = self.p.Process(
            TDocument(
                Url=url_doc2,
                PubDate=30,
                FetchTime=3,
                Text="Doc2 ver3",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc2
        assert res.PubDate == 20
        assert res.FetchTime == 3
        assert res.Text == "Doc2 ver3"
        assert res.FirstFetchTime == 2

        res, err = self.p.Process(
            TDocument(
                Url=url_doc2,
                PubDate=10,
                FetchTime=1,
                Text="Doc2 ver1",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc2
        assert res.PubDate == 10
        assert res.FetchTime == 3
        assert res.Text == "Doc2 ver3"
        assert res.FirstFetchTime == 1

        url_doc3 = "https://example.com/doc3"

        res, err = self.p.Process(
            TDocument(
                Url=url_doc3,
                PubDate=30,
                FetchTime=3,
                Text="Doc3 ver3",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc3
        assert res.PubDate == 30
        assert res.FetchTime == 3
        assert res.Text == "Doc3 ver3"
        assert res.FirstFetchTime == 3

        res, err = self.p.Process(
            TDocument(
                Url=url_doc3,
                PubDate=10,
                FetchTime=1,
                Text="Doc3 ver1",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc3
        assert res.PubDate == 10
        assert res.FetchTime == 3
        assert res.Text == "Doc3 ver3"
        assert res.FirstFetchTime == 1

        res, err = self.p.Process(
            TDocument(
                Url=url_doc3,
                PubDate=20,
                FetchTime=2,
                Text="Doc3 ver2",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc3
        assert res.PubDate == 10
        assert res.FetchTime == 3
        assert res.Text == "Doc3 ver3"
        assert res.FirstFetchTime == 1

        url_doc4 = "https://example.com/doc4"

        res, err = self.p.Process(
            TDocument(
                Url=url_doc4,
                PubDate=30,
                FetchTime=3,
                Text="Doc4 ver3",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc4
        assert res.PubDate == 30
        assert res.FetchTime == 3
        assert res.Text == "Doc4 ver3"
        assert res.FirstFetchTime == 3

        res, err = self.p.Process(
            TDocument(
                Url=url_doc4,
                PubDate=20,
                FetchTime=2,
                Text="Doc4 ver2",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc4
        assert res.PubDate == 20
        assert res.FetchTime == 3
        assert res.Text == "Doc4 ver3"
        assert res.FirstFetchTime == 2

        res, err = self.p.Process(
            TDocument(
                Url=url_doc4,
                PubDate=10,
                FetchTime=1,
                Text="Doc4 ver1",
                FirstFetchTime=None,
            )
        )
        assert res is not None
        assert res.Url == url_doc4
        assert res.PubDate == 10
        assert res.FetchTime == 3
        assert res.Text == "Doc4 ver3"
        assert res.FirstFetchTime == 1


if __name__ == "__main__":
    unittest.main()
