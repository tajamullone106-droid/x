from AnonXMusic.platforms.Youtube import build_shruti_download_url


def test_build_shruti_audio_url():
    url = build_shruti_download_url(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )

    assert url.startswith("https://shrutibots.site/download?")
    assert "url=dQw4w9WgXcQ" in url
    assert "type=audio" in url


def test_build_shruti_video_url():
    url = build_shruti_download_url(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "video",
    )

    assert url.startswith("https://shrutibots.site/download?")
    assert "url=dQw4w9WgXcQ" in url
    assert "type=video" in url
