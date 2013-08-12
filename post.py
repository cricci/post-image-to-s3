import urllib2
import settings

from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.bucket import Bucket

conn = S3Connection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)
bucket = Bucket(conn, settings.BUCKET)

image_file_object = urllib2.urlopen(settings.IMAGE_SRC)
k = Key(bucket)

k.key = settings.IMAGE_KEY
HEADER = {'Content-Type' : 'image/jpeg'}
k.set_contents_from_string(image_file_object.read(), HEADER)
k.make_public()

k.key = settings.RSS_KEY
HEADER = {'Content-Type' : 'application/rss+xml'}
k.set_contents_from_string(settings.RSS, HEADER)
k.make_public()
