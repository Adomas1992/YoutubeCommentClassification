import os
import googleapiclient.discovery

def main():

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBErdlLMzY6fxoAVrO1lNRLRzNfokDb-zY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    # Replace 'VIDEO_ID' with the actual video ID for which you want to retrieve comments
    video_id = "2OzpWVlt5Ok"

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText"
    )

    response = request.execute()

    # Open a file for writing comments
    with open("comments.txt", "w", encoding="utf-8") as file:
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            print(comment)
            file.write(comment + "\n")  # Write each comment to the file

if __name__ == "__main__":
    main()