
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from instapy import InstaPy
from instapy import smart_run
insta_username = 'jaincrystal18'
insta_password = 'hello@13'
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False).login()
with smart_run(session):
    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_do_follow(True, percentage=20)
    session.set_do_comment(True, percentage=30)
    hashtags = ['travelcouples', 'travelcommunity', 'passionpassport',
                'travelingcouple',
                'backpackerlife', 'travelguide', 'travelbloggers',
                'travelblog', 'letsgoeverywhere',
                'travelislife', 'stayandwander', 'beautifuldestinations',
                'moodygrams',
                'ourplanetdaily', 'travelyoga', 'travelgram', 'sunsetporn',
                'lonelyplanet',
                'igtravel', 'instapassport', 'travelling', 'instatraveling',
                'travelingram',
                'mytravelgram', 'skyporn', 'traveler', 'sunrise',
                'sunsetlovers', 'travelblog',
                'sunset_pics', 'visiting', 'ilovetravel',
                'photographyoftheday', 'sunsetphotography',
                'explorenature', 'landscapeporn', 'exploring_shotz',
                'landscapehunter', 'colors_of_day',
                'earthfocus', 'ig_shotz', 'ig_nature', 'discoverearth',
                'thegreatoutdoors']
my_hashtags = hashtags[:10]
session.set_comments([
    u'What an amazing shot! :heart_eyes: What do '
    u'you think of my recent shot?',
    u'What an amazing shot! :heart_eyes: I think '
    u'you might also like mine. :wink:',
    u'Wonderful!! :heart_eyes: Would be awesome if '
    u'you would checkout my photos as well!',
    u'Wonderful!! :heart_eyes: I would be honored '
    u'if you would checkout my images and tell me '
    u'what you think. :wink:',
    u'This is awesome!! :heart_eyes: Any feedback '
    u'for my photos? :wink:',
    u'This is awesome!! :heart_eyes:  maybe you '
    u'like my photos, too? :wink:',
    u'I really like the way you captured this. I '
    u'bet you like my photos, too :wink:',
    u'I really like the way you captured this. If '
    u'you have time, check out my photos, too. I '
    u'bet you will like them. :wink:',
    u'Great capture!! :smiley: Any feedback for my '
    u'recent shot? :wink:',
    u'Great capture!! :smiley: :thumbsup: What do '
    u'you think of my recent photo?'],
    media='Photo')
session.set_quota_supervisor(enabled=True,
                             sleep_after=[
                                 "likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                             sleepyhead=True,
                             stochastic_flow=True,
                             notify_me=True,
                             peak_likes_hourly=2,
                             peak_likes_daily=2,
                             peak_comments_hourly=2,
                             peak_comments_daily=1,
                             peak_follows_hourly=1,
                             peak_follows_daily=None,
                             peak_unfollows_hourly=1,
                             peak_unfollows_daily=2,
                             peak_server_calls_hourly=None,
                             peak_server_calls_daily=2)
session.set_relationship_bounds(enabled=True,
                                potency_ratio=None,
                                delimit_by_numbers=True,
                                max_followers=3,
                                max_following=1,
                                min_followers=1,
                                min_following=1)
session.like_by_tags(my_hashtags, amount=4, media=None)
session.unfollow_users(amount=1, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                       style="FIFO",
                       unfollow_after=5*60, sleep_delay=501)
session.unfollow_users(amount=1, instapy_followed_enabled=True, instapy_followed_param="all",
                       style="FIFO", unfollow_after=5*60,
                       sleep_delay=501)
session.like_by_tags(['python3', 'javascript'], amount=2)

session.end()
