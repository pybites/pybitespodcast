import pytest

from pybitespodcast.search import FeedSearcher, Episode


@pytest.fixture(scope="module")
def fs():
    return FeedSearcher()


@pytest.mark.parametrize(
    "term, expected",
    [
        (
            "review",
            [
                Episode(
                    title="#002 - Code Reviews",
                    link="https://www.pybitespodcast.com/1501156/6908411-002-code-reviews",
                )
            ],
        ),
        (
            "mindset",
            [
                Episode(
                    title="#020 - From Physicist to Cloud Software Architect",
                    link="https://www.pybitespodcast.com/1501156/8246289-020-from-physicist-to-cloud-software-architect",
                ),
                Episode(
                    title="#019 - 5 Tips for Dealing with Stress",
                    link="https://www.pybitespodcast.com/1501156/8194025-019-5-tips-for-dealing-with-stress",
                ),
                Episode(
                    title="#018 - High Risk Mindset: Going From Marketer to Developer",
                    link="https://www.pybitespodcast.com/1501156/8149274-018-high-risk-mindset-going-from-marketer-to-developer",
                ),
                Episode(
                    title="#017 - The Importance of Creativity as a Developer",
                    link="https://www.pybitespodcast.com/1501156/8128624-017-the-importance-of-creativity-as-a-developer",
                ),
                Episode(
                    title="#015 - Deliberate Practice is key",
                    link="https://www.pybitespodcast.com/1501156/8074629-015-deliberate-practice-is-key",
                ),
                Episode(
                    title="#013 - The Mindset of a Developer",
                    link="https://www.pybitespodcast.com/1501156/8005574-013-the-mindset-of-a-developer",
                ),
                Episode(
                    title="#011 - Marketing Yourself",
                    link="https://www.pybitespodcast.com/1501156/7603798-011-marketing-yourself",
                ),
                Episode(
                    title="#006 - The PyBites Python Tips Book",
                    link="https://www.pybitespodcast.com/1501156/7174954-006-the-pybites-python-tips-book",
                ),
                Episode(
                    title="#004 - Goal Setting",
                    link="https://www.pybitespodcast.com/1501156/6965435-004-goal-setting",
                ),
            ],
        ),
        (
            "habit",
            [
                Episode(
                    title="#019 - 5 Tips for Dealing with Stress",
                    link="https://www.pybitespodcast.com/1501156/8194025-019-5-tips-for-dealing-with-stress",
                ),
                Episode(
                    title="#014 - Habits",
                    link="https://www.pybitespodcast.com/1501156/8055529-014-habits",
                ),
                Episode(
                    title="#006 - The PyBites Python Tips Book",
                    link="https://www.pybitespodcast.com/1501156/7174954-006-the-pybites-python-tips-book",
                ),
                Episode(
                    title="#004 - Goal Setting",
                    link="https://www.pybitespodcast.com/1501156/6965435-004-goal-setting",
                ),
            ],
        ),
        ("procrast", []),
    ],
)
def test_search(fs, term, expected):
    actual = list(fs.search(term))
    assert actual == expected


def test_strip_html(fs):
    assert fs._strip_html("<p>Some text</p>") == "Some text"


def test_get_pybites_link(fs):
    link = "https://www.buzzsprout.com/1501156/6908411-002-code-reviews.mp3?blob_id=29338679"
    actual = fs._get_pybites_link(link)
    expected = "https://www.pybitespodcast.com/1501156/6908411-002-code-reviews"
    assert actual == expected
