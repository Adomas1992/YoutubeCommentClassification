import os
import googleapiclient.discovery

def main():
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ""

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    video_id = "4pLY1X46H1E"
    comment_file = "comments.txt"

    existing_comments = set()
    if os.path.exists(comment_file):
        with open(comment_file, "r", encoding="utf-8") as f:
            for line in f:
                values = line.strip().split("\t")
                if len(values) == 2:
                    comment, comment_id = values
                    existing_comments.add(comment_id)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText"
    )

    while request is not None:
        response = request.execute()

        total_comments = response["pageInfo"]["totalResults"]
        print(f"Total Comments: {total_comments}")

        next_page_token = response.get("nextPageToken")
        print(f"Next Page Token: {next_page_token}")

        with open(comment_file, "a", encoding="utf-8") as file:
            for item in response["items"]:
                comment_id = item["id"]
                if comment_id not in existing_comments:
                    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                    print(comment)
                    file.write(f"{comment}\t{comment_id}\n")

        print("API Response Headers:")
        print(response.get("headers", {}))

        request = youtube.commentThreads().list_next(request, response)

if __name__ == "__main__":
    main()
