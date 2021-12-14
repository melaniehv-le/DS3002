#Final Project: Option 2 - Twitter Bot
# I worked with Jonathan Yu for the completion of this project
# My twitter handle used to tweet at is @melaniedsclass

import tweepy
import time
import requests
import re

Consumer_Key = 'CKTi1ONs6WmaWdGEfn5O4Shr2'
Consumer_Secret = '8iZKeGMjUn8ytq8OdLIlAZAcNUILsvrY5TFoW9wVXYaMVOcM4Y'
Access_Token = '1445460556865966087-ME5ylERTtj9dC517Rlo7SnznRjlxt3'
Access_Token_Secret = 'wAs2GxVQXSM5QQiLdehXnFnDq00UhTPX189w1UHKC62Ol'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authenticated")
except:
    print("Authentication Error")

def YahooStockAPI(stocksymbol):
    apikey='UERf5Pj6w99i7k25hBgN9w5JWhLDKfs1z09PYmmb'
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {"symbols": stocksymbol}
    headers = {
        'x-api-key': apikey
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

filename = "mentionid.txt"
def replyStock():
    mentions = api.mentions_timeline(count=1)
    for mention in reversed(mentions):
        mentionfile = open(filename, "a+")
        mentionfile.seek(0, 0)
        if (str(mention.id)+"\n") in mentionfile.readlines():
            print("Already replied to")
        else:
            mentionfile.write(str(mention.id) + "\n")
            print(str(mention.id) + ' : ' + mention.text)
            last_seen_id = mention.id
            print(mention.text)
            if "help" in mention.text.lower():
                status = '@' + mention.user.screen_name + " To use this bot, please tweet at @melaniedsclass '$(stockticker)'.  Ex. '$AMZN', $COF"
                try:
                    api.update_status(status=status, in_reply_to_status_id=last_seen_id)
                    return
                except:
                    return
            if "info" in mention.text.lower():
                status = '@' + mention.user.screen_name + " This bot responds with stock information when given one or multiple tickers. Information includes Regular Market Day High, Regular Market Day Low, Fifty Day Average, Price, and Market Time."
                try:
                    api.update_status(status=status, in_reply_to_status_id=last_seen_id)
                    return
                except:
                    return
            if '$' in mention.text:
                x = re.findall("(?<=\$)[A-Za-z]+", mention.text)
                for stock in x:
                    stock = stock.upper()
                    try:
                        stock_json = YahooStockAPI(stock)
                        status = '@' + mention.user.screen_name + ' ' + (
                            stock_json['quoteResponse']['result'][0]["shortName"] + "\n"
                                                                                        "Regular Market Day High: $" + str(
                            stock_json['quoteResponse']['result'][0]['regularMarketDayHigh']) + "\n"
                                                                                                "Regular Market Day Low: $" + str(
                            stock_json['quoteResponse']['result'][0]['regularMarketDayLow']) + "\n"
                                                                                               "Fifty Day Average: $" + str(
                            stock_json['quoteResponse']['result'][0]['fiftyDayAverage']) + "\n"
                                                                                           "Price: $" + str(
                            stock_json['quoteResponse']['result'][0]["regularMarketPrice"]) + "\n"
                                                                                              "Market Time: " + str(
                            time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(
                                (stock_json['quoteResponse']['result'][0]["regularMarketTime"])))) + "\n"
                        )
                    except:
                        status = '@' + mention.user.screen_name + " One or more of your stock tickers are not valid in your tweet...please try again with a valid stock ticker. For help or more info please '@' the bot and type help. "

                    try:
                        api.update_status(status=status, in_reply_to_status_id=last_seen_id)
                    except:
                        return
            else:
                status = '@' + mention.user.screen_name + " One or more of your stock tickers are not valid in your tweet...please try again with a valid stock ticker. For help or more info please '@' the bot and type help."
                try:
                    api.update_status(status=status, in_reply_to_status_id=last_seen_id)
                except:
                    return

    return

while True:
    replyStock()
    time.sleep(10)

#Documentation
# This bot implements APIs of both Yahoo Finance and of Twitter to create a functioning Twitter Bot that responds to your tweets within seconds.
# It works by reading in the stock ticker read in the tweet directed at it, and retrieves and displays data
# The data displayed depends on information about the stock that it pulled from the Yahoo Finance website in real time for that specific company
# This bot also has checkpoints throughout to offer an error message and an option for additional guidance or help if the stock ticker inputted is invalid
# What makes it operational is the use of individual access keys, many nested if else statements, and the successful integration of code being executed from live data sources

