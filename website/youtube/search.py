"""This code is part of the sample code found on the Google developers page.
	https://developers.google.com/youtube/v3/samples/python"""

from apiclient.discovery import build

DEVELOPER_KEY = "Replace with API key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
    

def youtube_search(query, numResults):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


    search_response = youtube.search().list(
	q = query.lower(),
        part = "id, snippet",
        maxResults = numResults
    ).execute()

    videos = []
    channels = []
    playlists = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                        search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                        search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlist.append("%s (%s)" % (search_result["snippet"]["title"],
                                        search_result["id"]["videoId"]))
    return videos
