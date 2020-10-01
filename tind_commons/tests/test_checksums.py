import unittest
from io import BytesIO

from tind_commons.checksums import get_multipart_etag_checksum

try:
    from urllib.request import urlopen
    from urllib.error import URLError
except ImportError:
    from urllib2 import urlopen, URLError

class MultipartEtagChecksumTests(unittest.TestCase):
    def get_url(self, url):
        try:
            res = urlopen(url, timeout=5)
            return BytesIO(res.read())
        except URLError as err:
            self.fail(str(err.reason))

    def test_multipart_etag_checksum(self):
        url = "https://upload.wikimedia.org/wikipedia/commons/6/61/Korfu_%28GR%29%2C_Agii_Douli%2C_Olivenhain_--_2018_--_1284-8.jpg"
        data = self.get_url(url)

        res = get_multipart_etag_checksum(data)

        self.assertEqual(res, "d3484e041c154b2558683111ed02ca7e-4")

    def test_multipart_etag_checksum_regular_md5(self):
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/ET_Afar_asv2018-01_img58_Dallol.jpg/320px-ET_Afar_asv2018-01_img58_Dallol.jpg"
        data = self.get_url(url)

        res = get_multipart_etag_checksum(data)

        self.assertEqual(res, "4290b13b6643e63bfadfc65b16c11e91")
