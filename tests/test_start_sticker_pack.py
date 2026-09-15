from AnonXMusic.plugins.bot import start


def test_start_stickers_cycle():
    start._START_STICKER_INDEX = 0

    stickers = ["s1", "s2", "s3"]

    assert [start.get_next_start_sticker(stickers) for _ in range(5)] == [
        "s1", "s2", "s3", "s1", "s2"
    ]
