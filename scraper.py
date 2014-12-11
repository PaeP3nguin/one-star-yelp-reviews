#!python2
from lxml import html
import requests
import sys

if len(sys.argv) >= 2:
    business_name = sys.argv[1]
else:
    business_name = 'super-h-mart-niles'

business_page = requests.get('http://www.yelp.com/biz/' + business_name)
business_tree = html.fromstring(business_page.text)

review_count = int(business_tree.xpath('//span[@itemprop="reviewCount"]/text()')[0])
offset = review_count//40 * 40;

page = requests.get('http://www.yelp.com/biz/' + business_name + '?start=' + str(offset) + '&sort_by=rating_desc')

tree = html.fromstring(page.text)

one_star_text = tree.xpath('//meta[@itemprop="ratingValue"][@content="1.0"]/../../../../p[@itemprop="description"]//text()')

print one_star_text
print offset