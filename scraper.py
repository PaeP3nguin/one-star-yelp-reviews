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

one_star_reviews = tree.xpath('//meta[@itemprop="ratingValue"][@content="1.0"]/../../../../..')

highest_rating_sum = -1
funniest_rating = -1
review_rating_pairs = []
for review_wrapper in one_star_reviews:
    review_text = ' '.join(review_wrapper.xpath('div//p[@itemprop="description"]/text()'))
    review_ratings = review_wrapper.xpath('*//span[@class="count"]//text()')
    funny_rating = int(review_wrapper.xpath('*//span[@class="i-wrap ig-wrap-common i-ufc-funny-common-wrap button-content"]/span[@class="count"]//text()')[0])
    rating_sum = sum(map(int, review_ratings))
    
    review_rating_pair = [review_text, rating_sum]
    review_rating_pairs.append(review_rating_pair)
    if rating_sum > highest_rating_sum:
        highest_rated_review = review_rating_pair
        highest_rating_sum = rating_sum
        
    if funny_rating > funniest_rating:
        funniest_review = review_rating_pair
        funniest_rating = funny_rating

print highest_rated_review
print offset