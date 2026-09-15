from AnonXMusic.utils.inline.queue import format_queue_caption


def test_queue_caption_uses_separate_html_quotes():
    caption = format_queue_caption(
        "Tum Ho",
        "5:17",
        "Ayush",
        [
            ("Agar Tum Saath Ho", "5:41"),
            ("Phir Le Aya Dil", "5:05"),
        ],
    )

    assert "<blockquote>" in caption
    assert "❖ <b>Qᴜᴇᴜᴇ</b>" in caption
    assert "◯ <b>Nᴏᴡ Pʟᴀʏɪɴɢ :</b>" in caption
    assert "Tum Ho" in caption
    assert "◯ <b>Dᴜʀᴀᴛɪᴏɴ :</b> 5:17" in caption
    assert "◯ <b>Bʏ :</b> Ayush" in caption
    assert "◯ <b>#2 —</b> Agar Tum Saath Ho" in caption
    assert "◯ <b>#3 —</b> Phir Le Aya Dil" in caption
