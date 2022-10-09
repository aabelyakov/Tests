# Author: pythontoday
# YouTube: https://www.youtube.com/c/PythonToday/videos

import re
import os
from bs4 import BeautifulSoup as BS

FILE = "blank/index.html"

with open(FILE) as file:
    src = file.read()
# endwith

print(1, src)

soup = BS(src, "lxml")
title = soup.title
print(2, title)
print(3, title.text)
print(4, title.string)

# методы .find() и .find_all()
page_h1 = soup.find("h1")
print(5, page_h1)

page_all_h1 = soup.find_all("h1")
print(6, page_all_h1)

for item in page_all_h1:
    print(7, item.text)

user_name = soup.find("div", class_="user__name")
print(8, user_name.text.strip())

user_name = soup.find(class_="user__name").find("span").text
print(9, user_name)

find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
print(11, find_all_spans_in_user_info)

for item in find_all_spans_in_user_info:
    print(12, item.text)

print(13, find_all_spans_in_user_info[0])
print(14, find_all_spans_in_user_info[2].text)

social_links = soup.find(class_="social__networks").find("ul").find_all("a")
print(15, social_links)

all_a = soup.find_all("a")
print(16, all_a)

for item in all_a:
    item_text = item.text
    item_url = item.get("href")
    print(17, f"{item_text}: {item_url}")

# Методы .find_parent() и .find_parents()
post_div = soup.find(class_="post__text").find_parent()
print(18, post_div)

post_div = soup.find(class_="post__text").find_parent("div", "user__post")
print(19, post_div)

post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
print(20, post_divs)

# Методы .next_element и .previous_element
next_el = soup.find(class_="post__title").next_element.next_element.text
print(21, next_el)

next_el = soup.find(class_="post__title").find_next().text
print(22, next_el)

# Методы .find_next_sibling() и .find_previous_sibling()
next_sib = soup.find(class_="post__title").find_next_sibling()
print(23, next_sib)

prev_sib = soup.find(class_="post__text").find_previous_sibling()
print(24, prev_sib)

post_title = soup.find(class_="post__text").find_previous_sibling().find_next().text
print(25, post_title)

links = soup.find(class_="social__networks").find_all("a")
print(26, links)

for link in links:
    link_href_attr = link.get("href")
    link_href_attr1 = link["href"]
    print(27, link_href_attr1)

find_a_by_text = soup.find("a", text="Одежда")
print(29, find_a_by_text)

find_a_by_text = soup.find("a", text="Одежда для взрослых")
print(30, find_a_by_text)

find_a_by_text = soup.find("a", text=re.compile("Одежда"))
print(31, find_a_by_text)

find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
print(32, find_all_clothes)
