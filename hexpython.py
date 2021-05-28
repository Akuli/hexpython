import contextlib
import io
import traceback

import hexchat


__module_name__ = "hexpython"
__module_version__ = "0.1"
__module_description__ = "Run Python code in hexchat and post result to channel"

print("Hexpython plugin loaded.")


currently_running = False


def message_callback(words, words_to_end, userdata):
    if not words or words[0] != '>>>':
        return hexchat.EAT_NONE

    python_code = words_to_end[1]
    output_stream = io.StringIO()

    with contextlib.redirect_stdout(output_stream):
        with contextlib.redirect_stderr(output_stream):
            try:
                exec(compile(python_code, "<hexpython>", mode="single"))
            except BaseException:
                traceback.print_exc()

    output = output_stream.getvalue().replace('\n', ' ').strip()[:100] or '(no output)'
    channel = hexchat.get_info("channel")
    hexchat.command(f"msg {channel} >>> {python_code}")
    hexchat.command(f"msg {channel} {output}")
    return hexchat.EAT_ALL


hexchat.hook_command("", message_callback)
