from AnonXMusic.utils.stream.stream import format_queue_add_caption


def test_queue_add_caption_shows_current_song_and_added_song():
    caption = format_queue_add_caption(
        current_title="Tum Ho",
        current_duration="5:17",
        current_by="Ayush",
        added_title="Saanson Ko Full Video - Zid",
        added_duration="4:00",
        added_by="off",
        position=2,
    )

    assert "<blockquote>" in caption
    assert "❖ <b>Qᴜᴇᴜᴇ</b>" in caption
    assert "◯ <b>Nᴏᴡ Pʟᴀʏɪɴɢ :</b> Tum Ho" in caption
    assert "◯ <b>Dᴜʀᴀᴛɪᴏɴ :</b> 5:17" in caption
    assert "◯ <b>Bʏ :</b> Ayush" in caption
    assert "◯ <b>#2 —</b> Saanson Ko Full Video - Zid" in caption
    assert "◯ <b>Dᴜʀᴀᴛɪᴏɴ :</b> 4:00" in caption
    assert "◯ <b>Bʏ :</b> off" in caption
    assert "Added To Queue" not in caption
