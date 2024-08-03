import os

import base64

import pandas as pd
import tweepy as tp

import tkinter as tk
import tkinter.font as font

from tkinter import messagebox

def scrapeData():

    #The API Key and API Key Secret
    APIKey = 'dFPEbqBJBioWdU9hrcx9wYX8P'
    APIKeySecret = 'ZpFCGyFuVmyONlZXY27A9vQ8P74Qwq89R4x7neHCXsvqoLSkkF'

    #The Bearer Token
    bearerToken = 'AAAAAAAAAAAAAAAAAAAAAGlyvAEAAAAAe08p6H5AhIxLQq%2BAxMWTq%2FxZ4Z8%3DGtGveRwu9fgPF3mct0KDp92ozUVo5WwUVguFRDjV4SDPGl3J5J'

    #The Access Token and Access Secret Provided by the Twitter Developer Portal
    accessToken= '1818267428914176000-2tERjK1uTRRG4iwKdJc0dpVDCN6RW7'
    accessSecret= 'F8oHo0yGBPvFOa7VRuzAk5AhASjzgbK5l9xEeTQLIHPHU'

    #The Client Key and Client Secret Provided by the Twitter Developer Portal
    clientKey= 'c0lrMGFLYXluZ1hxR1dWOVBEaEw6MTpjaQ'
    clientSecret= 'F8oHo0yGBPvFOa7VRuzAk5AhASjzgbK5l9xEeTQLIHPHU'

    word = searchWord.get()
    number = dataValuesNumber.get()
    path = pathFolder.get() + "/TwitterData" + word + ".csv"

    authenticator = tp.OAuth1UserHandler(APIKey, APIKeySecret)
    authenticator.set_access_token(accessToken, accessSecret)

    api = tp.API(authenticator, wait_on_rate_limit = True)
    
    tweets = tp.Cursor(api.search_tweets, q = word, lang = "en").items(number)

    users_tweets = [ [tweet.created_at, tweet.id, tweet.user.screen_name, tweet.text] for tweet in tweets ]

    twitterDataFrame = pd.DataFrame(data = users_tweets, columns = ['location', "ID", "Username", "Content"])

    twitterDataFrame.to_csv(path)

    messagebox.showinfo("Python Data Scraper for Twitter", "The CSV file was saved successfully!")

window = tk.Tk()
window.geometry("500x500")
window.configure(bg = 'azure2')
window.title("Twitter Data Scraper")

searchWord = tk.StringVar()
dataValuesNumber = tk.IntVar(window)
pathFolder = tk.StringVar(window)

#Setup the Header
headingFrame = tk.Frame(window, bg = "light grey", bd = 5)
headingFrame.place(relx = 0.05, rely = 0.1, relwidth = 0.9, relheight = 0.1)

headingLabel = tk.Label(headingFrame, text = "Twitter Data Srcaper", fg = 'black', font = ('Calibri', 12, 'bold'))
headingLabel.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

#Get the Word that will be Searched
searchWordLabel = tk.Label(window, text = 'Enter the word that must be searched on twitter: ', bg = 'azure2', font = ('Calibri', 10))
searchWordLabel.place(x = 20, y = 150)

tk.Entry(window, textvariable = searchWord,  width = 35, font = ('Calibri', 10, 'bold')).place(x = 25, y = 175)

#Get the Number of Required Data Values
dataValueNumberLabel = tk.Label(window, text = 'Enter the number of required data values: ', bg = 'azure2', anchor = "e")
dataValueNumberLabel.place(x = 20, y = 200)

tk.Entry(window, textvariable = dataValuesNumber, width = 35, font = ('Calibri', 10, 'bold')).place(x = 25, y = 225)

#Get the Folder Path
pathFolderLabel = tk.Label(window, text = 'Enter the folder location where the CSV file will be saved: ', bg = 'azure2', anchor = "e")
pathFolderLabel.place(x = 20, y = 250)

tk.Entry(window, textvariable = pathFolder, width = 35, font = ('Calibri', 10, 'bold')).place(x = 25, y = 275)

#Create the 'Scrape Data' Button
ScrapeDataButton = tk.Button(window, text = 'Scrape Data', bg = 'light grey', fg = 'black', width = 15, height = 1, command = scrapeData)
ScrapeDataButton['font'] = font.Font(size = 15)
ScrapeDataButton.place(x = 20, y = 440)

#Create the 'Close' Button
CloseButton = tk.Button(window, text = 'Close', bg = 'light grey', fg = 'black', width = 15, height = 1, command = window.destroy)
CloseButton['font'] = font.Font(size = 15)
CloseButton.place(x = 305, y = 440)

window.mainloop()
