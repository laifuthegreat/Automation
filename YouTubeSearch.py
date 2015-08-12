#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from CustomClasses import Pair
from Input import put_in_pair


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBvq-IVa6ZndH_Xkg9gMpcgsee9I9-fND8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def do_search(query):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=query,
    type="channel",
    part="id,snippet",
    maxResults=7
  ).execute()

  videos = []
  channels = {}
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  result_list = []
  for search_result in search_response.get("items", []):
    result_list.append(
      Pair(
        search_result["snippet"]["title"],
        search_result["snippet"]["thumbnails"]['default']['url']
      )
    )
  return put_in_pair(result_list)
