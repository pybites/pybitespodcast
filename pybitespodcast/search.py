from collections import namedtuple
import re

import feedparser

PYBITES_FEED = "https://feeds.buzzsprout.com/1501156.rss"
PODCAST_BASE_URL = "https://www.pybitespodcast.com"
EPISODE_MATCH = """Title: {title}
Link: {link}
"""
Episode = namedtuple("Episode", "title link")


class FeedSearcher:
    def __init__(self, feed=PYBITES_FEED):
        self.entries = feedparser.parse(feed).entries

    def _strip_html(self, text):
        return re.sub("<[^<]+?>", "", text)

    def _get_pybites_link(self, link):
        slug = re.sub(r".*.com/(.*)\.mp3.*", r"\1", link)
        return f"{PODCAST_BASE_URL}/{slug}"

    def search(self, term):
        for entry in self.entries:
            title = entry.title
            term = term.lower()
            if term in entry.summary.lower() or term in title.lower():
                link = entry.links[0]["href"]
                link = self._get_pybites_link(link)
                yield Episode(title, link)

    def _print_episode(self, episode):
        return EPISODE_MATCH.format(title=episode.title, link=episode.link)

    def __call__(self):
        while True:
            term = input("Search for episodes ('q' for exit): ")
            term = term.strip().lower()
            if term == "q":
                print("Bye")
                break
            matching_episodes = list(self.search(term))
            if not matching_episodes:
                print("No hits, search again")
                continue
            for episode in matching_episodes:
                print(self._print_episode(episode))


def main():
    fs = FeedSearcher()
    fs()


if __name__ == "__main__":
    main()
