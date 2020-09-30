from functools import partial
import hashlib

def get_multipart_etag_checksum(stream, chunk_size=8 * 1024 * 1024):
    """Gets the checksum according to the style of S3 ETags when doing
    multipart uploads. If there less than 2 chunks, then a normal md5
    checksum is calculated.

    :param stream: a file like object
    :param chunk_size: the chunk size
    :return: the calculated etag
    """

    func = partial(stream.read, chunk_size)
    md5s = [hashlib.md5(c) for c in iter(func, b"")]

    l = len(md5s)

    if l < 1:
        return hashlib.md5().hexdigest()
    elif l == 1:
        return md5s[0].hexdigest()

    m = hashlib.md5()
    for i, md5 in enumerate(md5s):
        m.update(md5.digest())

    return "{}-{}".format(m.hexdigest(), l)
