import asyncio
from swagger_client import *

def async_to_sync(awaitable):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(awaitable)

async def main():
    # cfg = ConfigApi()
    # header: ConfigOriginIntegrityHeader = cfg.get_x_origin_integrity_header()
    # print(header.v)
    
    # p = PodcastApi()
    # episodes: PodcastEpisodesGetRequest = p.get_podcast_episodes(limit=100)
    # episode: Datum24
    # for episode in episodes.data:
    #     print(f"{episode.title}: {episode.source_url}") 
    
    v = VideosApi()
    videos = v.get_videos(order="latest", limit=100)
    video: VideosGetRequest
    for video in videos.data:
        print(f"{video.title}: {video.short_url}")
    pass

if __name__ == "__main__":
    async_to_sync(main())