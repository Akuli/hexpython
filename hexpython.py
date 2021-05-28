import contextlib
import io
import traceback

import hexchat


__module_name__ = "hexpython"
__module_version__ = "0.1"
__module_description__ = "Run Python code in hexchat and post result to channel"

print("Hexpython plugin loaded.")


def py_callback(split_to_words, word_to_end, userdata):
    python_code = word_to_end[1]
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


hexchat.hook_command("PY3", py_callback, help="/PY code Run Python code and post result to channel")
