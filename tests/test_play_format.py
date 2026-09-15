from AnonXMusic.utils.stream.stream import format_stream_caption


def test_stream_caption_has_separate_quotes_and_clickable_developer():
    caption = format_stream_caption(
        "Tum Ho",
        "5:17",
        "Ayush",
    )

    assert "> ❖ **Sᴛᴀʀᴛᴇᴅ Sᴛʀᴇᴀᴍɪɴɢ**" in caption
    assert "> ◯ **Tɪᴛʟᴇ :** Tum Ho" in caption
    assert "> ◯ **Dᴜʀᴀᴛɪᴏɴ :** 5:17" in caption
    assert "> ◯ **Bʏ :** Ayush" in caption
    assert "> ❖ **Mᴀᴅᴇ Bʏ :** [Ayush](https://t.me/Civilianssz)" in caption
