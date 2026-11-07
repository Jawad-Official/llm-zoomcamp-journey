"""Lesson 8: data loading helpers.

Simple version: this file is the "librarian".
- load_faq_data() downloads every FAQ card (question + answer) from the DataTalks.Club website.
- build_index() puts those cards into a minsearch index, so we can find the right cards fast.
"""
import requests
from minsearch import Index


# Download the list of courses, then every course's FAQ cards, into one big list.
def load_faq_data():
    docs_url = "https://datatalks.club/faq/json/courses.json"
    response = requests.get(docs_url)
    courses_raw = response.json()

    documents = []
    url_prefix = "https://datatalks.club/faq"

    for course in courses_raw:
        course_url = f"""{url_prefix}{course["path"]}"""
        course_response = requests.get(course_url)
        course_response.raise_for_status()
        course_data = course_response.json()

        documents.extend(course_data)

    return documents


# Build the search "book index": search the text fields, filter by course.
def build_index(documents):
    index = Index(
        text_fields=["question", "section", "answer"],
        keyword_fields=["course"]
    )
    index.fit(documents)
    return index