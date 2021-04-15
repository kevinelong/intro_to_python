"""
5 Famous wesites

amazon shopping
ebay auctions
google search
microdoft office365
facebook social
youtube watch

eBay Inc. (/ˈiːbeɪ/ EE-bay) is an American multinational e-commerce corporation based in San Jose,
California,
that facilitates consumer-to-consumer and business-to-consumer sales through its website.

eBay was founded by Pierre Omidyar in 1995, and became a notable success story of the dot-com bubble.
eBay is a multibillion-dollar business with operations in about 32 countries, as of 2019.[1][2]

The company manages the eBay website, an online


    auction and shopping website in which people and businesses
    buy and sell a wide variety of goods and services worldwide.

    The website is free to use for buyers,
    but sellers are charged fees for listing items
    after a limited number of free listings,
    and again when those items are sold.[3]

NOUNS (People places things) Site, Buyer, Seller, User, Listing (auction item) -> Classes
ADJ (Attributes know/have) sold, fee -> attributes/properties
VERB (Action words (what does it do?)) Buy, Sell, List, Use (Browse) -> functions/methods

IS_A buyer is a user, seller is a user -> inheritance
HAS_A site has users, seller has listings, buyer has bids -> composition
"""


class Site:
    def __init__(self):
        self.users = []


class User:
    def __init__(self, email):
        self.email = email
        self.bids = []
        self.purchases = []
        self.listings = []


class Listing:
    fee_percent = 0.1

    def __init__(self, seller, name, price,
                 photo_url="", description="",
                 starting_price=0,
                 start_date_time=None,
                 end_date_time=None,
                 buy_it_now_enabled=False
                 ):
        self.seller = seller
        self.name = name
        self.price = price
        self.photo_url = photo_url
        self.description = description
        self.buy_it_now_enabled = buy_it_now_enabled
        self.sold = False
        self.starting_price = starting_price
        self.final_price = None
        self.fee = self.fee_percent * price
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time

    def buy(self, buyer):
        self.sold = True
        buyer.purchases.append(self)


u = User("kevin@example.com")
u2 = User("nina@example.com")
listing = Listing(u, "comic book x-men #1", 1000.00)
listing.buy(u2)
