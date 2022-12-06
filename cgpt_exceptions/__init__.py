import json
import os
import re
import sys
import traceback
import warnings

from revChatGPT.revChatGPT import Chatbot

def initialize_cgpt_exceptions():
    with open("cgpt_exceptions_config.json", "r") as f:
        config = json.load(f)

    chatbot = Chatbot(config, conversation_id=None)

    def cgpt_exception_handler(exception_type, exception, tb):
        print("Traceback (most recent call last)")
        x = traceback.format_tb(tb)
        tb_string = "".join(x)[:-1]
        print(tb_string)
        print(f"{exception_type.__name__}: {exception}")
        last_frame = x[-1]
        match = re.search('File "(.*)", line \d+', last_frame)
        last_filename = match.group(1)
        last_file_prompt = ""
        if last_filename != "<stdin>":
            with open(last_filename, "r") as f:
                last_file = f.read()
                last_file_prompt = f"from the following code:\n```\n{last_file}\n```"
        print("\nLet's see what ChatGPT has to say...\n")
        chatbot.reset_chat()
        chatbot.refresh_session()
        resp = chatbot.get_chat_response(
            f"""
            Please correct the following python exception:\n```\n{tb_string}\n```\n{last_file_prompt}
            """,
            output="text",
        )
        print(resp['message'])

    sys.excepthook = cgpt_exception_handler

if os.path.exists("cgpt_exceptions_config.json"):
    initialize_cgpt_exceptions()
else:
    warnings.warn("No cgpt_exceptions_config.json found: Unable to initialize cgpt_exceptions")