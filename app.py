import asyncio
from swagger_client import *

def async_to_sync(awaitable):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(awaitable)

async def main():
    cfg = ConfigApi()
    header: ConfigOriginIntegrityHeader = cfg.get_x_origin_integrity_header()
    print(header.v)
    podcasts = PodcastApi()
    episodes: LatestPodcast = podcasts.get_podcast_episodes()
    print(episodes)
    
if __name__ == "__main__":
    async_to_sync(main())