import datetime

AWS_ACCESS_KEY = 'Your-AWS-Access-Key-Here'
AWS_SECRET_KEY = 'Your-AWS-Secret-Key-Here'

BUCKET    = 'Your-Bucket'
IMAGE_SRC = 'http://192.168.1.200/snapshot.jpg'
IMAGE_KEY = 'livecam/snapshot.jpg'
IMAGE_STR = 'https://s3.amazonaws.com/' + BUCKET + '/' + IMAGE_KEY
RSS_KEY   = 'livecam/snapshot.rss.xml'

RSS  = '<?xml version="1.0" encoding="UTF-8"?>\n' + \
       '<rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/">\n' + \
       ' <channel>\n' + \
       '  <title>Your Title</title>\n' +  \
       '  <link>' + IMAGE_STR + '</link>\n' + \
       '  <description>Your Description</description>\n' + \
       '  <ttl>5</ttl>\n' + \
       '  <item>\n' + \
       '   <title>Your Alt Title</title>\n' + \
       '   <link>http://www.your-link.com/</link>\n' + \
       '   <category>livecam</category>\n' + \
       '   <description>&lt;img src=&quot;' + IMAGE_STR + '&quot;&gt;</description>\n' + \
       '   <pubDate>' + datetime.datetime.now().strftime("%a, %d %b %Y %H:%M -06:00") + '</pubDate>\n' + \
       '   <guid isPermalink="true">' + IMAGE_STR + '</guid>\n' + \
       '   <media:content url="' + IMAGE_STR + '" type="image/jpeg" height="1280" width="720" duration="5" />\n' + \
       '   <media:thumbnail url="' + IMAGE_STR + '" type="image/jpeg" height="1280" width="720" duration="5" />\n' + \
       '   <enclosure url="' + IMAGE_STR + '" type="image/jpeg" />\n' + \
       '  </item>\n' + \
       ' </channel>\n' + \
       '</rss>'
