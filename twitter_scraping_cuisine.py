# -*- coding: utf-8 -*-
"""Twitter_Scraping_cuisine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EWuENnlfb67U8Cr-FM2vDwbvQh1GG6Gr
"""

# --------------------------------------------------------------------------------------------------------------------------------------
# imports and installs
#---------------------------------------------------------------------------------------------------------------------------------------  

import csv
import datetime
import os
import time
!pip install mysql-connector-python
import mysql.connector as msql
import pandas as pd
import pip
!pip install tweepy
import tweepy  # Library required for Twitter API

from mysql.connector import Error
from sqlalchemy import create_engine

# --------------------------------------------------------------------------------------------------------------------------------------
# API keys and Access Tokens
#--------------------------------------------------------------------------------------------------------------------------------------- 

sleep_on_rate_limit = False

api_key = "wAkEla5pcCAtwCtQfEr7uucMb"
api_key_secret = "k9dqhGcAeVUMCcpVHdzMiICGVmuiZj5ZKEnzGlffSZjfFMDMIS"

access_token = "3103544315-a0fpmcqJbRcUk8wlMaQ97UeUHo8DWx7NZj0r3ZN"
access_token_secret = "ySG3bQqQap0IuOIsabdCSM20zV7olRkBWqdUTaE4J0yaB"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=False)

#--------------------------------------------------------------------------------------------------------------------------------------  
# PART 1
# Below is a code snippet for searching for a keyword from input.xlsx file and displaying the tweets (number of tweets=20) containing it 
#  please download the input.xlxs file from canvas or my github for this part of code to run.
#--------------------------------------------------------------------------------------------------------------------------------------
keywords = pd.read_excel("input.xlsx", sheet_name=0, header=0, names=None, index_col=None, usecols=None).iloc[:,0]
keywords = list(keywords) #converted this into a list

num_tweets=20

#dictionary for all raw data
raw_tweets = dict(zip( keywords, [ api.search_tweets( 
                       q=keyword,
                       lang="en",
                       count=num_tweets,
                       tweet_mode='extended_tweet')
        for keyword in keywords ] ))

keys = ['id_str', 'text'] #for reaching data inside tweet
user_keys = ['screen_name','created_at'] #for reaching data inside user dictionary
tweets = [] #initialising empty list
[ tweets.extend( [ [key] + [ t._json[k] for k in keys ] + [t._json['user'][uk] for uk in user_keys] for t in raw_t ] ) for key, raw_t in raw_tweets.items() ] #flattened list of lists
print(tweets)

"""# OUTPUT part 1


[['#cuisine', '1591613020333297665', 'RT @Visit_Japan: Kamakura’s Komachi street is lined with over 200 shops, but the ‘Daibutsu-yaki’ or ‘Buddha Cake’ from Tomoya Kamakurakomac…', 'LuAskani', 'Wed May 15 22:46:28 +0000 2013'], ['#cuisine', '1591612382996226051', 'RT @ZhengguanCN: What do you want to eat for lunch ?\nThere are duck blood vermicelli soup, xiao long bao, and fried Spring rolls, do you wa…', 'Yamlkumo51', 'Sun Nov 04 09:11:40 +0000 2018'], ['#cuisine', '1591609606983540737', 'RT @Visit_Japan: Kamakura’s Komachi street is lined with over 200 shops, but the ‘Daibutsu-yaki’ or ‘Buddha Cake’ from Tomoya Kamakurakomac…', 'myday6am', 'Tue Jun 23 11:00:42 +0000 2015'], ['#cuisine', '1591599237690687495', '"These days, the Northern Rivers is a foodie mecca with an endless choice of different styles, cuisines and price p… https://t.co/xA54ys0oBF', 'BigVolcano', 'Tue Dec 09 23:22:03 +0000 2008'], ['#cuisine', '1591587994590388226', 'Oh just take a look at this! \r\r #Flower #Plant #Flowerpot #Orange #Houseplant #Wood #Ingredient #FlowerArranging… https://t.co/cugLGfCLYL', 'IanHornby13', 'Sat Mar 26 04:50:10 +0000 2022'], ['#cuisine', '1591587363582525442', 'RT @Visit_Japan: Kamakura’s Komachi street is lined with over 200 shops, but the ‘Daibutsu-yaki’ or ‘Buddha Cake’ from Tomoya Kamakurakomac…', 'Sushime21', 'Tue Aug 02 23:28:41 +0000 2011'], ['#cuisine', '1591585427110383616', '#WritingCommunity #writerslift #blog #link #book #poetry #music #shortstories #script #film #movie #creativity… https://t.co/TKKRPHo6I5', 'bmurphypointman', 'Mon Jun 25 04:38:20 +0000 2012'], ['#cuisine', '1591581185620131842', 'RT @Planeteco21: Share if you find it terrific! \r\r #Food #Green #Tableware #Ingredient #Recipe #Drink #Cuisine #Solution #Dish #Cooking htt…', 'cocktailmanual', 'Tue Jan 01 13:55:23 +0000 2019'], ['#cuisine', '1591581156130045952', 'Share if you find it terrific! \r\r #Food #Green #Tableware #Ingredient #Recipe #Drink #Cuisine #Solution #Dish… https://t.co/pXxpIsZG4j', 'Planeteco21', 'Tue Aug 30 19:03:56 +0000 2022'], ['#cuisine', '1591578314560655361', 'RT @Visit_Japan: Kamakura’s Komachi street is lined with over 200 shops, but the ‘Daibutsu-yaki’ or ‘Buddha Cake’ from Tomoya Kamakurakomac…', 'tyaya9822', 'Sat Aug 22 10:29:36 +0000 2009'], ['#pizza', '1591612990012653568', "RT @AndyMc81: Who wants to WIN Domino's🍕 #Pizza?!\n\nGet ready for #NFL Week 10 &amp; Enter to WIN by:\n\n1. Follow Me, @FiredUpNET &amp; @DominosCanad…", 'SteveSmith35', 'Sun Feb 06 05:03:36 +0000 2011'], ['#pizza', '1591612597371301888', 'RT @6Yaboiqa: My dawg just killed himself bc his girl cheating #gorecontent #gore #gore #sad #bozo #LGBTQ #pizza #gore https://t.co/eRCB3wR…', 'Ari47552393', 'Wed Sep 07 22:45:19 +0000 2022'], ['#pizza', '1591612585031651328', 'Our Appondanza® Signature Pizza is loaded with 12 delicious toppings: Mozzarella, pepperoni, beef, Canadian bacon,… https://t.co/bML3BTKeEK', 'PizzaWorldGC', 'Thu Jan 02 18:18:17 +0000 2014'], ['#pizza', '1591611736091951105', "RT @AndyMc81: Who wants to WIN Domino's🍕 #Pizza?!\n\nGet ready for #NFL Week 10 &amp; Enter to WIN by:\n\n1. Follow Me, @FiredUpNET &amp; @DominosCanad…", 'JamieThomasTV', 'Thu Dec 12 21:47:35 +0000 2013'], ['#pizza', '1591610981549047809', 'RT @LoveTheHumans: @elonmusk eating PIZZA IN SPACE needs to happen. \n\n🪐⚔️🍕\n\n#ELONMUSK #NFTs  #pizza #SpaceX @SpaceAddictsNFT #SpaceAddicts #…', 'Ricky_361', 'Sun Sep 30 17:37:14 +0000 2012'], ['#pizza', '1591610337396391936', 'RT @AmenaAlam5: Meaty-mashroom-ham pizza 🍕\nAll pizza treats are special. No matter how silly the reason is! It was one of them 😋.\n#pizza #D…', 'carlsl', 'Fri Oct 09 14:27:45 +0000 2009'], ['#pizza', '1591609957941665793', 'RT @LoveTheHumans: @elonmusk eating PIZZA IN SPACE needs to happen. \n\n🪐⚔️🍕\n\n#ELONMUSK #NFTs #pizza #SpaceX @SpaceAddictsNFT #SpaceAddicts #…', 'CrawliesCreepto', 'SSat Jun 12 03:34:52 +0000 2021'], ['#pizza', '1591609805105397761', 'Weekend pies so far \n \n#Pizza\n \nhttps://t.co/mMdesMlOBB https://t.co/tgyuZFUbBv', 'DiningCooking', 'Sat Aug 01 07:11:08 +0000 2015'], ['#pizza', '1591609314212732928', 'RT @PonyExpresshq: Statistics show that mass messaging is one of the most cost-effective marketing methods for #smallbusinesses. \n\n💡 Learn…', 'OfertasVips', 'Sat Mar 02 17:37:26 +0000 2013'], ['#pizza', '1591608535250509824', 'Statistics show that mass messaging is one of the most cost-effective marketing methods for #smallbusinesses. \n\n💡 L… https://t.co/bQEUcvQiPH', 'PonyExpresshq', 'Thu Sep 14 00:04:29 +0000 2017'], ['#recipe', '1591613088352309248', 'Looking for an easy way to cook turkey breast? Look no further than your crock pot! This Slow Cooker Turkey Breast… https://t.co/IdydtJpYrj', 'SlowCookerRyan', 'Wed Oct 05 21:50:17 +0000 2022'], ['#recipe', '1591612361173090306', 'RT @LifeExtension: There are a few ways to increase the #protein content of your #waffles, but the easiest way is by adding protein powder…', 'wootendw', 'Fri Sep 02 02:34:33 +0000 2011'], ['#recipe', '1591612021145063426', 'RT @Anns_Life: This sour cream #cheesecake recipe is creamy &amp; delicious. Easy-to-make, your guests and family will love every tangy-sweet b…', 'Anns_Life', 'Mon Apr 06 16:07:25 +0000 2009'], ['#recipe', '1591612013075202048', 'RT @cookingwithdog: Enjoy one of the healthiest Japanese sweets, Tofu Dango🍡 https://t.co/pM0nOZEK9W with soybean flour, black sesame seeds…', 'cookingwithdog', 'Sat Mar 13 01:28:27 +0000 2010'], ['#recipe', '1591611852349669376', 'This quick and easy #recipe for #CrockPot Pineapple Dump Cake requires no stirring or mixing. Just toss the ingredi… https://t.co/6tdf0xmX64', 'CrockPotLadies', 'Thu Sep 01 22:56:07 +0000 2011'], ['#recipe', '1591611385582358530', "RT @SchlegdawgYT: Heyyyy, it's time for a #writerslift!\n\nPost your: #wip #book #novel #drawing #sketch #selfhelp #health #recipe #poetry #a…", 'RamonaEldorrad2', 'Mon Aug 12 12:12:03 +0000 2019'], ['#recipe', '1591610437727965184', 'Try our new recipe: : Rhubarb Jam https://t.co/H1t1bcVbG8 #recipe', 'RecipeRodeo1', 'Thu Dec 12 23:17:58 +0000 2013'], ['#recipe', '1591609551270580224', 'RT @ParnellChef: Mac &amp; Cheese w/ Cottage Cheese &amp; Sour Cream🧀\n\nhttps://t.co/E0b7gtv33G\n\n#foodie #foodies #dinner #dinnertime #foodblog #foo…', 'helenscchin', 'Thu Dec 30 00:49:02 +0000 2010'], ['#recipe', '1591609416029437952', 'RT @simplyart4794: Cooking · Simply Cook Ep.60\nApple Jam\nhttps://t.co/uNKhwEhl65\n\nCredit for @simplycook4794 \n\nFollow @simplyart4794 \n\n#sim…', 'Y4794', 'Sun Aug 02 11:22:04 +0000 2020'], ['#recipe', '1591609290023997440', "RT @SchlegdawgYT: Heyyyy, it's time for a #writerslift!\n\nPost your: #wip #book #novel #drawing #sketch #selfhelp #health #recipe #poetry #a…", 'Kalimaxos1', 'Tue Mar 10 12:39:49 +0000 2020'], ['#indianfood', '1591594822150017024', 'After 6 hours in the kitchen with my mother we made delicious beef curry and Roti 😋#indianfood https://t.co/UCfv5DVMfr', 'cutiechan516', 'Sun Jan 16 02:54:48 +0000 2022'], ['#indianfood', '1591576917819506690', 'Rooh Restaurant – A Regionally Diverse Culinary Experience https://t.co/BAmbND2lNx @SplashMagWW @roohchicago… https://t.co/Vv3BogbT3T', 'SplashMagWW', 'Thu Mar 12 23:03:33 +0000 2009'], ['#indianfood', '1591567794415587331', 'Friday Night Takeaway https://t.co/fxtTCDodRN #pizza #chinese #recipes #fakeaway #sushi #indianfood #duck', 'dads_dinners', 'Wed May 02 13:16:20 +0000 2018'], ['#indianfood', '1591567775155519488', 'RT @spicewithkaur: Are you guys trying this reciepe on this weekend…?                         #tandorichicken #indianfood #spicyfood https:…', 'FabrcioALyra1', 'Mon Aug 08 18:39:34 +0000 2022'], ['#indianfood', '1591561112704921600', 'RT @spicewithkaur: Are you guys trying this reciepe on this weekend…?                         #tandorichicken #indianfood #spicyfood https:…', 'JamiBen2022', 'Sun Nov 06 10:25:04 +0000 2022'], ['#indianfood', '1591561099056672768', 'RT @spicewithkaur: Always craving for something unique…?\n#conestogacollege #food #foodie #weekendcraving #thali #indianfood https://t.co/Er…', 'JamiBen2022', 'Sun Nov 06 10:25:04 +0000 2022'], ['#indianfood', '1591561071219085312', 'RT @spicewithkaur: So wait is over now….😀  Here I am going to post yummy nd declious paneer tikka..😋 #food #conestogacollege #indianfood #i…', 'JamiBen2022', 'Sun Nov 06 10:25:04 +0000 2022'], ['#indianfood', '1591561057235091459', 'RT @spicewithkaur: Here is a indian sweet which is popular in indian the most…Carrot halwa#Conestogacollege #indianfood #Indiansweet #stree…', 'JamiBen2022', 'Sun Nov 06 10:25:04 +0000 2022'], ['#indianfood', '1591561043842588672', 'RT @spicewithkaur: Here is mouthwatering recipe…… PAV BHAJI #conestoga #indianfood #indianstreet #foodie #spicyndsweet https://t.co/bwceqr7…', 'JamiBen2022', 'Sun Nov 06 10:25:04 +0000 2022'], ['#indianfood', '1591556949287395329', '"@KitchenAnitas" Book a different experience this year for you office Christmas meal! Private dining experience in… https://t.co/kYqlZbMInM', 'OxTweets', 'Thu Feb 07 04:00:44 +0000 2013'], ['#italianfood', '1591611632651993089', "RT @jpkeaney111: Fresh San Marzano tomatoes from the garden , pork , meatballs(beef,veal &amp; pork) and sausage. It's going to be delicious wh…", 'MaryVicars', 'Thu May 26 19:05:28 +0000 2022'], ['#italianfood', '1591610863546519553', 'Keeping it local @sainttheosnyc &amp; their #shellfish #pasta 🦞🦑🦪🍝#westvillagenyc #nycrestaurants #italianfood @ Saint… https://t.co/wCRM412lnz', 'LZNYC', 'Mon Jun 08 15:52:21 +0000 2009'], ['#italianfood', '1591591976864223232', 'Behind that little door is a wonderful restaurant 🙏 #villamarina #Henleyonthames  #goodfood #italianfood… https://t.co/uTI3iwpckn', 'thack8', 'Tue Dec 28 01:11:37 +0000 2010'], ['#italianfood', '1591589244388401153', '#sundaysauceonasaturdaynight makes me happy!!  #sundaysauce #italianfood #Sauce #lovetocook https://t.co/Nc18buUDy4', 'LongIslandLady4', 'Wed Nov 09 16:46:04 +0000 2022'], ['#italianfood', '1591584882941218817', 'RT @DelevingneNiko: Was at Seta for a dinner date, food was amazing 😍. Rate your favourite dish below 😋\n#sydneylife #italianfood #asiandoll…', 'MrGeeT97314551', 'Fri Aug 03 21:45:34 +0000 2018'], ['#italianfood', '1591581937684152320', 'RT @kyleecooks: A hearty Italian Meatball Soup for everyone! Comforting, warming and so delicious, the smell of this cooking alone will bri…', 'kyleecooks', 'Sat May 24 01:10:45 +0000 2008'], ['#italianfood', '1591580555476619264', 'Was at Seta for a dinner date, food was amazing 😍. Rate your favourite dish below 😋\n#sydneylife #italianfood… https://t.co/x5DIf0rENU', 'DelevingneNiko', 'Sun Oct 21 02:27:02 +0000 2018'], ['#italianfood', '1591580518587699200', 'Was at Seta for a dinner date, food was amazing 😍. Rate your favourite dish below 😋\n#sydneylife #italianfood… https://t.co/4ITmurfSuX', 'DelevingneNiko', 'Sun Oct 21 02:27:02 +0000 2018'], ['#italianfood', '1591569427761356803', 'A family favourite: my Ultimate Chicken Pasta! #food #cooking #italianfood #italian #pasta https://t.co/9n3BPup4kR', 'devondenizen', 'Wed Nov 09 10:32:48 +0000 2022'], ['#italianfood', '1591545341949657097', 'How to Make No Knead Focaccia Bread in 3 Hours: watch this AMAZING recipe https://t.co/ES4NWJft9i #bread #italianfood #baking', 'CamiHomeCooking', 'Sat Nov 12 21:11:27 +0000 2022'], ['#burger', '1591612876770385923', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A", 'Archerave1', 'Thu Apr 29 20:55:26 +0000 2010'], ['#burger', '1591612766066036737', '*   FIL   *   |   *   Filecoin    *   Crypto - BUY   *   PRİCE WİLL RİSE   RSI INDICATOR   |(   FIL_USDT   BUY   )|… https://t.co/GONguI0Qx4', 'TrendsBullBear', 'Thu Aug 04 20:41:05 +0000 2022'], ['#burger', '1591612481104920576', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A", 'carlsl', 'Fri Oct 09 14:27:45 +0000 2009'], ['#burger', '1591612046755647488', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A", 'donaldepperson', 'Sat Mar 20 01:21:58 +0000 2010'], ['#burger', '1591610783313666049', '#MOVR 90 Days\n#EGLD 90 Days\n#IOTX 90 Days\n#DASH 90 Days\n#ARPA 90 Days\n#XTZ 60 Days\n#CTSI 60 Days\n#WOO 60 Days\n#OM 6… https://t.co/R8TncFt4i8', 'StakingAlerts', 'Fri Mar 11 07:21:18 +0000 2022'], ['#burger', '1591608640334712833', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A", 'LIBERAT37008797', 'Sat Mar 28 10:37:32 +0000 2020'], ['#burger', '1591608293558210560', 'Double with pickles, #Burger sauce, and fried onions \n \n#Burgers\n \nhttps://t.co/abTWZI1wQF https://t.co/Gj499Ieecv', 'DiningCooking', 'Sat Aug 01 07:11:08 +0000 2015'], ['#burger', '1591606387259617280', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A", 'DanielMullett', 'Sun Jan 31 22:03:34 +0000 2016'], ['#burger', '1591604756866551808', 'A classic.\n\n#AllAmericanHamburger #Burger #LongIsland #LongIslandClassic #Classic #DriveIn… https://t.co/neNOMluesR', 'bear_fuzzy', 'Wed Jun 29 15:11:08 +0000 2011'], ['#burger', '1591602646808670208', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A", 'TheArtOfDean', 'Fri Jan 14 19:26:33 +0000 2022']]
Error while connecting to MySQL 1007 (HY000): Can't create database 'twitterscraping'; database exists
You're connected to database:  ('twitterscraping',)
Creating table....
cuisine table is created....
"""

#--------------------------------------------------------------------------------------------------------------------------------------
#  this piece of code will get data from above and put it in a table called "cuisine"
#---------------------------------------------------------------------------------------------------------------------------------------

try:
    conn = msql.connect(host='localhost', user='root',  
                        password='root@14')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE TwitterScraping") #database name = TwitterScraping
        print("TwitterScraping database is created")
except Error as e:
    print("Error while connecting to MySQL", e)


#creating the table and inserting data in the table
try:
    conn = msql.connect(host='localhost', 
                           database='TwitterScraping', user='root', 
                           password='root@14')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS cuisine;') #table name = cuisine
        print('Creating table....')
        cursor.execute("CREATE TABLE cuisine (Hashtag VARCHAR(20), Tweet_ID VARCHAR(50) NOT NULL, Tweet_text VARCHAR(300), Screenname VARCHAR(50), Joined varchar(30))")
        print("cuisine table is created....")
        for row in tweets:
            sql = "INSERT INTO TwitterScraping.cuisine VALUES (%s,%s,%s,%s,%s)"
            # print(tuple(row))
            cursor.execute(sql, tuple(row))
            # print("Record inserted")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

# Execute query
sql = 'SELECT * FROM cuisine'
cursor.execute(sql)

#--------------------------------------------------------------------------------------------------------------------------------------
#  PART 2
#  this piece of code will get a particular username from above results and print out most recent 20 tweets from their profile (RT included)
#---------------------------------------------------------------------------------------------------------------------------------------
user = "gordonramsay" #hardcoded littleindchampa

tweets = api.user_timeline(screen_name=user, 
                           # 200 is the maximum allowed count
                           count=20,
                           include_rts = True,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended')
columns = ['ID', 'Username', 'Tweet Text', 'Likes','Created At', 'Location', 'Joined' ]
data = []
for tweet in tweets:
    data.append([tweet.id_str, tweet.user.screen_name, tweet.full_text, tweet.favorite_count, tweet.created_at, tweet.user.location, tweet.user.created_at])

df = pd.DataFrame(data, columns = columns)

df

"""# output part 2

index,ID,Username,Tweet Text,Likes,Created At,Location,Joined
0,1591357931047555072,GordonRamsay,Now that's how you make the perfect pepperoni pizza over at Street Pizza Camden !! @GordonRamsayGRR https://t.co/qLgn1V2ZcC,1308,2022-11-12 09:11:11,,2010-02-01 08:31:59
1,1590994868356403201,GordonRamsay,"Just look at that stunning Isle of Skye scallop, toasted hay, miataki, jus gras over at Restaurant Gordon Ramsay !! @GordonRamsayGRR https://t.co/Z3PTOfTxVv",741,2022-11-11 09:08:30,,2010-02-01 08:31:59
2,1590815571360485381,GordonRamsay,It’s wedding season tonight on an all new @HellsKitchenFOX ! See you at 8/7c ! https://t.co/o5UudZvLi0,336,2022-11-10 21:16:02,,2010-02-01 08:31:59
3,1590635034129883136,GordonRamsay,Christmas is right around the corner… !! Head to https://t.co/pd4jgj6jTy to join us at Gordon Ramsay Restaurants for Christmas dinner the Ramsay way !! Gx @GordonRamsayGRR https://t.co/vW9x6aB2ua,470,2022-11-10 09:18:39,,2010-02-01 08:31:59
4,1590335445682253824,GordonRamsay,I'm in my back garden for quite the showdown the next few week ! UK...#Uncharted starts tonight at 8 PM on @NatGeoUK ! https://t.co/xrxB2mJ6rl,521,2022-11-09 13:28:11,,2010-02-01 08:31:59
5,1590279737888636928,GordonRamsay,I'm so excited that Bread Street Kitchen Battersea Power Station opens it's doors TODAY !! Join us for a taste of our signature dishes and cocktails... Can't wait to see you ! Gx @GordonRamsayGRR https://t.co/RLMNsjVARL,833,2022-11-09 09:46:50,,2010-02-01 08:31:59
6,1589187410293772288,GordonRamsay,A Bread Street Kitchen signature... Saddleback pork belly !! @GordonRamsayGRR https://t.co/lcoqdlmQfs,1291,2022-11-06 09:26:18,,2010-02-01 08:31:59
7,1588820740408999936,GordonRamsay,"Aynhoe Park Deer, beetroot, cranberry, red amaranth... just stunning dishes over at Pétrus !! @GordonRamsayGRR https://t.co/Mnwc9DEWXZ",880,2022-11-05 09:09:18,,2010-02-01 08:31:59
8,1588460455630094338,GordonRamsay,Step inside @gracademy’s indulgent chocolate desserts class !! https://t.co/rw73dAeD0R,811,2022-11-04 09:17:39,,2010-02-01 08:31:59
9,1588101301644283910,GordonRamsay,Just look at those delicious River Restaurant scallops... beautifully baked in the shell with seaweed &amp; lime butter !! @GordonRamsayGRR https://t.co/tUIUF78kY5,863,2022-11-03 09:30:30,,2010-02-01 08:31:59
10,1587735574517096448,GordonRamsay,Cheesus… just look at that delicious mac &amp; cheese over at Heddon Street Kitchen !! @GordonRamsayGRR https://t.co/2i9VPpLYl9,1427,2022-11-02 09:17:14,,2010-02-01 08:31:59
11,1587372490908745728,GordonRamsay,Celebrate World Vegan Day in style with bottomless charred aubergine Street Pizza !! @GordonRamsayGRR https://t.co/x1UDw0Qsn5,648,2022-11-01 09:14:28,,2010-02-01 08:31:59
12,1587009198465990659,GordonRamsay,No tricks here... only treats !! Join us at @GordonRamsayGRR for the most delicious sweet treats this Halloween ! https://t.co/GKvcvQRIfw,1694,2022-10-31 09:10:52,,2010-02-01 08:31:59
13,1586646676554514433,GordonRamsay,A Street Burger classic... the butternut bhaji burger !! @GordonRamsayGRR https://t.co/Njn2gZUhxR,1204,2022-10-30 09:10:20,,2010-02-01 08:31:59
14,1586372283924238337,GordonRamsay,Your family won't call you a donut with this recipe this #Halloween Weekend ! Just play #ChefBlast to get the recipe now: https://t.co/x3KGcSyRR0 https://t.co/AXCzLpjlY9,748,2022-10-29 15:00:00,,2010-02-01 08:31:59
15,1586267962692227072,GordonRamsay,The weekend calls for sweet treats ! Delicious apple and pecan sticky toffee pudding over at @gracademy !! https://t.co/WoU9NSv1Du,749,2022-10-29 08:05:28,,2010-02-01 08:31:59
16,1585907488666243073,GordonRamsay,Looks like Gordon Ramsay Bar &amp; Grill have turned up the heat !! @GordonRamsayGRR https://t.co/4uRS1FLvMs,898,2022-10-28 08:13:04,,2010-02-01 08:31:59
17,1585682412570566656,GordonRamsay,We’re bringing the heat on @HellsKitchenFOX at 8/7c tonight !! https://t.co/BOa9mMeEGb,459,2022-10-27 17:18:42,,2010-02-01 08:31:59
18,1585548530428567553,GordonRamsay,"Apple parfait, Calvados, walnut, cinnamon… stunning dishes at Pétrus !! @GordonRamsayGRR https://t.co/HdmsoyAvzi",629,2022-10-27 08:26:42,,2010-02-01 08:31:59
19,1585359979430940672,GordonRamsay,Hey @kenjeong....you can have @MissPiggy !!! She was a nightmare in my kitchen ! Hopefully she's better on the @MaskedSingerFOX panel ! See you at 8/7c https://t.co/WiUzfB7s1R,388,2022-10-26 19:57:28,,2010-02-01 08:31:59
"""

#--------------------------------------------------------------------------------------------------------------------------------------
#  this piece of code will get data from tweets list and put it in a table called "tweets"
#---------------------------------------------------------------------------------------------------------------------------------------

try:
    conn = msql.connect(host='localhost', user='root',  
                        password='root@14')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE TwitterScraping") #database name = TwitterScraping
        print("TwitterScraping database is created")
except Error as e:
    print("Error while connecting to MySQL", e)

try:
    conn = msql.connect(host='localhost', 
                           database='TwitterScraping', user='root', 
                           password='root@14')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS tweets;') #table name = tweets
        print('Creating table....')
        cursor.execute("CREATE TABLE tweets (ID VARCHAR(30) NOT NULL, Username VARCHAR(250), Tweet_text VARCHAR(400), Likes int, Created_at VARCHAR(250), location VARCHAR(50), User_joining_date VARCHAR(50))")
        print("test table is created....")
        for i,row in df.iterrows():
            sql = "INSERT INTO TwitterScraping.tweets VALUES (%s,%s,%s,%s,%s,%s)"
            print(tuple(row))
            cursor.execute(sql, tuple(row))
            # print("Record inserted")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

"""SQL Queries on above table:

1. SELECT * FROM tweets 
    WHERE Created_at = #last 24 hours
"""

#--------------------------------------------------------------------------------------------------------------------------------------
#  PART 3
#  this piece of code will get data from input.xlsx file and store 10 tweets for each hashtag 
#  please download the input.xlxs file from canvas or my github for this part of code to run.
#---------------------------------------------------------------------------------------------------------------------------------------

keywords = pd.read_excel("input.xlsx", sheet_name=0, header=0, names=None, index_col=None, usecols=None).iloc[:,0]
keywords = list(keywords) #converted this into a list

num_tweets=10

#dictionary for all raw data
raw_tweets = dict(zip( keywords, [ api.search_tweets( 
                       q=keyword,
                       lang="en",
                       count=num_tweets,
                       tweet_mode='extended_tweet')
        for keyword in keywords ] ))

keys = ['id_str', 'text'] #username would be really good
tweets = []
[ tweets.extend( [ [key] + [ t._json[k] for k in keys ] for t in raw_t ] ) for key, raw_t in raw_tweets.items() ] #flattened list of lists
tweets

"""# output of PART 3

[['#cuisine', '1591587994590388226', 'Oh just take a look at this! \r\r #Flower #Plant #Flowerpot #Orange #Houseplant #Wood #Ingredient #FlowerArranging… https://t.co/cugLGfCLYL'], ['#cuisine', '1591587363582525442', 'RT @Visit_Japan: Kamakura’s Komachi street is lined with over 200 shops, but the ‘Daibutsu-yaki’ or ‘Buddha Cake’ from Tomoya Kamakurakomac…'], ['#cuisine', '1591585427110383616', '#WritingCommunity #writerslift #blog #link #book #poetry #music #shortstories #script #film #movie #creativity… https://t.co/TKKRPHo6I5'], ['#cuisine', '1591581185620131842', 'RT @Planeteco21: Share if you find it terrific! \r\r #Food #Green #Tableware #Ingredient #Recipe #Drink #Cuisine #Solution #Dish #Cooking htt…'], ['#cuisine', '1591581156130045952', 'Share if you find it terrific! \r\r #Food #Green #Tableware #Ingredient #Recipe #Drink #Cuisine #Solution #Dish… https://t.co/pXxpIsZG4j'], ['#cuisine', '1591578314560655361', 'RT @Visit_Japan: Kamakura’s Komachi street is lined with over 200 shops, but the ‘Daibutsu-yaki’ or ‘Buddha Cake’ from Tomoya Kamakurakomac…'], ['#cuisine', '1591574944256696320', "It's absolutely bang-on! \r\r #Food #Tableware #Ingredient #Dishware #Plate #Recipe #Naturalfoods #Dish #Cuisine… https://t.co/OpulXy5Tx8"], ['#cuisine', '1591574599304908800', 'RT @Visit_Japan: Kamakura’s Komachi street is lined with over 200 shops, but the ‘Daibutsu-yaki’ or ‘Buddha Cake’ from Tomoya Kamakurakomac…'], ['#cuisine', '1591571977948770304', 'RT @Visit_Japan: Kamakura’s Komachi street is lined with over 200 shops, but the ‘Daibutsu-yaki’ or ‘Buddha Cake’ from Tomoya Kamakurakomac…'], ['#cuisine', '1591570896971788288', 'RT @Visit_Japan: Kamakura’s Komachi street is lined with over 200 shops, but the ‘Daibutsu-yaki’ or ‘Buddha Cake’ from Tomoya Kamakurakomac…'], ['#pizza', '1591590965562978305', 'RT @LoveTheHumans: @elonmusk eating PIZZA IN SPACE needs to happen. \n\n🪐⚔️🍕\n\n#ELONMUSK #NFTs #pizza #SpaceX @SpaceAddictsNFT #SpaceAddicts #…'], ['#pizza', '1591590705394339843', 'RT @LoveTheHumans: @elonmusk eating PIZZA IN SPACE needs to happen. \n\n🪐⚔️🍕\n\n#ELONMUSK #NFTs #pizza #SpaceX @SpaceAddictsNFT #SpaceAddicts #…'], ['#pizza', '1591590365710397441', '@elonmusk eating PIZZA IN SPACE needs to happen. \n\n🪐⚔️🍕\n\n#ELONMUSK #NFTs #pizza #SpaceX @SpaceAddictsNFT… https://t.co/ITyffh0AxB'], ['#pizza', '1591589951539671040', 'Night in 🍕\n#Netflix #Anime #Pizza https://t.co/RWIFF0JgBV'], ['#pizza', '1591589790641971202', "RT @re_hungry: Happy #Saturday lovely Hungrys! It's the #weekend &amp; perfect for #pizza - recipe: https://t.co/1Z04eMUEbA Homemade, #handmade…"], ['#pizza', '1591589502342287361', 'Ok, Italians, what is a bigger insult? Pineapple or baked beans on #pizza . https://t.co/XKLtZE5T8X'], ['#pizza', '1591589300348620805', "RT @AndyMc81: Who wants to WIN Domino's🍕 #Pizza?!\n\nGet ready for #NFL Week 10 &amp; Enter to WIN by:\n\n1. Follow Me, @FiredUpNET &amp; @DominosCanad…"], ['#pizza', '1591588914216697856', "RT @AndyMc81: Who wants to WIN Domino's🍕 #Pizza?!\n\nGet ready for #NFL Week 10 &amp; Enter to WIN by:\n\n1. Follow Me, @FiredUpNET &amp; @DominosCanad…"], ['#recipe', '1591590673161064449', 'This perfectly spiced &amp; tangy Triple Spice Pumpkin #ButtermilkPie is about to replace your traditional #pumpkinpie… https://t.co/BX6WMWQaRw'], ['#recipe', '1591590207132151808', 'RT @takrecipe: Today at Takrecipe, we want to make another authentic Turkish food. Turkish grilled chicken is one of the most popular and d…'], ['#recipe', '1591589837207146496', 'RT @Somasray: #meat #recipe MY STYLE MUTTON BUGLAMA https://t.co/2RrJo3qqP3 https://t.co/F3rAKwLTil'], ['#recipe', '1591589824095719424', 'RT @AskChefDennis: Prime Rib Roast also known as a standing rib roast is a cut of beef most people think is too difficult to cook at home.…'], ['#recipe', '1591589758878519296', 'RT @Living_Lou: Crispy baked chicken drumsticks - LOVE this recipe with the crispy skin!\n\nRECIPE: https://t.co/h6jzkFNXo1\n#cooking #recipe…'], ['#recipe', '1591589417952722945', 'Pumpkin Pie Milkshake {Recipe} https://t.co/ZcfQ5HpOCH \n\n#recipe #pumpkin #pumpkinpie #milkshake #pumpkinmilkshake… https://t.co/jl003OMzh6'], ['#recipe', '1591589163786113025', 'Post from 3 years ago today: Quinoa Con Pollo #recipe #icancookthat #archives https://t.co/huOqN4ezOZ https://t.co/NPhgJyY09n'], ['#recipe', '1591588176367439872', 'RT @Living_Lou: Enjoy this smoked salmon #recipe that uses salmon fillets, salt, pepper, brown sugar and rosemary!\n\nRECIPE: https://t.co/YJ…'], ['#recipe', '1591587618520694787', 'RT @Living_Lou: Enjoy this smoked salmon #recipe that uses salmon fillets, salt, pepper, brown sugar and rosemary!\n\nRECIPE: https://t.co/YJ…'], ['#indianfood', '1591576917819506690', 'Rooh Restaurant – A Regionally Diverse Culinary Experience https://t.co/BAmbND2lNx @SplashMagWW @roohchicago… https://t.co/Vv3BogbT3T'], ['#indianfood', '1591567794415587331', 'Friday Night Takeaway https://t.co/fxtTCDodRN #pizza #chinese #recipes #fakeaway #sushi #indianfood #duck'], ['#indianfood', '1591567775155519488', 'RT @spicewithkaur: Are you guys trying this reciepe on this weekend…?                         #tandorichicken #indianfood #spicyfood https:…'], ['#indianfood', '1591561112704921600', 'RT @spicewithkaur: Are you guys trying this reciepe on this weekend…?                         #tandorichicken #indianfood #spicyfood https:…'], ['#indianfood  d', '1591561099056672768', 'RT @spicewithkaur: Always craving for something unique…?\n#conestogacollege #food #foodie #weekendcraving #thali #indianfood https://t.co/Er…'], ['#indianfood', '1591561071219085312', 'RT @spicewithkaur: So wait is over now….😀  Here I am going to post yummy nd declious paneer tikka..😋 #food #conestogacollege #indianfood #i…'], ['#indianfood', '1591561057235091459', 'RT @spicewithkaur: Here is a indian sweet which is popular in indian the most…Carrot halwa#Conestogacollege #indianfood #Indiansweet #stree…'], ['#indianfood', '1591561043842588672', 'RT @spicewithkaur: Here is mouthwatering recipe…… PAV BHAJI #conestoga #indianfood #indianstreet #foodie #spicyndsweet https://t.co/bwceqr7…'], ['#indianfood', '1591556949287395329', '"@KitchenAnitas" Book a different experience this year for you office Christmas meal! Private dining experience in… https://t.co/kYqlZbMInM'], ['#indianfood', '1591541484599255041', 'I Love #IndianFood, But… 💩☹️'], ['#italianfood', '15915589244388401153', '#sundaysauceonasaturdaynight makes me happy!!  #sundaysauce #italianfood #Sauce #lovetocook https://t.co/Nc18buUDy4'], ['#italianfood', '1591584882941218817', 'RT @DelevingneNiko: Was at Seta for a dinner date, food was amazing 😍. Rate your favourite dish below 😋\n#sydneylife #italianfood #asiandoll…'], ['#italianfood', '1591581937684152320', 'RT @kyleecooks: A hearty Italian Meatball Soup for everyone! Comforting, warming and so delicious, the smell of this cooking alone will bri…'], ['#italianfood', '1591580555476619264', 'Was at Seta for a dinner date, food was amazing 😍. Rate your favourite dish below 😋\n#sydneylife #italianfood… https://t.co/x5DIf0rENU'], ['#italianfood', '1591580518587699200', 'Was at Seta for a dinner date, food was amazing 😍. Rate your favourite dish below 😋\n#sydneylife #italianfood… https://t.co/4ITmurfSuX'], ['#italianfood', '1591569427761356803', 'A family favourite: my Ultimate Chicken Pasta! #food #cooking #italianfood #italian #pasta https://t.co/9n3BPup4kR'], ['#italianfood', '1591545341949657097', 'How to Make No Knead Focaccia Bread in 3 Hours: watch this AMAZING recipe https://t.co/ES4NWJft9i #bread #italianfood #baking'], ['#italianfood', '1591533443938390017', "Fresh San Marzano tomatoes from the garden , pork , meatballs(beef,veal &amp; pork) and sausage. It's going to be delic… https://t.co/y15wa3btjy"], ['#italianfood', '1591522091991728128', 'A great local Italian lunch today at Da Vinci’s #hornchurch #essex #Foodie #food #italianfood #foodies #essexdining… https://t.co/KGBRu1gzuH'], ['#burger', '1591590440318676993', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A"], ['#burger', '1591589207952461824', '✨ #BURGER \n💵 Current Price: 0.548 \n📱 Look other coin infos with our app: https://t.co/vNpxF6rVbO https://t.co/YLFslJCZ3x'], ['#burger', '1591588294684741632', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A"], ['#burger', '1591588262313091073', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A"], ['#burger', '1591587637139234816', "My Cheese Burger-cinis turned out AWESOME! They are basically #Cheeseburger #Arancini and I'm proud! It's my Cheesy… https://t.co/NIc3xOlvsj"], ['#burger', '1591581493129842690', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A"], ['#burger', '1591577579647025160', 'Look no further than our mouthwatering Southwest #Burger for the perfect after work meal. Topped with avocado, egg,… https://t.co/FW3yM6B9zv'], ['#burger', '1591576190565101568', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A"], ['#burger', '1591573927234527232', 'RT @barefootgrill: Pit stop for lunch at our local #burger 🍔 joint. I’m hungry! https://t.co/po0lrYKdRC'], ['#burger', '1591573857655291907', "RT @ignitegrilling: Too much? Or you'd dive in?\n\n📸 IG labirrabar | #Burger https://t.co/vZdYxQo04A"]]
"""

#--------------------------------------------------------------------------------------------------------------------------------------
#  this piece of code will get data from "tweets" list and put it in a table called "cuisine"
#---------------------------------------------------------------------------------------------------------------------------------------
#database conenction - mysql workbench
try:
    conn = msql.connect(host='localhost', user='root',  
                        password='root@14')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE TwitterScraping") #database name = TwitterScraping
        print("TwitterScraping database is created")
except Error as e:
    print("Error while connecting to MySQL", e)


#creating the table and inserting data in the table
try:
    conn = msql.connect(host='localhost', 
                           database='TwitterScraping', user='root', 
                           password='root@14')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS cuisine;') #table name = cuisine
        print('Creating table....')
        cursor.execute("CREATE TABLE cuisine (Hashtag VARCHAR(20), Tweet_ID VARCHAR(50) NOT NULL, Tweet_text VARCHAR(300))")
        print("cuisine table is created....")
        for row in tweets:
            sql = "INSERT INTO TwitterScraping.cuisine VALUES (%s,%s,%s)"
            # print(tuple(row))
            cursor.execute(sql, tuple(row))
            # print("Record inserted")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

# Execute query
sql = 'SELECT * FROM cuisine'
cursor.execute(sql)