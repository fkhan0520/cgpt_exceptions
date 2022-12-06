from setuptools import setup, find_packages
setup(
    name = "cgpt_exceptions",
    version = "0.1",
    author = "Farhan Khan",
    author_email = "fkhan0520@gmail.com",
    description = "cgpt_exceptions provides helpful tips for code failures with ChatGPT",
    packages = find_packages(),
    url = "https://github.com/fkhan0520/cgpt_exceptions",
    install_requires = [
        "revChatGPT",
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)