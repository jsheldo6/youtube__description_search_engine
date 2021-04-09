import sys
import config
import json
from googleapiclient.discovery import build

api_key = config.api_key
cse_id = config.cse_id
service = build("youtube", "v3", developerKey=api_key)

def search(query_term,maxPage):
    def get_video_info(video_id):
        result = service.videos().list(part='snippet',id=video_id).execute()
        try:
            return result['items'][0]
        except: 
            return None

    def get_video_list(search_results):
        video_list = []
        for item in search_results['items']:
            video_id = item['id']['videoId']
            video_info = get_video_info(video_id)
            if video_info:
                video_list.append(video_info)
        return video_list

    results = []
    tempResults = service.search().list(part="snippet",type="video", q=query_term, maxResults=50).execute()
    video_list = get_video_list(tempResults)
    results.extend(video_list)
    count = 0
    while tempResults['nextPageToken'] != '' and count < maxPage:
        token = tempResults['nextPageToken']
        tempResults = service.search().list(part="snippet",type="video", q=query_term, maxResults=50, pageToken=token).execute()
        video_list = get_video_list(tempResults)
        results.extend(video_list)
        count += 1
    fileName = "youtube_search_"+query_term+".json"
    with open(fileName, 'w', encoding='utf-8') as f:
         json.dump(results,f,ensure_ascii=False, indent=4)

    return results


if __name__ == '__main__':
    arg1 = sys.argv[0]
    if len(sys.argv) == 2:
        query_term = sys.argv[1]
        print("query: "+query_term)

        results = search(query_term, 1)
        fileName = "youtube_search_"+query_term+".json"
        with open(fileName, 'w' , encoding = 'utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
    else:
        print("usage: " + arg1 + " [search_term]")

