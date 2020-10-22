import tweepy
import sys, os, time
import csv
import json
import jsonpickle
#import numpy as np
import pandas as pd
import kasg as ks
from tkinter import *
from tkinter import messagebox


access_token = '1151196229683929088-86wOu9aaxdYWgNvalp2pkNqucaXp5d'
access_token_secret ='NUfnsWNcgfbCPHotYT4LS6fXXfrRgHCQfALFsCi5NrjyH'
consumer_key = 'CN9YzSn3CqC9KT9bcByUCv8Kp'
consumer_secret = '0iiSCqbKO6IDCP5uG2qfreTZcuxICeLcIU1zwD6KwpOWItt02R'
 
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    return api
 
# Create API object
api = connect_to_twitter_OAuth()



def get_save_tweets(filepath, api, query, max_tweets=100,lang="in"):

    tweetCount = 0

    #Open file and save tweets
    with open(filepath, 'w') as f:
        f.write("[")
        # Send the query
        try:
            for tweet in tweepy.Cursor(api.search,q=query,tweet_mode='extended').items(max_tweets):         

            #Convert to JSON format
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + ',\n')
                tweetCount += 1

        #Display how many tweets we have collected
       
            print("Downloaded {0} tweets".format(tweetCount))
        except:
            window =Tk()
            #window.eval('tk:: PlaceWindow %s center ' % window.wifo_toplevel())
            window.withdraw()
            messagebox.showerror("Error giler", "error nak buat macam mana")
            window.deiconify()
            window.destroy()
            window.quit()

def cus(query):
    return query

fuh=cus("query");

get_save_tweets('tweetshwe.json', api,fuh)

def buang_coma():
    f=open('tweetshwe.json',"a+")
    f.write("]")
    f.close()
    with open('tweetshwe.json','rb+') as filehandle:
        filehandle.seek(-1,os.SEEK_END)
        filehandle.truncate()
        filehandle.seek(-3,os.SEEK_END)
        filehandle.truncate()
    f=open('tweetshwe.json',"a+")
    f.write("]")
    f.close()

buang_coma()

positiveList=[]
negativeList=[]
ks.getLexicons(positiveList, negativeList)
ham,kuym=ks.okay(positiveList, negativeList)
ks.read(ham,kuym)



