from AnonXMusic.plugins.bot.start import get_next_start_sticker


def test_start_stickers_rotate_one_by_one():
    stickers = ["sticker_1", "sticker_2", "sticker_3"]

    assert get_next_start_sticker(stickers) == "sticker_1"
    assert get_next_start_sticker(stickers) == "sticker_2"
    assert get_next_start_sticker(stickers) == "sticker_3"
    assert get_next_start_sticker(stickers) == "sticker_1"
