from AnonXMusic.plugins.bot import start


def test_start_sticker_pack_loader_returns_file_ids(monkeypatch):
    class Sticker:
        def __init__(self, file_id):
            self.file_id = file_id

    async def fake_get_stickers(short_name):
        assert short_name == "Ishahahahahahaha_by_fStikBot"
        return [Sticker("s1"), Sticker("s2"), Sticker("s3")]

    monkeypatch.setattr(start.app, "get_stickers", fake_get_stickers)

    start._START_STICKERS = None

    import asyncio
    stickers = asyncio.run(start._load_start_stickers())

    assert stickers == ["s1", "s2", "s3"]
