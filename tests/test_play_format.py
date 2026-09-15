from AnonXMusic.utils.stream.stream import format_stream_caption


def test_stream_caption_uses_real_html_quotes_and_clickable_ayush():
    caption = format_stream_caption(
        "Tum Ho",
        "5:17",
        "Ayush",
        "https://t.me/example",
    )

    assert "<blockquote>" in caption
    assert "</blockquote>" in caption

    assert "❖ <b>Sᴛᴀʀᴛᴇᴅ Sᴛʀᴇᴀᴍɪɴɢ</b>" in caption
    assert "◯ <b>Tɪᴛʟᴇ :</b>" in caption
    assert "◯ <b>Dᴜʀᴀᴛɪᴏɴ :</b>" in caption
    assert "◯ <b>Bʏ :</b>" in caption

    assert '<a href="https://t.me/example">Tum Ho</a>' in caption
    assert '<a href="https://t.me/Civilianssz">Ayush</a>' in caption

    assert "**" not in caption
    assert "[Ayush]" not in caption
    assert "https://t.me/Civilianssz" in caption


def test_no_legacy_stream_caption_references():
    from pathlib import Path

    files = [
        Path("AnonXMusic/core/call.py"),
        Path("AnonXMusic/plugins/admins/skip.py"),
        Path("AnonXMusic/plugins/admins/callback.py"),
    ]

    for path in files:
        text = path.read_text()
        assert '["stream_1"]' not in text
        assert '["stream_2"]' not in text
