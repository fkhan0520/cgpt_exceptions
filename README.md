# cgpt_exceptions

Use ChatGPT to give helpful advice when your python program fails

# Usage

1. Install through git:
```
pip install git+https://github.com/fkhan0520/cgpt_exceptions
```
2. Create a `cgpt_exceptions_config.json` file with your OpenAI auth info and put it in the same directory as wherever `python` is invoked. It can use either your username/password or auth token. Full details in the [revChatGPT docs](https://github.com/acheong08/ChatGPT)

3. Just import the package and invoke your program as normal!
```python
import cgpt_exceptions
import os

def foo():
    os.listdir("a-random-directory")

foo()
```

```
Traceback (most recent call last)
  File "/Users/farhan/test.py", line 7, in <module>
    foo()
  File "/Users/farhan/test.py", line 5, in foo
    os.listdir("a-random-directory")
FileNotFoundError: [Errno 2] No such file or directory: 'a-random-directory'

Let's see what ChatGPT has to say...

Here are a few ways you can correct the exception:

1. Make sure that the directory "a-random-directory" exists and you have permission to access it.

2. Handle the `FileNotFoundError` exception that is raised when the directory doesn't exist by using a `try`-`except` block:

import os

def foo():
    try:
        os.listdir("a-random-directory")
    except FileNotFoundError:
        print("Directory not found.")

foo()

```

# How it works

Sends ChatGPT the following prompt when an exception is thrown anywhere during execution:
```
Please correct the following python exception:
<your stacktrace>
from the following code:
<file where exception was thrown>
```

Huge thanks to [acheong8](https://github.com/acheong08) for making this super straightforward with their [revChatGPT package](https://github.com/acheong08/ChatGPT)

