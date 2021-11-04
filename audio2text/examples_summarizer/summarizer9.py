
# install file formater
# /bin/python3 -m pip install -U autopep8


# https://blog.paperspace.com/generating-text-summaries-gpt-2/
# https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88
# Putting it all together

# The full code is this:

"""
import openai
import wget
import pathlib
import pdfplumber
import numpy as np


def getPaper(paper_url, filename="random_paper.pdf"):
    downloadedPaper = wget.download(paper_url, filename)
    downloadedPaperFilePath = pathlib.Path(downloadedPaper)
    return downloadedPaperFilePath


def showPaperSummary(paperContent):
    tldr_tag = "\n tl;dr:"
    openai.organization = 'API KEY org'
    openai.api_key = "your openAI key"
    engine_list = openai.Engine.list()

    for page in paperContent:
        text = page.extract_text() + tldr_tag
        response = openai.Completion.create(engine="davinci", prompt=text, temperature=0.3,
                                            max_tokens=140,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0,
                                            stop=["\n"]
                                            )
        print(response["choices"][0]["text"])


paperContent = pdfplumber.open(paperFilePath).pages
showPaperSummary(paperContent)
"""