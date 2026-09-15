from html import escape


def format_stream_caption(title, duration, by, info_link=None):
    safe_title = escape(str(title))
    safe_duration = escape(str(duration))
    safe_by = escape(str(by))

    if info_link:
        title_text = (
            f'<a href="{escape(str(info_link), quote=True)}">'
            f'{safe_title}</a>'
        )
    else:
        title_text = safe_title

    return (
        f"<blockquote>❖ <b>Sᴛᴀʀᴛᴇᴅ Sᴛʀᴇᴀᴍɪɴɢ</b></blockquote>\n"
        f"<blockquote>"
        f"◯ <b>Tɪᴛʟᴇ :</b> {title_text}\n"
        f"◯ <b>Dᴜʀᴀᴛɪᴏɴ :</b> {safe_duration} Mɪɴᴜᴛᴇs\n"
        f"◯ <b>Bʏ :</b> {safe_by}"
        f"</blockquote>\n"
        f'<blockquote>❖ <b>Mᴀᴅᴇ Bʏ...</b> '
        f'<a href="https://t.me/Civilianssz">Ayush</a></blockquote>'
    )


def format_queue_add_caption(
    current_title,
    current_duration,
    current_by,
    added_title,
    added_duration,
    added_by,
    position,
):
    from html import escape

    safe_current_title = escape(str(current_title))
    safe_current_duration = escape(str(current_duration))
    safe_current_by = escape(str(current_by))
    safe_added_title = escape(str(added_title))
    safe_added_duration = escape(str(added_duration))
    safe_added_by = escape(str(added_by))

    return (
        "<blockquote>❖ <b>Qᴜᴇᴜᴇ</b></blockquote>\n"
        "<blockquote>"
        f"◯ <b>Nᴏᴡ Pʟᴀʏɪɴɢ :</b> {safe_current_title}\n"
        f"◯ <b>Dᴜʀᴀᴛɪᴏɴ :</b> {safe_current_duration}\n"
        f"◯ <b>Bʏ :</b> {safe_current_by}"
        "</blockquote>\n"
        "<blockquote>"
        f"◯ <b>#{int(position)} —</b> {safe_added_title}\n"
        f"◯ <b>Dᴜʀᴀᴛɪᴏɴ :</b> {safe_added_duration}\n"
        f"◯ <b>Bʏ :</b> {safe_added_by}"
        "</blockquote>"
    )
