One-Star Yelp Reviews
======================
Python script to generate and post images captioned with text from a one-star Yelp review of that business/location. See the output at http://onestaryelp.tumblr.com/

### How does it work?
1. Go to Yelp and find a business, ex. Northwestern University
2. Copy the last part of the url after the "/biz/" ex. "northwestern-university-evanston-2"
3. Run scraper.py with that string as the first argument ex. "scraper.py northwestern-university-evanston-2"
4. The Python script goes the Yelp, finds the one star review with the highest "Funny" rating, using XPath searches
5. The script displays all of the sentences of the review, letting you select which ones to put on the image
6. The script performs a Google Image Search and grabs the first photo that's big enough
7. Using Python Imaging Library, it overlays the caption onto the image
8. Finally, the image is posted onto Tumblr!
